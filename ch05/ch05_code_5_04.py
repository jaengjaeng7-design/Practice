from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Title</title></head>
<body>
<p class="title"><b>The Title</b></p>
<a href="http://example.com/1" class="link">Link 1</a>
<a href="http://example.com/2" class="link">Link 2</a>
<a href="http://example.com/3" class="link">Link 3</a>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')
# 코드 5-4 find()의 예제. tag가 'a'인 첫번째 요소만 찾음
# Find the first 'a' tag
link = soup.find('a')

print(link.get('href')) # 출력: http://example.com/1