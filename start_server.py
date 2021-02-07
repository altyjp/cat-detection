# -*- coding: utf-8 -*-
import os
import uuid
import base64
import numpy as np
from cat import Cat
from flask import Flask, request, jsonify
import json
import cv2

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

    # decode json string
    request_row_data = request.data.decode('utf-8')
    request_json_data = json.loads(request_row_data)
    request_img = request_json_data["image"]

    img_binary = base64.b64decode(request_img.split(",")[1])
    jpg=np.frombuffer(img_binary,dtype=np.uint8)

    # save file
    #raw image <- jpg
    img = cv2.imdecode(jpg, cv2.IMREAD_COLOR)
    extend = 'jpg'
    save_file_path = os.path.join(app.config['UPLOAD_FOLDER'], result_id) + '.' + extend
    cv2.imwrite(save_file_path, img)

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
