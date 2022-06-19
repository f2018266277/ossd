from selenium import webdriver  
import time

def send_keys(id, key):
    global driver
    driver.find_element_by_id(id).send_keys(key)

def click(id):
    global driver
    driver.find_element_by_id(id).click()

# driver = webdriver.Chrome()  
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://lms.umt.edu.pk/login/index.php")
send_keys("username", "F2018266277")
send_keys("password", "eMZDe5@e")
click("loginbtn")
navbar = driver.find_element_by_id("nav-drawer").find_elements_by_tag_name("a")
for links in navbar:
    print(links.text)