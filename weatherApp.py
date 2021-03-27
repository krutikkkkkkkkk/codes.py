import requests #pip install requests
chk = 1
while chk >= 1:
    chk = chk + 1
    api = "  "  #Get API Key From OpenWeathermap.org
    city = input("Enter City Name: ")
    request = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,api))
    httpStatus = request.status_code
    print("Status Code: ", httpStatus)
    if httpStatus != 200:
        print("\nInvalid City\n")
    else:
        weather = request.json()['main']
        kelivn = 273
        temp = weather['temp']
        celcius = temp - kelivn
        feelsLike = weather['feels_like']
        feelsLike = feelsLike - kelivn
        wthStatus = request.json()['weather'][0]
        status = wthStatus['main']
        description = wthStatus['description']
        location = request.json()['sys']
        country = location['country']
        print("\nCity: "+ city + "\nTemperature: " + "{0:.2f}".format(celcius) + "\nFeels Like: "+ "{0:.2f}".format(feelsLike) + "\nStatus: "+ status+ "\nDescription: "+ description +"\nCountry: "+country+"\n")
