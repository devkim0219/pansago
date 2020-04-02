from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

def step2_preprocessing():
    df = pd.read_csv('prec_data.csv')

    title_list = df['law_title'].tolist()
    jm_list = df['law_jm'].tolist()

    title_train, title_test, jm_train, jm_test = train_test_split(title_list, jm_list, test_size=0.3, random_state=0)

    dic_train = {'title': title_train, 'jm': jm_train}
    df_train = pd.DataFrame(dic_train)

    dic_test = {'title': title_test, 'jm': jm_test}
    df_test = pd.DataFrame(dic_test)

    df_train.to_csv('prec_train_data.csv', index=False, encoding='utf-8')
    df_test.to_csv('prec_test_data.csv', index=False, encoding='utf-8')