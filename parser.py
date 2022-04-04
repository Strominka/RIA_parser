from msilib.schema import Class
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


url = 'https://ria.ru/politics/'


options = webdriver.ChromeOptions()
options.add_argument = ('user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.3')
options.add_argument = ('--disable-blink-features=AutomationControlled')
options.headless = True

s = Service(executable_path = 'C:\\Users\\Mikhail\\VS python\\Practica\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)

  
def get_sourse_html(url):
    try:
        driver.get(url=url)
        news_name = driver.find_elements(By.CLASS_NAME, 'list-item__title')
        news_time = driver.find_elements(By.CLASS_NAME, 'list-item__date')
        news_views = driver.find_element(By.CLASS_NAME, 'list-item__views-text')

        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def get_content(url):
    try:
        driver.get(url = url)
        news_text = driver.find_elements(By.CLASS_NAME, 'article__text')
        news_emotions = driver.find_elements(By.CLASS_NAME, 'm-value')
        news_button = driver.find_element(By.CLASS_NAME, 'form__btn')

        for emotions in news_emotions:
            print(emotions.text)
            
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()   

def main():
    #get_sourse_html(url)
    get_content(url = 'https://ria.ru/20220330/referendum-1780974627.html')


if __name__ == '__main__':
    main()
    
