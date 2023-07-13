from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def scrape_website(url):
    driver.get(url)
    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.CLASS_NAME, value="_qsor55")
    
    imgResult = driver.find_element(By.XPATH,'//*[@id="mm-facts-widget-inner"]/article/div/div/figure/div/div')
    image_url = imgResult.get_attribute('innerHTML')

    split_text = image_url.split()
    src_item = next(item for item in split_text if item.startswith('src='))
    imgUrl = src_item.split('"')[1]

    return text_box.text, imgUrl

website_url = 'https://www.mentalfloss.com/amazingfactgenerator'  
scraped_text, scraped_url = scrape_website(website_url)

data_dictionary = {
    scraped_text: scraped_url
}

print(data_dictionary)
driver.quit()
