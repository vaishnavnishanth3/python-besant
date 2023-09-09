import requests

api_key = input("Enter the Api-Key: ")
city = input("Enter your city: ")
country_code = input("Enter your country code: ")

url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']

    print(f'Weather in {city}, {country_code}:')
    print(f'Description: {weather_description}')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')

else:
    print(f'Error: Unable to fetch weather data. Status code: {response.status_code}')
