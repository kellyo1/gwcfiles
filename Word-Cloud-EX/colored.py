#!/usr/bin/env python


import json
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'tweets.json')).read()

# read the mask / color image taken from
# https://orig00.deviantart.net/edb5/f/2015/246/d/e/panda_we_bare_bears_by_yocatglitter-d98a6sj.png
bears_coloring = np.array(Image.open(path.join(d, "minnie.jpg")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask= bears_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(bears_coloring)

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
plt.figure()
plt.imshow(bears_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off")
plt.show()
