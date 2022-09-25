# https://docs.python-requests.org/en/latest/user/quickstart/#custom-headers


# r = requests.get("http://ip-api.com/json/")
# print(r)
# print(r.content)  # content in bytes
# print(r.text)  # content in unicode
# print(r.json())  # json

# CUSTOM HEADERS
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent': 'my-app/0.0.1'}
#
# r = requests.get(url, headers=headers)


# POST REQUEST WITH PAYLOAD
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# r = requests.post("https://httpbin.org/post", data=payload)
# print(r.text)
# {
#     ...
# "form": {
#     "key2": "value2",
#     "key1": "value1"
# },
# ...
# }

# BUILT IN JSON ENCODING json=payload
# url = 'https://api.github.com/some/endpoint'
# payload = {'some': 'data'}
#
# r = requests.post(url, json=payload)

# REQUEST STATUS CODE
# r = requests.get('https://httpbin.org/get')
# r.status_code
# 200

# insert your api key
def make_request():
    import urequests as requests
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Rostock&units=metric&APPID=YOUR_API_KEY")
    data = r.json()
    return data


