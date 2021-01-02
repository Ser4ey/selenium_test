from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from time import sleep

opt = FirefoxOptions()
opt.add_argument('--headless')

web = webdriver.Firefox(executable_path='/home/ubuntu/bots_Telegram/Test_Firefox/geckodriver', firefox_options=opt)
web.get('https://stackoverflow.com/questions/46809135/webdriver-exceptionprocess-unexpectedly-closed-with-status-1')

print('ok1')
sleep(10)

print('ok2')

web.save_screenshot('1.png')
web.get('https://www.instagram.com/')
sleep(10)
web.save_screenshot('2.png')

print('ok3')
web.quit()
print('ok4')
