import pickle
import numpy as np

def step4_using():
    with open('prec_pipe.dat', 'rb') as fp :
        pipe = pickle.load(fp)

    while True:
        keyword = input("범죄 유형을 입력하세요 :")

        # 데이터를 입력해 결과를 가져온다.
        y = pipe.predict([keyword])
        rate = pipe.predict_proba([keyword]) * 100
        rate = np.max(rate)

        # print(y)

        if y == '1':
            print('징역!!')
        else :
            print('무죄!!')

        print('정확도 : %d' % rate)