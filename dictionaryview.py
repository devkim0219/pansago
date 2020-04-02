#law_title
#잘 익숙하지 않은 단어를 법률용어대사전으로 링크 연결시켜 단어 정의 보여주기
#view 겸용
# import pandas as pd
# import warnings
# warnings.filterwarnings('ignore')

# import numpy as np
# import re
# from soynlp.tokenizer import RegexTokenizer
# import logging
# from gensim.models import word2vec

# from collections import Counter
# from sklearn.manifold import TSNE
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import gensim
# import gensim.models as g
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.shortcuts import redirect
# from django.views.decorators.csrf import csrf_exempt
# from django.db import connection

# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout

# from django.db import connection


#main > views > 사전 링크 걸기
# @csrf_exempt
# def dictionary(request) :
#     if request.method == "GET" :
#         return render(request, 'shop/auth_login.html')
#     elif request.method == "POST" :
#         id = request.POST['username']
#         pw = request.POST['password']

#         user = authenticate(request, username=id, password=pw)
#         if user is not None:
#             login(request, user) #로그인 처리
#             return redirect("/shop/auth_index")
#         else:
#             return redirect("/shop/auth_login")

#127.0.0.1:8000/board/index

# def index(request):
    # return HttpResponse("index page")
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM board")
#     row = cursor.fetchall()
#     print(row)

#     return render(request, 'board/index.html')

# @csrf_exempt
# def dictionary2(request):
#     if request.method == "GET":
#         return render(request, 'board/boardwrite.html')
#     elif request.method == "POST":
#         ti = request.POST['ti']
#         co = request.POST['co']
#         img = request.POST['img']
#         wr =request.POST['wr']

#         a1 = [ti, co, img.read(), wr]
#         #print(a1)

#         cursor = connection.cursor()
#         sql =  """
#             INSERT INTO BOARD
#             (BRD_NO, BRD_TITLE, BRD_CONTENT, BRD_IMG, BRD_WRITER, BRD_HIT, BRD_DATE) 
#              VALUES(SEQ_BOARD_NO.NEXTVAL, %s, %s, %s, %s, 1, SYSDATE)   
#              """
#         cursor.execute(sql, a1)
#         #connection.commit()

#         return redirect("/board/index")


# def boardlist(request):
#     cursor =  connection.cursor() # cursor 얻기
#     sql = "SELECT * FROM BOARD ORDER BY BRD_NO DESC"
#     cursor.execute(sql) #SQL 문 수행
#     rows = cursor.fetchall() #결과값 받기
#     print(rows)

#     return render(request, 'board/boardlist.html', {"data":rows})

#그래프에서 마이너스 폰트 깨지는 문제에 대한 대처
# mpl.rcParams['axes.unicode_minus'] = False
# model_name = '1minwords'
# model = g.Doc2Vec.load(model_name)

# df = pd.read_csv('data/petition.csv', parse_dates=['start', 'end'])

# 관심사별로 텍스트 데이터를 학습시키기 위한 목적 있지만 전체 텍스트를 돌렸을 때
# 빠르게 결과를 얻기 위함. 샘플링 의도

# def preprocessing(text):
#     #개행문자 제거
#     text = re.sub('\\\\n', ' ', text)
#     #특수 문자 제거
#     #특수문자나 이모티콘 제거
#     #text = re.sub('[?.,;:|\)*~'"!^\-_+<>@\#$%&~=#}*]', '', text)
#     #한글, 영문, 숫자만 남기고 모두 제거
#     #text = re.sub('[^가-힣ㄱ-ㅎㅏ-|a-zA-Z0-9]', ' ', text)
#     # 한글, 영문만 남기고 모두 제거
#     text = re.sub('[^가-힣ㄱ-ㅎㅏ-|a-zA-Z]', ' ', text)
#     return text

# sample_content = preprocessing(sample_content)
# sample_content[:1000]

# %time sentences = finance['content'].apply(preprocessing)

# tokenizer = RegexTokenizer()


# tokened_title = tokenizer.tokenize(sample_title)
# tokened_title

# tokened_content = tokenizer.tokenize(sample_content)
# tokened_content[:10]

# print(len(tokened_title))
# print(len(tokened_content))























