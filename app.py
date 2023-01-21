# Setting up modules
from cohere_rest import generateTasks
from flask import Flask, jsonify, request
from aws import s3, bucket_name, db, table, postImage, retrieveImage
# from flask_restful import Api, Resource

app = Flask(__name__)

# Request: category (string), Response: tasks (array of strings)

# the request gets sent to 0.0.0.0/category/STRING where the STRING is the request that you can get and post using the function below

# RESTful API
@app.route('/category/<string:category>/', methods=['GET'])
def cohere_run_m(category):
    # print(category)
    return jsonify(generateTasks(category))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file_data = file.read()
    s3.put_object(Bucket=bucket_name, Key=file.filename, Body=file_data)
    return jsonify({'message': 'File uploaded successfully'})

# download (filename) takes the filename in the AWS S3 bucket and returns the universal URL to view it
@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
    data = s3.get_object(Bucket=bucket_name, Key=filename)
    file_data = data['Body'].read()
    print(file_data)

    url = s3.generate_presigned_url('get_object', Params={
        'Bucket': bucket_name,
        'Key': filename
    }, ExpiresIn = 3600)

    return url

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)