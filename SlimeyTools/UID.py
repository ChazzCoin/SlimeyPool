from selenium import webdriver

# Create a new Chrome browser instance
browser = webdriver.Chrome()

# Navigate to the coinmarketcap.com website
browser.get('https://coinmarketcap.com/')

# Find the Bitcoin price element and get the text value
btc_price = browser.find_element_by_xpath('//*[@id="id-bitcoin"]/td[5]/a').text

print(f"Latest Bitcoin price: {btc_price}")

# Close the browser
browser.quit()