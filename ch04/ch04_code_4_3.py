# 코드 4-3 Scrapy의 예제 코드
import scrapy

class exampleSpider(scrapy.Spider):
  name = "example" # 크롤러 이름
  start_urls = ['https://example.com'] # 시작할 URL 리스트

  def parse(self, response):
     # XPath를 사용해 <title> 태그의 텍스트 추출

    page_title = response.xpath('//title/text()').get()
    print("페이지 제목:", page_title)  # 콘솔에 직접 출력

    yield{'title': page_title} # 결과를 딕셔너리 형태로 반환