#코드 4-4 Selenium의 예제 코드
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#크롬 드라이버 경로 설정(ChromeDriver가 설치된 경로로 수정 필요)
# CHROME_PATH = "C:\tools\chromedriver\chromedriver.exe"

# chrome_service = Service(executable_path=CHROME_PATH)

#웹 브라우저 실행
# driver = webdriver.Chrome(service=chrome_service)
driver = webdriver.Chrome()


#웹 페이지 열기
# driver.get("https://example.com")


# 1번
driver.get("https://www.naver.com") 
# 잠시 대기 (페이지 로딩 대기용)
time.sleep(2)

# <title> 태그 가져오기
extract_title = driver.title
print("페이지 제목:", extract_title)



#웹 브라우저 닫기
driver.quit()



# 2번
github_address = "https://github.com/jaengjaeng7-design/Practice/blob/main/ch05/ch05_code_5_6.py"
driver1 = webdriver.Chrome()
driver1.get(github_address)



extract_github_address_title = driver1.title
print("페이지 제목:", extract_github_address_title)


#웹 브라우저 닫기
driver1.quit()


print(extract_github_address_title)
