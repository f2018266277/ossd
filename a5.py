from selenium import webdriver
import requests

driver = webdriver.Firefox()
driver.maximize_window()

container = "mItv1"
image_class = "YVj9w"
nature = "https://unsplash.com/s/photos/nature"
beach = "https://unsplash.com/s/photos/beach"
animals = "https://unsplash.com/s/photos/animals"

def download(link, folder):
    global container, image_class, driver
    driver.get(link)
    images = driver.find_element_by_class_name(container).find_elements_by_class_name(image_class)
    for i in range(10):
        try:
            response = requests.get(images[i].get_attribute("src"))  
        except:
            print('Error')    
        else:
            if response.status_code == 200:
                with open(folder+"/image"+str(i+1)+".jpg", "wb") as f:
                    f.write(response.content)
        
download(nature, "nature")
download(beach, "beach")
download(animals, "animal")
