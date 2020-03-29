import time
import requests
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD
lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
              numbering_mode=GPIO.BOARD)
lcd.clear()
lcd.write_string("Covid-19")
lcd.crlf()
lcd.write_string("Global  Tracker")
while(True):
      response = requests.get('https://covid19api.herokuapp.com/latest')
      
      if response.status_code == 200:
            print(response.json())
            for count in range(0,10):
            
                confirmed=str((response.json()['confirmed']))
                lcd.clear()
                lcd.write_string('Total Confirmed')
                lcd.crlf()
                lcd.write_string(confirmed)
                time.sleep(2)


                recovered=str((response.json()['recovered']))
                lcd.clear()
                lcd.write_string('Total Recovered')
                lcd.crlf()
                lcd.write_string(recovered)
                time.sleep(2)
                
                deaths=str((response.json()['deaths']))
                lcd.clear()
                lcd.write_string('Total Deaths')
                lcd.crlf()
                lcd.write_string(deaths)
                time.sleep(2)

            lcd.clear()
            lcd.write_string("Covid-19")
            lcd.crlf()
            lcd.write_string("Global Tracker")
      elif response.status_code == 404:
            print('Not Found')
      
      time.sleep(60)
