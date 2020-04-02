import warnings
warnings.filterwarnings('ignore')

from pandas import DataFrame as df
import pandas as pd
import numpy as np
import re
from soynlp.tokenizer import RegexTokenizer
from soynlp.noun import LRNounExtractor
from collections import Counter
from wordcloud import WordCloud
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from stopwords import make_stopword

# 마이너스 폰트 깨짐 현상 수정
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf'
font_name = fm.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

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

def tag_counting(law_event_type):
    prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

    noun_extractor = LRNounExtractor(verbose=True)
    noun_extractor.train(prec[prec['law_event_type'] == law_event_type]['law_content'].astype('str').apply(preprocessing))
    nouns = noun_extractor.extract()

    count = Counter(nouns)
    # print(count)

    tag_count = []
    stopwords = make_stopword()
    # print(stopwords)

    for n, c in count.most_common(200):
        if n not in stopwords:
            dics = {'tag': n, 'count': c[0]}
            tag_count.append(dics)

        if len(tag_count) == 20:
            break

    # print(tag_count)

    for tag in tag_count:
        print("{:<14}".format(tag['tag']), end='\t')
        print("{}".format(tag['count']))

    df = pd.DataFrame.from_dict(tag_count, orient='columns')
    df.set_index(df['tag'], inplace=True)
    # print(df)

    # 스타일 서식 지정
    plt.style.use('ggplot')

    ax1 = df.plot(kind='bar', figsize=(20, 10), width=0.7, stacked=False, legend=None)

    ax1.set_ylim(0, 60000)
    ax1.set_xlabel('단어', size=20)
    ax1.set_ylabel('빈도수', size=20)

    plt.title('사건 종류별 특정 단어 빈도수(형사)', size=20)

    plt.show()

# 실행
# tag_counting('가사')      # limit -> 2000
# tag_counting('민사')      # limit -> 60000
# tag_counting('세무')      # limit -> 20000
# tag_counting('일반행정')  # limit -> 35000
# tag_counting('특허')      # limit -> 14000
tag_counting('형사')      # limit -> 60000