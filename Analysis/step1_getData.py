import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from soynlp.tokenizer import RegexTokenizer
from wordcloud import WordCloud
from soynlp.tokenizer import RegexTokenizer
from stopwords import make_stopword
from soynlp.noun import LRNounExtractor
from konlpy.tag import Okt
from collections import Counter
import re
from stopwords_keyword import make_stopword

okt = Okt()

def tokenizer_nouns(text):
    return okt.nouns(text)

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

def jm_preprocessing(text):
    if ('징역' in text) or ('집행유예' in text) or ('집행 유예' in text):
        return '1'

    else:
        return '0'

def step1_getData():

    prec = pd.read_csv('C:/Users/admin/Documents/pansago/law_list_detail.csv', encoding='utf-8')

    # print(prec.shape)
    # print(prec.head())
    # print(prec.tail())
    # print(prec.info())
    # print(prec.isnull().sum())
    # print(prec.dtypes)
    # print(prec.columns)
    # 선고일자에서 앞 4자리를 슬라이스 후 연도 컬럼 생성

    law_jumoon = []

    for tmp in prec['law_content']:
        try :
            sub1 = tmp.split('문】')[1].split('【')[0]
            law_jumoon.append(sub1)
        except :
            law_jumoon.append('123')

    prec['law_title'].fillna('1', inplace=True)
    prec['law_jumoon'] = law_jumoon
    prec['law_title'] = prec['law_title'].apply(tokenizer_nouns)
    prec['token_jm'] = prec['law_jumoon'].apply(tokenizer_nouns)
    prec['law_jm'] = prec['token_jm'].apply(jm_preprocessing)

    df = prec[['law_title', 'law_jm']]
    print(df)

    # df.to_csv('prec_data.csv', mode='w')