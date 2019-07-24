import openpyxl, os


def create_answer(part_str):
    parts = part_str.split()
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(
        ['Part#', 'SKU', 'Price']
    )
    for line in range(2, len(parts) + 2):
        ws.cell(row=line, column=1).value = parts[line - 2]
        ws.cell(row=line, column=2).value = 'sku' + str(line)
        ws.cell(row=line, column=3).value = 'price' + str(line)
    wb.save(os.path.join('C:\cisco_dev\\answers', 'answer.xlsx')) #попробовать отправить файл без сохранения
    #отправляем файл на почту
    #os.remove(os.path.join('C:\cisco_dev\\answers', 'answer.xlsx'))