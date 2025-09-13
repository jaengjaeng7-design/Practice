# 코드 5-10 send_key()의 예제
search_box =driver.find_element(By.NAME, "q")
# ㄴHTML에서 name="q"인 요소를 찾음. 구글 검색창이 보통 이 이름을 가지고 있음.

search_box.send_keys("Selenium")  # - 해당 입력창에 "Selenium"이라는 텍스트를 자동으로 입력.
search_button.click() #.click(): 해당 버튼을 클릭하는 동작을 수행.