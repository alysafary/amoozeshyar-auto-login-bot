
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from decaptcha import decap
import time

USERNAME = "Username"
PASSWORD = "Password"

def login():
    chrome_driver = "C:\chromedriver.exe"
    service = ChromeService(executable_path=chrome_driver)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # navigate to the login page
    driver.execute_script(
        "window.open('https://stdn.iau.ir/Student/Pages/acmstd/loginPage.jsp')")
    driver.switch_to.window(driver.window_handles[-1])
    original_window = driver.current_window_handle
    driver.switch_to.window(original_window)

    try:
        logout_link = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='خروج']")))
        logged_in = True
        print("Already Logged In\n")
    except:

        go_next = False
        while go_next == False:
            try:
                code_input = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.NAME, "OTP")))
                logged_in = False
                go_next = True

            except:
                try:
                    error_button = WebDriverWait(driver, 2).until(
                        EC.presence_of_element_located((By.XPATH, "//span[@id='dialog34_title']")))
                    print("CaptchaCode was wrong\n")
                    driver.get(
                        'https://stdn.iau.ir/Student/Pages/acmstd/loginPage.jsp')

                except:
                    print("LogIn is in progress...\n")
                    username_field = WebDriverWait(driver, 7).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='user']")))
                    username_field.send_keys(USERNAME)

                    password_field = WebDriverWait(driver, 7).until(
                        EC.presence_of_element_located((By.XPATH, "//input[@id='pass']")))
                    password_field.send_keys(PASSWORD)
                    time.sleep(2)
                    captcha_field = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//tbody/tr[3]/td[1]/input[1]")))
                    text = decap(driver)
                    captcha_field.send_keys(text)
                    login_button = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.NAME, "B1")))
                    login_button.click()
                    logged_in = False
    return driver, logged_in
