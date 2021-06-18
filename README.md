# Capture All Google Images

Install selenium-python and chrome/firefox/IE driver before executing this code. Replace the location of my chrome driver by the location of your driver.

Edit the folder location in the code to the location of your choice in which you want to save all the images.

Run the code. The program will ask you for your input.

Enter a keyword/phrase for which you want the images. Press Enter.

The program uses Selenium-Python to automatically take screenshots of all images available on a certain keyword/phrase in the google image search result. 
After capturing the images on the search result, it will automatically click on the first filter and capture all images in it. Then it will unselect the 1st filter and select the 2nd filter to do the same job until all filters are done executing. 

The image names will follow this syntax:  
   If the images are captured from the normal search results: {Keyword you searched for}({image number})
      
   If the images are captured after a filter is selected: {Keyword you searched for} - {selected filter}({image number})
