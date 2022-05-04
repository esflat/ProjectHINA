# XX01 : 古典的なニューラルネットで使う関数の紹介
# 
# ニューラルネットでは、様々な活性化関数が使われました。
# 深層学習ではReLuと呼ばれる関数がよく使われます。
# どの関数もニューラルネットでは、値域、定義域共に[0-1]です。

import numpy as np

# シグモイド関数：神経科学でニューロンの活性化関数として使われる。計測近似関数。
#              ニューラルネットが、脳の近似なら同じ関数の方が学習精度が高いかと言うと、そうでもない。
#              微分が少し扱いづらい。
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ソフトマックス関数 : シグモイドに似た活性化関数。
#                   シグモイド関数を使うときは、ニューロンへの入力の総和をxとするが、ソフトマックスは入力の最大値をxとする。
#                   偏微分が楽という理由で便利。
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y