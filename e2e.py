from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_scores_service(URL):
    web_driver = webdriver.Chrome(service=Service('chromedriver.exe'))
    web_driver.get(URL)
    score = web_driver.find_element(By.XPATH, '//*[@id="score"]').text
    web_driver.quit()
    if 0 < int(score) < 1001:
        return True
    else:
        return False


def main_function(URL):
    if test_scores_service(URL):
        print("The score is good")
        return 0
    else:
        print("The score is bad")
        return -1