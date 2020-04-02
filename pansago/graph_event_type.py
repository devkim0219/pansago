import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import re
import io #그래프를 byte로 변경
import base64 #웹에 출력하기 위해서

def draw_graph(keyword):
    # 마이너스 폰트 깨짐 현상 수정
    mpl.rcParams['axes.unicode_minus'] = False

    # 한글 폰트 설정
    path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf'
    font_name = fm.FontProperties(fname=path, size=15).get_name()
    plt.rc('font', family=font_name)

    prec = pd.read_csv('C:/Users/admin/Documents/pansago/law_list_detail.csv', encoding='utf-8')

    prec['law_date'] = prec['law_date'].astype('str')
    prec['law_count'] = 1

    # print(prec.shape)
    # print(prec.head())
    # print(prec.tail())
    # print(prec.info())
    # print(prec.isnull().sum())
    # print(prec.dtypes)
    # print(prec.columns)

    # 선고일자에서 앞 4자리를 슬라이스 후 연도 컬럼 생성

    year_list = []

    for tmp in prec['law_event_no']:
        if tmp[:1] == '(':
            if tmp[4:6] == '20':
                year_list.append(tmp[4:8])
            else:
                year_list.append('19' + tmp[4:6])

        elif re.match('^[가-힣]+$', tmp[:1]):
            year_list.append(tmp[4:6])

        else:
            if tmp[:2] == '20':
                year_list.append(tmp[0:4])
            else:
                year_list.append('19' + tmp[:2])

    prec['law_year'] = year_list
    prec['law_title'].fillna('1', inplace=True)

    # print(prec.shape)
    # print(prec.isnull().sum())

    prec_kill = prec[prec['law_title'].str.contains(keyword)]
    # print(prec_kill)
    prec_kill['title'] = keyword

    # 스타일 서식 지정
    plt.style.use('ggplot')

    prec_pivot = pd.pivot_table(prec_kill, index='law_year', columns='title', values='law_count', aggfunc='sum')
    print(prec_pivot)

    max_count = 0

    for count in prec_pivot[keyword]:
        if count > max_count:
            max_count = count

    # print('max_count : ', max_count)

    ax1 = prec_pivot[[keyword]].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True, legend=None)

    ax1.set_ylim(0, (max_count - (max_count % 10) + 10))

    ax1.set_xlabel('연도', size=20)
    ax1.set_ylabel('판례수(건)', size=20)

    plt.title('연도별 ' + keyword + ' 사건 판례수(2019년 10월 기준)', size=20)

    # plt.show()

    plt.draw()
    img = io.BytesIO() #그린그래프를 바이트로 변경
    plt.savefig(img, format="png") #png포맷으로 변경
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close() #그래프 종료

    graph = 'data:image/png;base64,{}'.format(graph_url)

    return graph