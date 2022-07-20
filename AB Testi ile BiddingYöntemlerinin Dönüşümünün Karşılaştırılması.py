import pandas as pd
import numpy as np
import math
import datetime
import scipy.stats as st
#import sklearn
#from sklearn.preprocessing import MinmaxScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 20)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.5f' %x)


data = pd.read_csv("Datasets/amazon_review.csv")

df = data.copy()

# Görev 1.1:  Average Rating’igüncel yorumlara göre hesaplayınız
# ve var olan average rating ile kıyaslayınız.

df.columns

df.shape

df['overall'].mean()

# Gorev 1.2: Tarihe gore agirlikli puan ortalamasini hesaplayiniz.


df['reviewTime'] = pd.to_datetime(df['reviewTime'])
df.info()

current_date = df['reviewTime'].max()
df['date_difference'] = (current_date - df['reviewTime']).dt.days

df['date_difference'].quantile([.25, .5, .75])  # df['date_difference'].describe().T 'da olabilirdi.

df.loc[(df['date_difference'] <=280), 'overall'].mean() # 1. quantile puan ortalamasi
df.loc[(df['date_difference']> 280) & (df['date_difference']<= 430), 'overall'].mean() # 2. quantile puan ortalamasi
df.loc[(df['date_difference']> 430) & (df['date_difference']<= 600), 'overall'].mean() # 3. quantile puan ortalmasi
df.loc[(df['date_difference']> 600), 'overall'].mean() #4. quantile puan ortalamasi

df.loc[(df['date_difference'] <= 280), 'overall'].mean() * 33/100 # 3. adim yorum sorusu
df.loc[(df['date_difference'] > 280) & (df['date_difference'] <= 430), 'overall'].mean() * 30/100
df.loc[(df['date_difference'] > 430) & (df['date_difference'] <= 600), 'overall'].mean() * 20/100
df.loc[(df['date_difference'] > 600), 'overall'].mean() * 17/100

df

# Bu fonksiyon ekstra. Her quantile icin farkli agirliklari denemek icin. Vahit hocanin derste yaptigi gibi.
def weighted_average( df, a1, a2, a3, a4):
    return  df.loc[(df['date_difference'] <= 280), 'overall'].mean() * a1/100 + \
            df.loc[(df['date_difference'] > 280) & (df['date_difference'] <= 430), 'overall'].mean() * a2/100 + \
            df.loc[(df['date_difference'] > 430) & (df['date_difference'] <= 600), 'overall'].mean() * a3/100 + \
            df.loc[(df['date_difference'] > 600), 'overall'].mean() * a4/100
weighted_average(df, a1 = 33, a2 = 30, a3= 20, a4= 17)
df['overall'].mean() # Ratingler, Agirlikli ortalamamizda 4.61, agirliksiz ortalamada 4.58 cikti. Guncel yorumlar
# daha positif gelmis, varsa urunde veya operasyonel anlamda yaptigimiz degisiklikler
# olumlu sonuclanmis diyebilirdik.

# GOREV 2: Ürün için ürün detay sayfasında görüntülenecek 20 review’ibelirleyiniz.

df['helpful_no'] = df['total_vote'] - df['helpful_yes']

def score_pos_neg_diff(positive, negative):
    return positive - negative

def score_average_rating(positive, negative):
    if positive + negative == 0:
        return 0
    else:
        return (positive / (positive+negative))

def wilson_lower_bound(up, down, confidence = 0.95):
    n = up + down
    if n == 0:
        return 0
    z = st.norm.ppf(1 - (1- confidence) / 2)
    phat = 1.0 * up / n
    return (phat + z  * z / (2 * n) - z * math.sqrt((phat * ( 1 - phat) + z * z / ( 4 * n)) / n)) / ( 1 + z * z / n)

df['score_pos_neg_diff'] = df.apply(lambda x: score_pos_neg_diff(x['helpful_yes'], x['helpful_no']), axis = 1 )

df['score_average_rating'] = df.apply(lambda x: score_average_rating(x['helpful_yes'], x['helpful_no']), axis = 1)

df['wilson_lower_bound'] = df.apply(lambda x: wilson_lower_bound(x['helpful_yes'], x['helpful_no']), axis = 1 )

df.sort_values('wilson_lower_bound', ascending = False)[:20]
