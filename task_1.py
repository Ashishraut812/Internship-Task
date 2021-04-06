from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui

s = []


def chck(s):
    for i in s:
        if 'blog' in i:
            s.remove(i)
        elif 'article' in i:
            s.remove(i)
        else:
            pass
    return s


# enter path of chrome driver in your pc.
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")

driver.find_element_by_name('q').send_keys("buy cbd products")

pyautogui.press("Enter")

for a in driver.find_elements_by_partial_link_text('CBD'):
    s.append(a.get_attribute('href'))

# chck() function to check if it is a shopping site or not.
chck(s)

for i in s:
    print(i)


driver.quit()