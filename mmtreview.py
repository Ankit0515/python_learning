from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
from google_play_scraper import reviews_all, Sort
import jason 
 
# Reads 'Youtube04-Eminem.csv' file
df = reviews_all(
    'com.next.innovation.takatak',
    sleep_milliseconds=0,
    lang='en', #set language to english.
    country='in', # set country to Hong Kong.
    sort=Sort.NEWEST, # Default is Sort.
)
comment_words = ''
stopwords = set(STOPWORDS)
 
# iterate through the csv file
for val in df.CONTENT:
     
    # typecaste each val to string
    val = str(val)
 
    # split the value
    tokens = val.split()
     
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
    comment_words += " ".join(tokens)+" "
 
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
 
# plot the WordCloud image                      
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
 
plt.show()
