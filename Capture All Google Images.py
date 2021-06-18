"""
This program takes your search query as the input and then it searches for it on google images.
It will scroll to the bottom of the search results and then will start to capture the images from image 1 displayed on the search results. You can specify the number of images you want to capture from the search result.
After capturing the no. of specified images, it will click on the first filter (displayed by google on the top of the search results), it will repeat the same process.
Then, it will unselect the selected filter and click on the next filter to repeat the same process.
This process will continue until the program finishes capturing the images from all the no. of filters you specified to capture from.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

query = input("Enter your search query: ")  # What you enter here will be searched for in Google images

# NOTE: Enter the location of your own driver
driver = webdriver.Chrome('C:/Users/Urvish/WebDrivers/chromedriver_win32 - Chrome 91/chromedriver.exe')

driver.maximize_window()

driver.get('https://images.google.com/')

box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')

box.send_keys(query)    # Type the search query in the search box
box.send_keys(Keys.ENTER)   # Pressing enter



# Keep scrolling down the webpage until it cannot scroll no more
def scroll_to_bottom():
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_css_selector(".YstHxe input").click()    # These element paths might change in the future. 
            time.sleep(3)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height

scroll_to_bottom()


for i in range(1, 901):     # 901 is a hard coded value. I found out that there are maximum 900 images(generally) in a google image search result. Feel free to change the value if you want to capture less or more images.
    try:
        driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot('D:/HYS/Images/'+ query + ' (' +str(i)+ ').png')
        time.sleep(0.1)
    except:
        pass


# Looping through the related searches (or "so called" filters) offered by google
error_counter1 = 0
error_counter2 = 0
loop_count = 0      # Just to see the progress of the program (as the program can run for a very long time)

for j in range(1, 31):  # 31 is a hard coded value. Google shows a max of 30 filters in its image search result
    time.sleep(5)
    try:
        related = driver.find_element_by_xpath('//*[@id="i6"]/div[1]/span/span/div['+str(j)+']/a')

        filter_name = related.text     
        # print(filter_name)

        time.sleep(2)

        related.send_keys(Keys.ENTER)   # clicking on the filter

        scroll_to_bottom()

        for i in range(1, 901):     # 901 is a hard coded value. I found out that there are maximum 900 images(generally) in a google image search result

            image_location = f"D:/HYS/Images/{query} - {filter_name}({str(i)}).png"     
            # NOTE: Replace D:/HYS/Images/  by the path of your choice

            try:
                driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(image_location)

            except:
                error_counter1 += 1
                # print('   Minor Error-->', error_counter1)   # This error means an image was not saved.
                # NOTE: This error can also arrive if the range of the inner loop is greater than the total no. of images displayed by google in the search result.
        
        # Unclicking the selected related search
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="i6"]/div[1]/span/span[1]/div/a').send_keys(Keys.ENTER)

        # print("j--> ", j)

    except:
        error_counter2 += 1
        # print('BIGGER Error-->', error_counter2)    # This error means the loop didn't execute as planned
        # NOTE: This error can also occur if the no. of recommended filters displayed by google are less than the range of the outer loop.

    loop_count += 1
    # print('Loop Count ==>', loop_count)

# print("No. of minor errors:", error_counter1)
driver.close()

