# 코드 5-8 find_element()의 예제
# Selenium을 사용할 때 웹 페이지에서 특정 요소를 찾는 다양한 방법을 보여주는 예제
# 각각의 find_element() 방식은 HTML 요소를 어떤 기준으로 찾을지를 지정함

diver.find_element(By.CLASS_NAME, "") #클래스 이름으로 요소 찾기
diver.find_element(By.ID, "") #고유한 ID 값으로 요소 찾기
diver.find_element(By.CSS_SELECTOR, "") #CSS 선택자 방식으로 찾기
diver.find_element(By.NAME, "") #name 속성으로 요소 찾기
diver.find_element(By.TAG_NAME, "") #태그 이름으로 요소 찾기
diver.find_element(By.XPATH, "") #XPath 경로로 요소 찾기
diver.find_element(By.Link_TEXT, "") #링크 텍스트 전체로 찾기
diver.find_element(By.PARTIAL_LINK_TEXT, "") #링크 텍스트 일부로 찾기

diver.find_element(By.ID, "login-btn") #로그인 버튼을 찾고 싶을때
diver.find_element(By.CLASS_NAME, "nav-link") #특정 클래스의 링크를 찾고 싶다면