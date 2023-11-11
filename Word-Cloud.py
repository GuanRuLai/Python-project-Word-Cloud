from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba
from collections import Counter
from PIL import Image
import numpy as np
import requests

text = open("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\travel.txt",
            "r", encoding="utf-8").read()

# replace "\n" with space
text = text.replace("\n", " ")

# set default word bank
jieba.set_dictionary("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\dict.txt.big")
# add stop words: deal with meaningless words
with open("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\stopWord_cloudmod.txt",
          "r", encoding="utf-8-sig") as f: # remove BOM problem
    stops = f.read().split("\n")

breakword = jieba.cut(text, cut_all=False)

# remove stop words
words = []
for word in breakword:
    if word not in stops:
        words.append(word)

# count words(decending sorted)
diction = Counter(words)

# set text type
fontfile = requests.get("https://drive.google.com/uc?id=1QdaqR8Setf4HEulrIW79UEV_Lg_fuoWz&export=download")
with open("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\taipei_sans_tc_beta.ttf", "wb") as f:
    f.write(fontfile.content)

# make wordcloud
mask = np.array(Image.open("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\heart.png"))
wordcloud = WordCloud(background_color="white", mask=mask,
                      font_path="C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\taipei_sans_tc_beta.ttf")
wordcloud.generate_from_frequencies(frequencies=diction)
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

# store wordcloud image
wordcloud.to_file("C:\\Users\\HP\\Desktop\\project\\NLP-Basic-Application\\Article-Summarization-and-Word-Cloud-dir\\bookCloud.png")