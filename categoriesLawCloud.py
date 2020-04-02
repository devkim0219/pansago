import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from stopwords import make_stopword

import soynlp
from soynlp.noun import LRNounExtractor

# import nltk
# from nltk.corpus import stopwords

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

def displayWordCloud(data=None, backgroundcolor='black', width=800, height=600):
    stopwords_kr = make_stopword()
    print('불용어 리스트 : ', stopwords_kr)
    
    wordcloud = WordCloud(
                        font_path = 'C:/Windows/Fonts/malgun.ttf',
                        stopwords = stopwords_kr,
                        background_color = backgroundcolor,
                        width = width,
                        height = height).generate(data)

    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

# contents = prec['law_content'].astype('str').apply(preprocessing)
# print(contents)





# law_categoriesGa = prec[prec['law_event_type'] == "가사"] 
# law_categoriesGa1 = law_categoriesGa['law_content'].astype('str').apply(preprocessing)
# print(law_categoriesGa1.head())

law_categoriesMin = prec[prec['law_event_type'] == "민사"]
law_categoriesMin1 = law_categoriesMin['law_content'].astype('str').apply(preprocessing)
# print(law_categoriesMin1.head())
# displayWordCloud(' '.join(law_categoriesMin1))


# law_categoriesSe = prec[prec['law_event_type'] == "세무"]
# law_categoriesSe1 = law_categoriesSe['law_content'].astype('str').apply(preprocessing)
# displayWordCloud(' '.join(law_categoriesSe1))


# law_categoriesH = prec[prec['law_event_type'] == "일반행정"]
# law_categoriesH1 = law_categoriesH['law_content'].astype('str').apply(preprocessing)
# displayWordCloud(' '.join(law_categoriesH1))

# law_categoriesT = prec[prec['law_event_type'] == "특허"]
# law_categoriesT1 = law_categoriesT['law_content'].astype('str').apply(preprocessing)
# # print(law_categoriesT1)
# displayWordCloud(' '.join(law_categoriesT1))


# law_categoriesP = prec[prec['law_event_type'] == "형사"]
# law_categoriesP1 = law_categoriesP['law_content'].astype('str').apply(preprocessing)
# displayWordCloud(' '.join(law_categoriesP1))

noun_extractor = LRNounExtractor(verbose=True)
noun_extractor.train(law_categoriesMin1)
# 명사만 추출
nouns = noun_extractor.extract()
# print(type(nouns))
# print(nouns)
displayWordCloud(' '.join(nouns))

# displayWordCloud(' '.join(law_categoriesGa1))