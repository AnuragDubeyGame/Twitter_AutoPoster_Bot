from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ROWS_TO_FETCH = 5500 # Just Enough for 1 years of tweet.

data_dictionary = {}
driver = webdriver.Chrome()
website_url = 'https://www.mentalfloss.com/amazingfactgenerator'
wait = WebDriverWait(driver, 1)

def scrape_website(url):
    driver.get(url);

    text_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, '_qsor55')))
    img_element = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mm-facts-widget-inner"]/article/div/div/figure/div/div')))
    image_html = img_element.get_attribute('innerHTML')

    split_text = image_html.split()
    src_item = next(item for item in split_text if item.startswith('src='))
    img_url = src_item.split('"')[1]

    return text_box.text, img_url
for i in range(ROWS_TO_FETCH):
    scraped_text, scraped_url = scrape_website(website_url)
    data_dictionary[scraped_text] = scraped_url

driver.quit()




