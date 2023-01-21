import boto3

# client is an interface that interacts with AWS
db = boto3.resource(
    "dynamodb",
    aws_access_key_id='AKIAT45JMXVXYVQQSDYK',
    aws_secret_access_key='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',
    region_name='ca-central-1',
)

table = db.Table("renewposts")

def postImage(user: str, caption: str, image: str):
    try:
        table.put_item(
            Item={"user": user, "caption": caption, "image": image},
            ConditionExpression=f"attribute_not_exists({user})",
        )
    except:
        print("This user has already posted.")

def retrieveImage(user: str):
    response = table.get_item(Key={"user": user})
    image = response["Item"]["image"]
    caption = response["Item"]["caption"]
    return [caption, image]
