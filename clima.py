import requests

def temperatura():
    city =("Santiago")
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=54144da4d6d0ec812cb4b2b11ea48124&units=metric".format(city) #https://openweathermap.org

    res = requests.get(url)
    data = res.json()
    print(data)
    return data


