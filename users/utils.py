import requests
import environ

env = environ.Env()
environ.Env.read_env()

api_key = env('API_KEY') 
print(api_key)
def send_otp(otp, phone):

    url = f"https://2factor.in/API/V1/{api_key}/SMS/{phone}/{otp}"

    # querystring = {"authorization":f"{api_key}","variables_values":f"{str(otp)}","route":"otp","numbers":f"{str(phone)}"}

    # headers = {
    #     'cache-control': "no-cache"
    # }

    response = requests.request("GET", url)

    print(response.text)