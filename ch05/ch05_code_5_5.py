# 코드 5-5 select()의 예제
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Title</title></head>
<body>
<p class="title"><b>The Title</b></p>
<div class="container">
 <a href="http://example.com/1" class="link">link 1</a>
 <a href="http://example.com/2" class="link">link 2</a>
 <a href="http://example.com/3" class="link">link 3</a>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# class가 "container"인 div 태그 안에 있는 모든 a 태그 선택
links = soup.select('div.container a')

for link in links:
    print(link.get('href'))