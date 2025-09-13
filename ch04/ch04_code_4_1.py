# 코드 4-1 Requests의 예제 코드
import requests

# 가져올 웹 페이지의 URL
url = "https://example.com"

# HTTP GET 요청을 보내고 응답받기
response = requests.get(url)

#응답이 성공적으로 왔는지 확인
if response.status_code == 200:
  # HTML 문서 내용 출력
  print(response.text)

else:
  print("웹 페이지를 불러오는데 실패했습니다.") 