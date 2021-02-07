# -*- coding: utf-8 -*-
import os
import uuid
import base64
from cat import Cat
from flask import Flask, request, jsonify

UPLOAD_FOLDER = './uploaded_cat_images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

# flask
app = Flask(__name__, static_folder='static_resources')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

"""
POST /api/detect_cat/image
Post cat image for cat detection.
The cat detector called synchronously by this method,
and returns image_base64
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
    extend = file.filename.rsplit('.', 1)[1].lower()
    save_file_path = os.path.join(app.config['UPLOAD_FOLDER'], result_id) + '.' + extend
    file.save(save_file_path)

    # start detect
    cat = Cat(save_file_path)

    # encode result
    encode_prefix = 'data:image/' + extend +';base64,'
    with open(cat.get_file_path(), "rb") as f:
        img_base64 = base64.b64encode(f.read()).decode('utf-8')

    response = {'cat_number' : cat.get_number() , 'encode_prefix' : encode_prefix, 'image_base64' : img_base64}

    # remove file
    os.remove(cat.get_file_path())

    # retrun result
    return jsonify(response)


# main
if __name__ == "__main__":
    # show server mapping.
    print(app.url_map)
    app.run(host='0.0.0.0', \
    port=os.getenv("APP_PORT", 8080))
