# your imports
...
from selenium import webdriver

site = 'http://heroimages.com/portfolio'
directory = "pixabay/" #Relative to script location

driver = webdriver.Chrome('/usr/local/bin/chromedriver')

driver.get(site)

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_tags = soup.find_all('img')

urls = [img['src'] for img in img_tags]

for url in urls:
    print(url)
    # your code
    ...