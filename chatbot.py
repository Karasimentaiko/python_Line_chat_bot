#PYxVsrNIJXK4eyngXvTWyByUozWB612cV0O78AuIbJE
import requests
import datetime
import pytz

time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time = time.strftime('%Y年%m月%d日 %H:%M:%S')

TOKEN = 'PYxVsrNIJXK4eyngXvTWyByUozWB612cV0O78AuIbJE'

api_url = 'https://notify-api.line.me/api/notify'

send_contents = time

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

image_file = './images/Sakize.jpeg'
binary = open(image_file, mode='rb')

image_dic = {'imageFile': binary}



requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
