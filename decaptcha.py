import requests
import base64
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def decap(driver):
    text = cap(driver)
    return text


def cap(driver):
    found = False
    while not found:
        refresh = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//tbody/tr[5]/td[2]/a[1]")))
        for i in range(3):
            time.sleep(0.3)
            refresh.click()
        time.sleep(4)
        captcha_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@id='captchaimg']")))
        # get the captcha as a base64 string
        img_captcha_base64 = driver.execute_async_script("""
        var ele = arguments[0], callback = arguments[1];
        ele.addEventListener('load', function fn(){
          ele.removeEventListener('load', fn, false);
          var cnv = document.createElement('canvas');
          cnv.width = this.width; cnv.height = this.height;
          cnv.getContext('2d').drawImage(this, 0, 0);
          callback(cnv.toDataURL('image/jpeg').substring(22));
        }, false);
        ele.dispatchEvent(new Event('load'));
        """, captcha_element)

        # save the captcha to a file
        with open(r"captcha.jpg", 'wb') as f:
            f.write(base64.b64decode(img_captcha_base64))
        # Upload grayscale captcha image to OCR.space API
        payload = {'isOverlayRequired': False,
                   'detectOrientation': True,
                   'scale': True,
                   'OCREngine': 2,
                   'apikey': 'K82339863688957',
                   'language': 'eng',
                   }

        files = {'file': ('captcha.jpg', open('captcha.jpg', 'rb'))}
        r = requests.post('https://api.ocr.space/parse/image',
                          data=payload, files=files)
        ocr_text = r.json()['ParsedResults'][0]['ParsedText']
        captcha_text = ''.join(filter(str.isdigit, ocr_text))
        if len(captcha_text) not in [3, 4]:
            found = False
        else:
            found = True
            print("captcha code is: "+captcha_text)
            return captcha_text
