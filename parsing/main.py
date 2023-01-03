from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#Supply Chain Dynamics

#options
options=webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36")
driver=webdriver.Chrome(options=options)

try:
    driver.get("https://authn.edx.org/login")
    time.sleep(2)

    #email_input=driver.find_element(by=By.CLASS_NAME,value="form-control").find_element(by=By.ID,value="emailOrUsername")
    email_input=driver.find_element_by_id("emailOrUsername")
    email_input.clear()
    email_input.send_keys("ksu.mystery@gmail.com")
    time.sleep(1)

    #password_input = driver.find_element(by=By.CLASS_NAME, value="form-control").find_element(by=By.ID,value="password")
    password_input=driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys("Severstal2021")
    time.sleep(2)

    login_button=driver.find_element_by_id("sign-in").click()
    #login_button = driver.find_element(by=By.CLASS_NAME, value="login-button-width").find_element(by=By.ID,value="sign-in").click()
    time.sleep(15)

    #Dynamics_link=driver.find_element_by_link_text("Supply Chain Dynamics").click()
    #time.sleep(150)

    #Week 8: Global Supply Chain Management II
    #Dynamics_link = driver.find_element(by=By.CLASS_NAME,value="tomatoes").click()
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
