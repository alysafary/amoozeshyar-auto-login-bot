from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def changeTerm(driver):
    choose = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@href='javascript: void(); return false;']")))
    choose.click()
    select = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "parameter(wsTermRef)")))
    select.click()
    option = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//option[@value='6143046807']")))
    option.click()
    button = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@id='saveWorkspace']")))
    button.click()

    return driver


def program(driver):
    frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//iframe[@id='menuFrame']")))
    driver.switch_to.frame(frame)
    time.sleep(1)
    bt = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mi_1_3']")))
    driver.execute_script("arguments[0].click();", bt)
    driver.switch_to.default_content()
    s = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//button[@id='_3_31']")))
    s.click()
    return driver


def selectUnit(driver):
    frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//iframe[@id='menuFrame']")))
    driver.switch_to.frame(frame)
    bt = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mi_1_0']")))
    driver.execute_script("arguments[0].click();", bt)
    driver.switch_to.default_content()


def transcript(driver):
    frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//iframe[@id='menuFrame']")))
    driver.switch_to.frame(frame)
    bt = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mi_1_7']")))
    driver.execute_script("arguments[0].click();", bt)
    driver.switch_to.default_content()


def payment(driver):
    frame = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//iframe[@id='menuFrame']")))
    driver.switch_to.frame(frame)
    bt = WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.XPATH, "//a[@id='mi_1_5']")))
    driver.execute_script("arguments[0].click();", bt)
    driver.switch_to.default_content()
    s = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//tbody/tr[1]/td[4]/form[1]/span[1]/input[1]")))
    s.click()
