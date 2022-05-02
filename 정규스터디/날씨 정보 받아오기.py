import requests
import json
#javascript object notation: 자바스크립트 중 오브젝트 객체의 문법을 따르는 것. 데이터를 주고 받을 때 사용.
city = "Seoul"
apikey = "1abc8c35045e1da154011432f49aa856"
lang = "kr"
api = f"http://api.openweathermap.org/
data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"
#물음표 뒤는 파라미터. 함수의 재료. &로 연결. 온도 단위를 화씨에서 섭씨로 바꿀 때 unit 파라미터 사용 가능.

result = requests.get(api)
#print(result.text) #.text를 넣어야 오류가 뜨지 않음.

#print(type(result.text)) #타입을 알게하는 함수

data = json.loads(result.text)
#문자열을 json 타임으로 변경

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["descriptioin"],"입니다.")
#"weather"이라는 키값 안에 딕셔너리 0번째, 그 중 main이라는 키값.
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")data[weather{}]
