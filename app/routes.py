from app import app
from flask import render_template, request, redirect, url_for
from app.answer_xlsx import create_answer_table, create_answer_excel
from app.forms import partForm


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index():
    args = {"method": "GET"}
    form = partForm()
    if form.validate_on_submit():
        part = form.post.data
        if len(part.split()) > 5:
            table_answer = False
            args["input_size_error"] = True
        else:
            table_answer = create_answer_table(part)
        args["method"] = "POST"
        return render_template("index.html", form=form, table_answer=table_answer, args=args)
    if request.method == "POST":
        file = request.files["myfile"]
        if allowed_file(file.filename):
            file_bytes = file.read(app.config['MAX_FILE_SIZE'])
            args["file_size_error"] = len(file_bytes) == app.config['MAX_FILE_SIZE']
            if len(file_bytes) == app.config['MAX_FILE_SIZE']:
                print('файл больше 1 мб')
            else:
                print('файл меньше 1 мб')
                #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                create_answer_excel(file_bytes.decode())
        else:
            args["file_size_error"] = True
        args["method"] = "POST"
    return render_template("index.html", args=args, form=form)
