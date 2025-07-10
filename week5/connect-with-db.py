import json
import boto3

# this is connect with dynamodb
def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

    table = dynamodb.Table('users')

    username= event['username']
    first_name= event['f_name']
    last_name= event['l_name']
    age= event["age"]

    responce = table.put_item(
        Item={
            'username': username, # hash key for Partition key
            'first_name': first_name,
            'last_name': last_name, # Sort key for demo 
            'age': age
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps(responce)
    }

'''
{
    "username": "T1",
    "f_name": "dhruv",
    "l_name":"",
    "age": 22
}
'''


'''
get all item from db 

scan_param{
    tablename: <db_table>
}

res = dyanmodb.scan(**scan_parm)

add in for loop and convert this list in dict


'''


'''
# this is for push data using function url so takk
import json
import boto3 

def lambda_handler(event, context):
    
    print("************")
    print(event)
    print("************")


    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')

    table = dynamodb.Table('user-with-url')

    request_body = json.loads(event['body'])

    

    res = table.put_item(
        Item={
            "username": request_body['username'],
            "f_name": request_body['f_name'],
            "l_name": request_body['l_name'],
            "age": request_body['age']
        }
    )


    

    return {
        'statusCode': 200,
        'body': json.dumps(res)
    }


'''
