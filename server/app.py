import botocore
import boto3
from flask import Flask, redirect, url_for, request, jsonify
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import json

UPLOAD_FOLDER = '/Users/alex/sources/hack-a-thing-2-23w-alexander-chen-hack-a-thing-2/tmp/'

app = Flask(__name__)

app.config['S3_BUCKET'] = "S3_BUCKET_NAME"
app.config['S3_KEY'] = "AWS_ACCESS_KEY"
app.config['S3_SECRET'] = "AWS_ACCESS_SECRET"
app.config['S3_LOCATION'] = 'http://{}.s3.amazonaws.com/'.format(
    app.config['S3_BUCKET'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

s3 = boto3.client(
    "s3",
    aws_access_key_id=app.config['S3_KEY'],
    aws_secret_access_key=app.config['S3_SECRET']
)


# to test:
# curl -X POST -F 'file=@/Users/alex/sources/hack-a-thing-2-23w-alexander-chen-hack-a-thing-2/server/files/example.mp4' http://127.0.0.1:5000

@app.route("/", methods=["POST"])
def upload_file():
    print(f"uploading file: {request.files}")

    ok = {'status': 'OK'}
    err = {'status': 'NOT OK'}
    if 'file' not in request.files:
        return json.dumps(err)

    file = request.files['file']
    if file.filename == '':
        return json.dumps(err)

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return json.dumps(ok)
