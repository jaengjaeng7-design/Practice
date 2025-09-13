# 코드 5-9 click()의 예제
# 셀레니움을 사용해서 웹페이지에서 검색 버튼을 클릭하는 동작을 자동화하는 예제.

search_button = driver.find_element(By.NAME, "btnk")
#HTML에서 name="btnk"인 요소를 찾음. 구글 검색 버튼이 이 이름을 가지고 있는 경우가 많음.

search_button.click() #.click(): 해당 버튼을 클릭하는 동작을 수행.