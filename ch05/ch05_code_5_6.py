from bs4 import BeautifulSoup

#코드 5-6 get_text()의 예제
# tag가 "a"인 첫번째 문장을 찾아서 해당 text를 출력

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

# tag가 "a"인 첫번째 문장을 찾아서 해당 text 출력
link = soup.find('a')

print(link.get_text())   # 출력: 예제 링크
