# REST API
from werkzeug.utils import secure_filename
from cohere_rest import generateTasks
from flask import Flask, jsonify, request
from aws import s3, bucket_name, db, table, postImage, retrieveImage, postHistory, retrieveAll

app = Flask(__name__)

# checking if the extension is alright
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'gif']

# the request gets sent to 0.0.0.0/category/STRING where the STRING is the request that you can get and post using the function below

# This generates 4 unique prompts in an array of strings
@app.route('/category/<string:category>/', methods=['GET'])
def cohere_run_m(category):
    return jsonify(generateTasks(category))

# We are assuming that the file is being recieved as type FILE and not a BLOB in any situation
@app.route('/upload', methods=['POST'])
def upload():
    # Get the image file from the form data
    image = request.files['image']
    # Get the user from the form data
    user = request.form['user']
    # Get the caption from the form data
    caption = request.form['caption']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        s3.upload_fileobj(image, bucket_name, filename)
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'message': 'Invalid file type'})

# download (filename) takes the postid with meta data in the dynamodb and in the AWS S3 bucket and returns the universal URL to view it and caption
@app.route('/download/<string:postid>', methods=['GET'])
def download(postid):
    imageData = retrieveImage(postid)
    caption = imageData[0]
    filename = imageData[1]

    data = s3.get_object(Bucket=bucket_name, Key = filename)
    url = s3.generate_presigned_url('get_object', Params = {
        'Bucket': bucket_name,
        'Key': filename
    }, ExpiresIn = 3600)

    return {'url': url, 'caption': caption}

# This gets post history in the form of a JSON where each item is a [url, caption]
@app.route('/history/<string:user>', methods=['GET'])
def history(user):
    posts = []
    postIds = postHistory(user)
    for postid in postIds:
        posts.append(download(postid))
    return jsonify(posts)

@app.route('/allposts', methods=['GET'])
def allPosts():
    posts = retrieveAll()
    for post in posts:
        post['image'] = download(post['postid'])['url']

    return jsonify(posts)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)