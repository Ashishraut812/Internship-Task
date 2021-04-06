from selenium import webdriver
import time

driver = webdriver.Chrome (executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.maximize_window()

driver.get("https://docplus.online/")

# identify elements with tag-name <a>
lnks = driver.find_elements_by_tag_name("a")

links = set()
# traverse list
for lnk in lnks:
    # get_attribute() to get all href
    links.add(lnk.get_attribute('href'))

links.remove(None)





for i in links:
    driver.get("https://www.site24x7.com/check-website-availability.html")
    s_k = driver.find_element_by_name('url')
    s_k.clear()
    s_k.send_keys(i)
    driver.find_element_by_xpath('//*[@id="cmdbtn"]').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="id_cws"]/a').click()
    driver.implicitly_wait(5)
    try:
        if driver.find_element_by_name('Host Unavailable'):






driver.quit()