import requests
import json
from datetime import date
from datetime import timedelta
import time


pincode_list = [638112,638053,638051]
call_success = 0
for time1 in range(15000):
        for pin_code in pincode_list:

                for i in range(30):

                        #response=requests.post('https://e76fd430de7c8144ed4d0041e124601a622c48b952b5cccf:281207b256bb4a8db953d2709f80a05fba169df9550b77ee@api.exotel.com/v1/Accounts/ghhhhh1/Calls/connect', data=data)

                        #print (response.text)

                        #URL="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=638112&date=31-05-2021"

                        date = date.today()
                        date += timedelta(days=i)
                        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=" + str(pin_code) +"&date=" + date.strftime('%d-%m-%Y')


                        # api-endpoint
                        #URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=563&date=31-05-2021"


                        # defining a params dict for the parameters to be sent to the API
                        #PARAMS = {'district_id': 563, 'date': '22-05-2021' }
                        HEADERS = {'Accept': 'application/json',
                                   'Accept-Language': 'en-GB',
                                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0' }

                        # sending get request and saving the response as response object
                        #r = requests.get(url=URL,params=PARAMS ,headers=HEADERS)
                        r = requests.get(url=URL ,headers=HEADERS)
                        # extracting data in json format
                        if  r.status_code == 200:
                                data = r.json()
                                centres= json.dumps(data)
                                #print(data['centers'][0]['name'],data['centers'][0]['fee_type'],data['centers'][0]['district_name'],
                                #      data['centers'][0]['sessions'][0]['available_capacity_dose1'],data['centers'][0]['sessions'][0]['vaccine'],
                                #      data['centers'][0]['sessions'][0]['available_capacity'], data['centers'][0]['sessions'][0]['min_age_limit'])

                                #['date'],data['centers'][0]['sessions']['vaccine'],data['centers'][0]['sessions']['available_capacity_dose1'])

                                length = len(data['centers'])

                                for i in range(length):
        #                              if data['centers'][i]['pincode'] == pin_code:
        #                                  print(data['centers'][i]['name'],data['centers'][i]['pincode'], data['centers'][i]['fee_type'], data['centers'][i]['district_name'],
        #                                      data['centers'][i]['sessions'][0]['available_capacity_dose1'], data['centers'][i]['sessions'][0]['vaccine'],
        #                                      data['centers'][i]['sessions'][0]['available_capacity'],data['centers'][i]['sessions'][0]['min_age_limit'] ,data['centers'][i]['sessions'][0]['date'])
                                      if  data['centers'][i]['sessions'][0]['available_capacity_dose1'] > 2:
                                          print ("available in",data['centers'][i]['name'], "dosetype",data['centers'][i]['sessions'][0]['vaccine'], "number of doses1", data['centers'][i]['sessions'][0]['available_capacity_dose1'] )
                                          data = {
                                              'From': '077xxxxxxxxx',
                                              'To': '077xxxxxxxxx',
                                              'CallerId': '04440115132'
                                          }
                                          response = requests.post(
                                              'https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@api.exotel.com/v1/Accounts/ghhhhh1/Calls/connect',
                                              data=data)
                                          call_success = response.status_code
                                          print (response.text)
                        elif  r.status_code == 429:
                                print("Handling 429 will retry with 5 mins back off")
                        else:
                            print("The Covid vaccine status server seem to be unresponsive. Error code:",r.status_code)

                        if call_success == 200:
                            break
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(300)
