# Back-end for Re:New (UofTHacks X)

## DOCUMENTATION

* Note: The upload feature may not be working properly

** Note: The API Endpoint is at local host at http://0.0.0.0:105/

USING THE COHERE API THROUGH FLASK

To generate 4 random tasks, use the 'GET' method on the extension /category/<string:category>/. 

This should return a JSON of an array of 4 random tasks, given a category. The <string:category> MUST be exactly one of: 'skill', 'academic', 'fitness', or 'wellness'.

UPLOADING IMAGES TO THE AWS CLOUD

To upload images to the AWS Cloud, including DynamoDB and S3, use the 'POST' method on the extension /upload.

This should return a JSON message of 'File uploaded successfully', or 'Invalid file type.'

DOWNLOADING/GETTING A PHOTO's UNIVERSAL URL AND CAPTION

To get the universal URL and the caption of a photo, use the 'GET' method on the extension /download/<string:postid>, where the postid is the UUID of an image. This is likely not useful as it is a helper function.

This should return the URL and caption in the form {'url': url, 'caption': caption}

GETTING A USER's POST HISTORY

To get a user's post history (or equilvalently, all their posts), use the 'GET' method on the extension /history/<string:user>, where user is the username. 

This should return a JSON of each post and their information. The information includes: caption (string), and the universal url (string).  

GETTING EVERY POST FROM EACH PERSON EXACTLY ONCE

To get every post from each person exactly once, meaning one person doesn't appear twice, use the 'GET' method on the extension /allposts.

This should return a JSON of each post, including all the information: 'caption' (string), 'image' (universal URL/string), 'postid' (string/UUID), 'user' (string), 'verified' (bool)



