# 코드 5-2 prettify()의 예제
from bs4 import BeautifulSoup

html_doc = "<html><head><title>The Tittle</title></head><body><h1>The Heading</h1><p>The paragraph.</p></body></html>"
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())