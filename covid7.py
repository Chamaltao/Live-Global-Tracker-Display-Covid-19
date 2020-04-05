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
      import requests

      api_response = requests.get('https://thevirustracker.com/free-api?global=stats', headers={"User-Agent": "Chrome"})
      time.sleep(2)

      apiSL_response = requests.get('https://thevirustracker.com/free-api?countryTotal=LK', headers={"User-Agent": "Chrome"})
      time.sleep(2)


      if api_response.status_code == 200:

            covid_U = api_response.json()['results']
            for count in range(0,5):

                confirmed=str(covid_U[0]["total_cases"])
                lcd.clear()
                lcd.write_string('Total Confirmed')
                lcd.crlf()
                lcd.write_string(confirmed)
                time.sleep(3)

                deaths=str(covid_U[0]["total_deaths"])
                lcd.clear()
                lcd.write_string('Total Deaths')
                lcd.crlf()
                lcd.write_string(deaths)
                time.sleep(3)

            lcd.clear()
            lcd.write_string("Covid-19")
            lcd.crlf()
            lcd.write_string("SRI LANKA")
            time.sleep(2)

      elif api_response.status_code == 404:
            lcd.clear()
            lcd.write_string("Conection fail")
      if apiSL_response.status_code == 200:

            covid_SL = apiSL_response.json()['countrydata']
            for count in range(0,5):

                confirmed=str(covid_SL[0]["total_cases"])
                lcd.clear()
                lcd.write_string('SL Confirmed')
                lcd.crlf()
                lcd.write_string(confirmed)
                time.sleep(3)

                deaths=str(covid_SL[0]["total_deaths"])
                lcd.clear()
                lcd.write_string('SL  Deaths')
                lcd.crlf()
                lcd.write_string(deaths)
                time.sleep(3)

                deaths=str(covid_SL[0]["total_new_cases_today"])
                lcd.clear()
                lcd.write_string('SL  New  Cases')
                lcd.crlf()
                lcd.write_string(deaths)
                time.sleep(3)



      elif apiSL_response.status_code == 404:
            lcd.clear()
            lcd.write_string("Conection fail")

      lcd.clear()
      lcd.write_string("Covid-19")
      lcd.crlf()
      lcd.write_string("Global Tracker")
      time.sleep(30)
