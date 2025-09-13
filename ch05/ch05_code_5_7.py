# 코드5-7 get()의 예제
# find ('a')의 결과에서 href와 class의 속성 찾기
link = soup.find('a')

print(link.get('href'))  # 하이퍼링크의 목적지
print(link.get('class'))  # 스타일이나 그룹 지정