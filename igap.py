from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def gap(driver):
    code = code_reader(driver)
    return code


# Define the iGap function
def code_reader(driver):
    found = False
    while not found:
        driver.switch_to.window(driver.window_handles[0])  
        time.sleep(1)
        driver.refresh()
        driver.get('https://web.igap.net/app?q=@amoozeshbot')

        # wait for the page to load and get the latest message
        latest_message = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "position-relative")))
        latest_message_text = latest_message.text

        # extract the numerical code from the latest message text
        pattern = r"رمز ورود: (\d+)"
        match = re.search(pattern, latest_message_text)
        if match:
            found = True
            code = match.group(1)
            print("The numerical code is:", code+"\n")
            return code
        else:
            found = False
            print("No numerical code found in the latest message")

