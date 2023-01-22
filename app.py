# REST API
from werkzeug.utils import secure_filename
from cohere_rest import generateTasks
from flask import Flask, jsonify, request
from aws import s3, bucket_name, db, table, postImage, retrieveImage, postHistory, retrieveAll

app = Flask(__name__)

# Checking that the file extension is a valid image
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'gif']

# Generating tasks
@app.route('/category/<string:category>/', methods=['GET'])
def cohere_run_m(category):
    return jsonify(generateTasks(category))

# Uploading images to the cloud
@app.route('/upload', methods=['POST'])
def upload():
    # Get the image file, user, and caption from the form data
    image = request.files['image']
    user = request.form['user']
    caption = request.form['caption']

    if image and allowed_file(image.filename):
        filename = secure_filename(image.filename)
        s3.upload_fileobj(image, bucket_name, filename)
        return jsonify({'message': 'File uploaded successfully'})
    else:
        return jsonify({'message': 'Invalid file type'})

# Downloading images from the cloud in the form of a universal URL
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

# Get the post history of a given user
@app.route('/history/<string:user>', methods=['GET'])
def history(user):
    posts = []
    postIds = postHistory(user)

    for postid in postIds:
        posts.append(download(postid))

    return jsonify(posts)

# Get posts from every user exactly once
@app.route('/allposts', methods=['GET'])
def allPosts():
    posts = retrieveAll()

    for post in posts:
        post['image'] = download(post['postid'])['url']

    return jsonify(posts)

# Running the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)