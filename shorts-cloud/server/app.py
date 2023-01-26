import boto3
from flask import Flask, redirect, url_for, request, jsonify
import os
from werkzeug.utils import secure_filename
from secret import S3_BUCKET, S3_KEY, S3_SECRET
import json

app = Flask(__name__)

app.config['S3_BUCKET'] = S3_BUCKET
app.config['S3_KEY'] = S3_KEY
app.config['S3_SECRET'] = S3_SECRET

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

    # this code will save the file to the os
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    s3.upload_fileobj(file.stream, app.config['S3_BUCKET'], filename)

    return json.dumps(ok)
