import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 마이너스 폰트 깨짐 현상 수정
mpl.rcParams['axes.unicode_minus'] = False

# 한글 폰트 설정
path = 'C:/Users/admin/AppData/Local/Microsoft/Windows/Fonts/D2Coding.ttf'
font_name = fm.FontProperties(fname=path, size=15).get_name()
plt.rc('font', family=font_name)

prec = pd.read_csv('law_list_detail.csv', encoding='utf-8')

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
prec['law_year'] = prec['law_date'].str.slice(stop=4)

# 1991년 데이터 삭제
prec = prec[prec['law_year'] != '1991']

print(prec['law_year'])

# 스타일 서식 지정
plt.style.use('ggplot')

prec_pivot = pd.pivot_table(prec, index='law_year', columns='law_event_type', values='law_count', aggfunc='sum')
print(prec_pivot)

ax1 = prec_pivot[['가사', '민사', '세무', '일반행정', '특허', '형사']].plot(kind='bar', figsize=(20, 10), width=0.7, stacked=True)

ax1.set_ylim(0, 3000)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('판례수(건)', size=20)

plt.title('사건 종류별 판례수(2019년 10월 기준)', size=20)
ax1.legend(loc='upper right')

plt.show()