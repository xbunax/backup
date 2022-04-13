from selenium import webdriver
import time
import os
def dianji(a):
    return driver.find_element_by_xpath(a).click()
driver=webdriver.Chrome('/Users/xbunax/Downloads/chromedriver-4')
url='https://auth.suda.edu.cn/cas/login?service=https%3A%2F%2Fauth.suda.edu.cn%2Fsso%2Flogin%3Fredirect_uri%3Dhttps%253A%252F%252Fauth.suda.edu.cn%252Fsso%252Foauth2%252Fauthorize%253Fscope%253Dopenid%252520profile%2526response_type%253Dcode%2526redirect_uri%253Dhttps%25253A%25252F%25252Fauth.suda.edu.cn%25252Fmiddleware%25252FgetProfile%25253Fapp%25253Dmy%252526welcome%25253D%252525E4%252525BF%252525A1%252525E6%25252581%252525AF%252525E9%25252597%252525A8%252525E6%25252588%252525B7%252526x_app_url%25253Dhttp%25253A%25252F%25252Faff.suda.edu.cn%25252F_web%25252Fucenter%25252Flogin.jsp%252526jumpto%25253Dhttp%25253A%25252F%25252Fmy.suda.edu.cn%25252Fportal%25252Flogin.jsp%25253FreturnUrl%25253Dhttp%2525253A%2525252F%2525252Fmy.suda.edu.cn%2525252Fportal%2526client_id%253DRROw9GYmIQzXK6KtTyvv%2526state%253D123%26x_client%3Dcas'
driver.get(url)
username=driver.find_element_by_xpath('//*[@id="username"]')
passport=driver.find_element_by_xpath('//*[@id="password"]')
login2=driver.find_element_by_xpath('//*[@id="fm1"]/div[7]/button')
username.send_keys('')#学号
passport.send_keys('')#密码
login2.click()
driver.implicitly_wait(5)
try:
    daka=driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div/div/div/div/div/div[2]/div/div/ul/li[2]/div/div/div[1]')
    daka.click()
    a = driver.window_handles
    driver.switch_to.window(a[1])
except:
    driver.refresh()
    daka=driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div/div/div/div/div/div[2]/div/div/ul/li[2]/div/div/div[1]')
    daka.click()

driver.implicitly_wait(10)
a=driver.window_handles
driver.switch_to.window(a[1])
mt=driver.find_element_by_xpath('//*[@id="input_swtw"]')
at=driver.find_element_by_xpath('//*[@id="input_xwtw"]')
mt.send_keys('36.5')
at.send_keys('36.5')
driver.find_element_by_xpath('//*[@id="checkbox_jkzk33"]/div/ins').click()
driver.find_element_by_xpath('//*[@id="select2-select_xrywz-container"]').click()
driver.find_element_by_xpath('/html/body/span/span/span[2]/ul/li/ul/li[4]').click()#所在地点
driver.find_element_by_xpath('//*[@id="input_jtdz"]').send_keys('')#具体地址
driver.find_element_by_xpath('//*[@id="radio_sfyxglz7"]/div/ins').click()
dianji('//*[@id="radio_sfywc11"]/div/ins')
dianji('//*[@id="radio_sfygrzjcg15"]/div/ins')
dianji('//*[@id="radio_sfyxcgjjc19"]/div/ins')
dianji('//*[@id="radio_sfyzgfxljs23"]/div/ins')
dianji('//*[@id="radio_sfyzgfxryjc27"]/div/ins')
dianji('//*[@id="tpost"]')
time.sleep(5)
driver.close()

