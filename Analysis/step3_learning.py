from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import pickle
from time import time
import pandas as pd
from konlpy.tag import Okt
from soynlp.tokenizer import MaxScoreTokenizer
from sklearn.preprocessing import StandardScaler

okt = Okt()

def tokenizer(text):
    return okt.morphs(text)

def step3_learning():
    train_df = pd.read_csv('prec_train_data.csv')
    test_df = pd.read_csv('prec_test_data.csv')

    X_train = train_df['title'].astype('str').tolist()
    y_train = train_df['jm'].astype('str').tolist()

    X_test = test_df['title'].astype('str').tolist()
    y_test = test_df['jm'].astype('str').tolist()

    tfidf = TfidfVectorizer(lowercase=False, tokenizer=tokenizer)
    logistic = LogisticRegression(C=1000.0, penalty='l2', random_state=0)
    pipe = Pipeline([('tfidf', tfidf), ('clf', logistic)])

    # 학습
    stime = time()

    print('학습 시작')

    pipe.fit(X_train, y_train)

    print('학습 종료')

    etime = time()

    print('총 학습 시간 : %d' % (etime - stime))

    # 학습 정확도 측정
    y_pred = pipe.predict(X_test)
    print('정확도 : %.3f' % accuracy_score(y_test, y_pred))

    # 객체 저장
    with open('prec_pipe.dat', 'wb') as fp:
        pickle.dump(pipe, fp)