import subprocess
from menu import menu
from login import *
from igap import gap


def main():
    command = "chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\selenum\ChromeProfile"
    p = subprocess.Popen(command)
    # call the login function
    driver, logged_in = login()
    if not logged_in:
        # handle two-factor authentication
        while not logged_in:
            code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "OTP")))
            code = gap(driver)
            driver.switch_to.window(driver.window_handles[-1])
            code_input.send_keys(code)
            submit_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "B1")))
            submit_button.click()
            try:
                error_message = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "//th[@style='text-align: right; color: red;']")))
                print("Invalid code entered\n")
            except:
                logged_in = True
                print("###### LoggedIn successfully ######\n")
    menu(driver)

if __name__ == '__main__':
    main()
