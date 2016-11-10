# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.

# Name: Yuxuan Chen

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os


# beautiful soup
url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
changedHTML = soup.prettify()


# swap out main picture
originalBigImg = 'https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg'
mainImg = 'https://thecubicle.us/images/banners/valkbanner2.jpg'
changedHTML = changedHTML.replace(originalBigImg, mainImg)

# change small logo pictures
img = os.path.abspath('media/logo.png')
changedHTML = re.sub(r'logo2.png', img, changedHTML);

# change student to AMAZING students
changedHTML = re.sub(r'( students*)', r' AMAZING \1', changedHTML)

# create html file
webpage = open('output.html', 'w')
webpage.write(changedHTML)


