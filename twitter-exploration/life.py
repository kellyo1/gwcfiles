import json
from os import path
from wordcloud import *

import matplotlib.pyplot as plt

d = path.dirname(__file__)

# Read the whole text.
file = open(path.join(d, 'tweets.json')).read()

# Generate a word cloud image
wordcloud = WordCloud.generate(file)

# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
