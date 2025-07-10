import json

def lambda_handler(event, context):
    # for allow only require method to 
    '''
    if event['requestContext']['http']['method'] != 'POST':
        return {
            'statusCode': 403,
            'body': 'give only post method support'
        }
'''

    #num1 = 5
    #num2 = 10
    print("********")
    print(event)
    print("********")

    request_body = json.loads(event['body'])
    
    print("******")
    print(request_body)
    print("******")

    num1 = request_body['num1']
    num2 = request_body['num2']

    sum = num1 + num2
    sub = num2 - num1
    mul = num1 * num2
    div = num1 / num2

    return {
        'statusCode': 200,
        'body': {
            "sum": sum,
            "sub": sub,
            "mul": mul,
            "div": div
        }
    }
