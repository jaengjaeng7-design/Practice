# 코드 5-3 find_all()의 예제. tag가 'a'인 요소를 전부 찾음
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

# Find all 'a' tags
links = soup.find_all('a')

for link in links:
  print(link.get('href'))