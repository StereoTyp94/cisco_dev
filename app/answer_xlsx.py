import openpyxl, os
from app import db
from app.models import Product, Service


def create_answer(part_str):
    parts = part_str.split()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(
        ['Part#', 'SKU', 'Price', 'Комментарий']
    )
    line = 2
    for part in parts:
        result = db.session.query(Product.part, Service.sku, Service.serv_gpl).join(Service).\
            filter(Service.serv_lev == 'SNT', Product.part == part).first()
        if result:
            ws.cell(row=line, column=1).value = result[0]
            ws.cell(row=line, column=2).value = result[1]
            ws.cell(row=line, column=3).value = result[2]
        else:
            ws.cell(row=line, column=1).value = part
            ws.cell(row=line, column=4).value = 'Оборудование EndOfSupport или не имеет отдельного смартнета.'
        line += 1
    wb.save(os.path.join(os.getcwd(), 'excel_files', 'answer.xlsx')) #попробовать отправить файл без сохранения
    #отправляем файл на почту
    #os.remove(os.path.join(os.getcwd(), 'excel_files', 'answer.xlsx')) #удаляем файл


# db.session.query(Product.part, Service.sku, Service.serv_gpl).join(Service)\
#     .filter(Service.serv_lev == 'SNT', Product.part == '01FT600X').all()