from selenium import webdriver
import time





try:
    ''' options '''
    driver = webdriver.Chrome()
    driver.get("https://www.avito.ru/")
    title = driver.title
    time.sleep(4)
    search_box = driver.find_element(by=By.NAME, value="Электроника")
    search_button = driver.find_element(by=By.NAME, value="Найти")
    # search_box.send_keys("Selenium")
    search_button.click()
    # value = search_box.get_attribute("value")
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()