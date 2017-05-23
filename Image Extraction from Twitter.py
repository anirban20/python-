## This is a code to extract images from Twitter using BeautifulSoup

import urllib
from bs4 import BeautifulSoup
import numpy as np
from nltk import sent_tokenize, word_tokenize, pos_tag
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg

url="http://www.twitter.com"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html)
imgs = soup.findAll("img",{"alt":True, "src":True})

### ALL IMAGE LINKS IN THE PAGE

for img in imgs:
    print(img["src"])

k=[]
for img in imgs:
    img_url=img["src"]
    filename = os.path.join('/Volumes/16 DOS/Temp', 
                            img_url.split("/")[-1])
    urllib.request.urlretrieve(img_url, filename)
    k.append(filename)

o=[]
for i in range(0,len(k)):
    image=mpimg.imread(k[i])
    o.append(image)

### ALL IMAGES
fig = plt.figure(figsize=(12, 8)) 
gs = gridspec.GridSpec(int(len(k)/5),5)     
for i in range(0,len(k)-1):
    ax0=plt.subplot(gs[i])    
    ax0.axes.get_xaxis().set_ticks([])
    ax0.axes.get_yaxis().set_ticks([])
    plt.imshow(o[i])
    