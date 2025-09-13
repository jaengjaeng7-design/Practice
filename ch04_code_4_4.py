#코드 4-4 Selenium의 예제 코드
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 경로 설정(ChromeDriver가 설치된 경로로 수정 필요)
chrome_service = Service(executable_path="path/to/chromedriver")

#웹 브라우저 실행
driver = webdriver.Chrome(service=chrome_service)

#웹 페이지 열기
driver.get("https://example.com")

# 잠시 대기 (페이지 로딩 대기용)
time.sleep(2)

# <title> 태그 가져오기
title = driver.title
print("페이지 제목:", title)

#웹 브라우저 닫기
driver.quit()

