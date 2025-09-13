# 코드 4-2 Beautifulsoup의 예제 코드
import requests
from bs4 import BeautifulSoup

# 가져올 웹 페이지의 URL
url = "https://example.com"

#웹 페이지 요청 및 HTML 가져오기
response = requests.get(url)

# 응답이 성공했는지 확인
if response.status_code == 200:
  # HTML 파싱
  soup = BeautifulSoup(response.text, 'html.parser')

  # <tittle> 태그 찾기
  title_tag =soup.title

  # <title> 태그의 텍스트 출력
  print("페이지 제목:", title_tag.string)

else:
  print("웹 페이지를 불러오는데 실패했습니다.")