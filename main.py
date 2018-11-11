from flask import Flask, request, send_file
import os

UPLOAD_FOLDER = '/tmp'
PDF_OUTPUT_PATH = os.path.join(UPLOAD_FOLDER, 'doc.pdf')
NUM_ALLOWED_CSSFILES = 10
NUM_ALLOWED_IMGFILES = 10

app = Flask(__name__)


def handle_file(file_id):
    try:
        uploaded_file = request.files[file_id]
    except KeyError:
        return None
    path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    uploaded_file.save(path)
    return path


@app.route('/', methods=['POST'])
def hello():
    htmlfile_path = handle_file('htmlfile')
    for i in range(NUM_ALLOWED_CSSFILES):
        handle_file(f'cssfile{i+1}')
    for i in range(NUM_ALLOWED_IMGFILES):
        handle_file(f'imgfile{i+1}')

    os.system(f'prince {htmlfile_path} -o {PDF_OUTPUT_PATH}')
    return send_file(PDF_OUTPUT_PATH)
