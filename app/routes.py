import os
from app import app
from flask import render_template, request, redirect, url_for, send_file, send_from_directory
from app.answer_xlsx import create_answer_table, create_answer_excel
from app.forms import partForm, fileForm
from werkzeug.utils import secure_filename


@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    formInput = partForm()
    formFile = fileForm()
    if formInput.validate_on_submit():
        parts = formInput.post.data
        table_answer = []
        if len(parts.split()) > 10:
            args["input_size_error"] = True
        else:
            table_answer = create_answer_table(parts, formInput.serv_lev.data)
        args["method"] = "POST"
        return render_template("index.html", form=formInput, table_answer=table_answer, args=args)
    if formFile.validate_on_submit():
        filename = secure_filename(formFile.file.data.filename)
        if filename in app.config['ALLOWED_EXTENSIONS']:
            file_bytes = formFile.file.data.read(app.config['MAX_FILE_SIZE'])
            args["file_size_error"] = len(file_bytes) == app.config['MAX_FILE_SIZE']
            if not args["file_size_error"]:
                create_answer_excel(file_bytes.decode(), formFile.levels.data)
        else:
            args["file_size_error"] = True
        return send_from_directory(os.path.join(os.getcwd(), 'excel_files'), 'answer.xlsx', as_attachment=True)
        args["method"] = "POST"
    return render_template("index.html", args=args, formInput=formInput, formFile=formFile)
