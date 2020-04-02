import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stopwords import make_stopword

# 텍스트 데이터 전처리
def preprocessing(text):

    # 개행문자 제거
    text = re.sub('\\\\n', ' ', text)

    # 【피 고 인】형식 문자 제거
    text = re.sub(r'\【[^)]*\】', '', text)

    # 양 끝 공백 제거
    text = text.strip()

    # 문자 중간 공백 1개
    text = ' '.join(text.split())

    return text

def displayWordCloud(data=None, backgroundcolor='white', width=800, height=600):
    stopwords_kr = make_stopword()
    print('불용어 리스트 : ', stopwords_kr)

    wordcloud = WordCloud(
                        font_path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf',
                        stopwords = stopwords_kr,
                        background_color = backgroundcolor,
                        width = width,
                        height = height).generate(data)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

contents = prec['law_content'].astype('str').apply(preprocessing)
print(contents)

displayWordCloud(' '.join(contents))