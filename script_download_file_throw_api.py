import requests
import os


url = 'https://www.selenium.dev/images/selenium_logo_square_green.png'

response = requests.get(url)  #сохраним ответ, который будет созранен в респонсе

f = open('selenium_logo_square_green.png', 'wb').write(response.content)

selenium_png  = open ("selenium_logo_square_green.png", 'rb').read()

print(selenium_png)

print(len(selenium_png))

#f = ["true" if  len(selenium_png)==30803 else "false"]
#print(f)



with open("selenium_logo_square_green_API.png", 'wb') as file:
    file.write(response.content)

with open("selenium_logo_square_green_API.png", "rb") as file:
    selenium_png=file.read()
    print(len(selenium_png))
    assert len(selenium_png)==30803


print(os.path.getsize('selenium_logo_square_green.png'))
