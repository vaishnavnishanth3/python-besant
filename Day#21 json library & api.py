print("")
#api
#JSON --> JavaScript Object Notation
#'http://api.openweathermap.org/data/2.5/weather?qq=(CITY_NAME)&appid=(API_KEY)&units=metric'
#weather:
print("Weather:")
import json
url='{"Chennai":"90","Madurai":"65","Trichy":"50"}'
x=json.loads(url)
print(x)
print(type(x))
print("")

#database
print("From Database:")
url1='{"firstname":"Arun","Lastname":"Kumar","Age":"25"}'
y=json.loads(url1)
print(y)
print(type(y))
print("")