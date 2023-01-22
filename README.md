# Back-end for Re:New (UofTHacks X)

## DOCUMENTATION

* Note: The upload feature may not be working properly

* Note: The API Endpoint is at local host at http://0.0.0.0:105/

* Note: The AWS Cloud comes preloaded with 5 sample users: 'user1', 'johndoe66', 'emilysmith08', 'jessicadonn1', 'tianjiyuan12'. Each have their own posts. 



###### 1. USING THE COHERE API THROUGH FLASK

To generate 4 random tasks, use the 'GET' method on the extension /category/<string:category>/. 

This should return a JSON of an array of 4 random tasks, given a category. The <string:category> MUST be exactly one of: 'skill', 'academic', 'fitness', or 'wellness'.

For example, in Postman, you could send a 'GET' method to http://0.0.0.0:105/category/skill, and this would return: 
[
    " Read one new book",
    " Watch one new documentary",
    " Take one new course",
    " Write one new article"
]



###### 2. UPLOADING IMAGES TO THE AWS CLOUD

To upload images to the AWS Cloud, including DynamoDB and S3, use the 'POST' method on the extension /upload.

This should return a JSON message of 'File uploaded successfully', or 'Invalid file type.'

* This one I am not sure what to do


###### 3. DOWNLOADING/GETTING A PHOTO's UNIVERSAL URL AND CAPTION

To get the universal URL and the caption of a photo, use the 'GET' method on the extension /download/<string:postid>, where the postid is the UUID of an image. This is likely not useful as it is a helper function.

This should return the URL and caption in the form {'url': url, 'caption': caption}

For example, in Postman, you could send a 'GET' method to http://0.0.0.0:105/download/testpost1, and this would return: 
{
    "caption": "I love Re:New!",
    "url": "https://renewphotos.s3.amazonaws.com/UNADJUSTEDNONRAW_thumb_26.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT45JMXVXYVQQSDYK%2F20230122%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20230122T014739Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=8f00f70ab76d235f370cdfbcab27813aa4140f4594b179cb51a67ae4ffd4c984"
}



###### 4. GETTING A USER's POST HISTORY

To get a user's post history (or equilvalently, all their posts), use the 'GET' method on the extension /history/<string:user>, where user is the username. 

This should return a JSON of each post and their information. The information includes: caption (string), and the universal url (string).  

For example, in Postman, you could send a 'GET' method to http://0.0.0.0:105/history/user1, and this would return:
[
    {
        "caption": "I love Re:New!",
        "url": "https://renewphotos.s3.amazonaws.com/UNADJUSTEDNONRAW_thumb_26.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT45JMXVXYVQQSDYK%2F20230122%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20230122T014914Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=91baef24852d65474314529e7822fd1056de02f376e5d3d4362c30536763a9c7"
    },
    {
        "caption": "My second post!",
        "url": "https://renewphotos.s3.amazonaws.com/UNADJUSTEDNONRAW_thumb_2d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT45JMXVXYVQQSDYK%2F20230122%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20230122T014914Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=1c9f49455f14ee1974c3679f615291b8a456b617507c8077dd665d45cd04cf9c"
    }
]


###### 5. GETTING EVERY POST FROM EACH PERSON EXACTLY ONCE

To get every post from each person exactly once, meaning one person doesn't appear twice, use the 'GET' method on the extension /allposts.

This should return a JSON of each post, including all the information: 'caption' (string), 'image' (universal URL/string), 'postid' (string/UUID), 'user' (string), 'verified' (bool)

For example, in Postman, you could send a 'GET' method on the extension http://0.0.0.0:105/allposts, and this would return:
[
    {
        "caption": "I love Re:New!",
        "image": "https://renewphotos.s3.amazonaws.com/UNADJUSTEDNONRAW_thumb_26.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT45JMXVXYVQQSDYK%2F20230122%2Fca-central-1%2Fs3%2Faws4_request&X-Amz-Date=20230122T015010Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=525e16d6832e9f0bc2065086d2e71c084c5461b9b0b1fdf260f9010b2f95ad15",
        "postid": "testpost1",
        "user": "user1",
        "verified": false
    }
]
