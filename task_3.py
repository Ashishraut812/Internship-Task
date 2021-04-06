# importing required package
from selenium import webdriver

# enter "path" of chrome driver in your pc.
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

# given list of websites.
s = ["https://cbdfx.com", "https://cbdmd.com", "https://premiumjane.com", "https://bluebirdbotanicals.com", "https://nuleafnaturals.com", "https://purekana.com", "https://joyorganics.com", "https://greenroads.com", "https://medterracbd.com", "https://justcbdstore.com", "https://www.thecbdistillery.com/", "https://cbdamericanshaman.com/", "https://www.corecbd.com/", "https://www.endoca.com/cbd-products/cbd-oil", "https://www.bluerivernutrition.com/", "https://www.cbdpure.com/", "https://fabcbd.com/", "https://royalcbd.com/", "https://miraflora.co/", "https://www.getsabaidee.com/"]

#     function declaration.


def fun1(s):
    s1 = []
    for i in s:
        driver.get(i)
        # implicitly_wait() is required to load all the elements in the webpage.
        driver.implicitly_wait(5)

        # try and except block is required, if some webpages didn't load correctly.
        try:
            if driver.find_element_by_link_text('FAQ'):
                s1.append(i)
            elif driver.find_element_by_link_text('blog' or 'blogs'):
                s1.append(i)
            else:
                pass
        except:
            pass
    # To close the tab.
    driver.quit()
    for k in s1:
        print(k)

    return


fun1(s)







