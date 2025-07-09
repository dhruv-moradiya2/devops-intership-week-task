import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3')
    num1 = 5
    num2 = 10
    
    #num1 = event['num1']
    #num2 = event['num2']

    sums = num1 + num2
    sub = num2 - num1
    mul = num1 * num2
    div = num1 / num2

    response = client.list_buckets()
    print(response)
    s3_bucket = response['Buckets']
    length = len(s3_bucket)

    for i in s3_bucket:
        print(i['Name'])
        print()
        print(i['CreationDate'])

    return {
        'statusCode': 200,
        'body': {
            "sum": sums,
            "minus": sub,
            "multiply": mul,
            "divide": div,
            "list": length
        }
    }
