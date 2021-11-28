
# insert your api key
def make_request():
    import urequests as requests
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Rostock&units=metric&APPID=YOUR_API_KEY")
    data = r.json()
    return data