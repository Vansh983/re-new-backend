# AWS CLOUD
import boto3
from boto3.dynamodb.conditions import Key
import uuid

# Initializing our API keys - Replace with generic ones when going public
s3 = boto3.client('s3',
    aws_access_key_id='XXXXX',
    aws_secret_access_key='XXXXX',
    region_name='ca-central-1'
)

bucket_name = 'renewphotos'

db = boto3.resource(
    "dynamodb",
    aws_access_key_id='XXXXX',
    aws_secret_access_key='XXXXX',
    region_name='ca-central-1',
)

table = db.Table("renewposts")

# Posting an image
def postImage(user: str, caption: str, image: str):
    try:
        postid = str(uuid.uuid1())
        table.put_item(
            Item={"postid": postid, "user": user, "caption": caption, "image": image, "verified": False},
            ConditionExpression=f"attribute_not_exists({postid})",
        )
    except:
        print("This user has already posted.")

# Retrieving an image, given the postid (UUID)
def retrieveImage(postid: str):
    response = table.get_item(Key={"postid": postid})
    image = response["Item"]["image"] # filename to find in s3
    caption = response["Item"]["caption"]

    return [caption, image]

# Get all the posts of a user
def postHistory(user: str):
    response = table.scan(FilterExpression = Key("user").eq(user))
    postIds = [item["postid"] for item in response["Items"]]

    return postIds

# Get every post from each user exactly once
def retrieveAll():
    response = table.scan()
    items = response["Items"]
    unique_users = set()
    unique_items = []

    for item in items:
        if item["user"] not in unique_users:
            unique_users.add(item["user"])
            unique_items.append(item)

    return unique_items
