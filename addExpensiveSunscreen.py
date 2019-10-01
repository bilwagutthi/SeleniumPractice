"""
Find the most expensive sunscreen and add it to the cart.

SCOPE:
1) Launch Firefox Driver
2) Navigate to Max sunscreen
3) Add that sunscreen to the cart
4) Open the cart
5) Check if correct sunscreen is adder
6) Close the browser

Author : Bilwa Gutthi
"""

from selenium import webdriver
import time

# Creating an instence of thw web browser and navigating to the Shopping page
browser = webdriver.Firefox()
browser.get('https://weathershopper.pythonanywhere.com/sunscreen')

# Checking if the right web page has been loaded
if browser.title!="The best moisturizers in the world!":
    print("Error in loading page")
    browser.close()
    exit()
else:
    print("Page loaded")

# Creating a list with prizes of all sunscreens
sunscreens_prices=list()
prices=browser.find_elements_by_xpath('//div[@class="text-center col-4"]//descendant::p[contains(text(),"Price")]')
for i in prices:
    price=int(i.text.strip("Price: Rs. "))
    sunscreens_prices.append(price)
print("The prizes of the sunscreen are ",sunscreens_prices)

# Finding the sunscreen with max prize
max_prize=max(sunscreens_prices)
print("The maximum prize is",max_prize)

# Adding to cart sunscreen with max prize
add_button=browser.find_element_by_xpath('//div[@class="text-center col-4"]//descendant::button[contains(@onclick,{})]'.format(max_prize))
add_button.click()

# Clicking on cart button to check if the correct sunscreen is selected
cart_button=browser.find_element_by_xpath('//button[@class="thin-text nav-link"]')
cart_button.click()

time.sleep(3)

# Cheacking if the final prize is correct
try:
    final_prize=int(browser.find_element_by_xpath('//div[@class="row justify-content-center top-space-50"]//td[2]').text)
    print("Prize in cart is ",final_prize)
    if final_prize==max_prize:
        print("Success")
    else:
        print("Fail")
except Exception as e:
    print(e)
browser.close()