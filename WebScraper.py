from selenium import webdriver
import json

data = {}
data[''] = []
browser = webdriver.Chrome(executable_path=r'CHROME_DRIVER_LOCATION')
browser.get('URL')

for i in browser.find_elements_by_xpath('//a[@class="shelfProductTile-descriptionLink"]'):
    try:

        print(i.get_attribute("href"))
        browser2 = webdriver.Chrome(executable_path=r'CHROME_DRIVER_LOCATION')
        browser2.get(i.get_attribute("href"))

        name = browser2.find_element_by_xpath('//div[@class="productDetail-tile"]/h1')
        barcode = browser2.find_element_by_xpath('//div[@class="productDetail"]/meta[3]')
        price = browser2.find_element_by_xpath('//div[@class="productDetail-price"]/meta[2]')
        print(name.text)
        print(barcode.get_attribute("content"))
        print(price.get_attribute("content"))

        data[''].append({'id': barcode.get_attribute("content"), 'commercialName': name.text, 'price': price.get_attribute("content")})
        browser2.close()

    except:
        continue

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
