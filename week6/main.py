# using request module install external lib and add in lambda 

import requests

def check_web_status(url):
    response = requests.get(url)
    # print(response.status_code)

    if response.status_code == 200: 
        return {
            'body': "website status is 200"
        }
    else:
        return {
            'body': "website status is 404"
        }


def lambda_handler(event, context):
    return check_web_status('https://apidog.com/blog/check-requests-status-python')