import requests

api_key = "4056aa4e8e76bc6c927eb9be8fe60567"
city_name = input('Enter the city name : ')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

response = requests.get(url)
print(response)

if response.status_code == 200:
    weather_data = response.json()
    city_temp = weather_data['main']['temp'] - 273.15
    print(f'{city_name} temperature is : {round(city_temp)}°C')
else:
    print(f'City Name {city_name} is Invalid or Incorrect')