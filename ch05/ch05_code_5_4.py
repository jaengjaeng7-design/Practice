# 코드 5-4 find()의 예제. tag가 'a'인 첫번째 요소만 찾음
# Find the first 'a' tag
link = soup.find('a')

print(link.get('href')) # 출력: http://example.com/1