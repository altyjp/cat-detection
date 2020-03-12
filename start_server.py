# -*- coding: utf-8 -*-
import os
import uuid
from catDetector import catDetector
from flask import Flask, request, send_from_directory

UPLOAD_FOLDER = './static_resources/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# flask
app = Flask(__name__, static_folder='static_resources')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# catDetector
cat_detector = catDetector()

"""
POST /api/detect_cat/image
Post cat image for cat detection.
The cat detector called synchronously by this method,
and returns file name.
"""
@app.route('/api/detect_cat/image',methods=["POST"])
def post_detect_cat_image():
    result_id = str(uuid.uuid4())
    file = request.files['file']
    if file.filename == '':
        print('ERROR : No_file_uploaded')
        return '{"error_msg" : "ファイルがアップロードされていません。", "code" : "No_file_uploaded."} '
    if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS == 0:
        print('ERROR : Invaild_file_type')
        return '{"error_msg" : "ファイルが不正です。対応した画像ではありません。", "code" : "Invaild_file_type."} '

    # save file
    extend = '.' + file.filename.rsplit('.', 1)[1].lower()
    save_file_path = os.path.join(app.config['UPLOAD_FOLDER'], result_id) + extend
    file.save(save_file_path)
    # start detect
    cat_num = cat_detector.detect_cat(save_file_path)

    # retrun id
    return '{"file_name" : "' + result_id + extend + '", "cat_num" :' + str(cat_num) +' }'

# main
if __name__ == "__main__":
    # show server mapping.
    print(app.url_map)
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), \
    port=os.getenv("APP_PORT", 8080))
