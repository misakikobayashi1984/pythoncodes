# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:30:24 2017

@author: mi_o3
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#ref
#Pythonでカルマンフィルタを実装してみる
#https://satomacoto.blogspot.jp/2011/06/python.html

#シンプルなモデルとイラストでカルマンフィルタを直感的に理解してみる
#http://qiita.com/MoriKen/items/0c80ef75749977767b43

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline 

def lkf(T, Y, U, mu0, Sigma0, A, B, C, Q, R):
    '''Linear Kalman Filter
    
    - 状態方程式
        x = A * x_ + B * u + w, w ~ N(0,Q)
    - 観測方程式
        y = C * x + v, v ~ N(0,R)
    
    Parameters
    ==========
    - T : ステップ数
    - Y : 観測列
    - U : 入力列
    - mu0 : 初期状態推定値
    - Sigma0 : 初期誤差共分散行列
    - A, B, C, Q, R : カルマンフィルタの係数 
    
    Returns
    =======
    - M : 状態推定値列
    '''

    mu = mu0 # 初期状態推定値
    Sigma = Sigma0 # 初期誤差共分散行列

    M = [mu] # 状態推定値列

    for i in range(T):
        # 推定
        mu_ = A * mu + B * U[i]
        Sigma_ = Q + A * Sigma * A.T#推定値の誤差

        # 更新
        yi = Y[i+1] - C * mu_
        S = C * Sigma_ * C.T + R
        K = Sigma_ * C.T * S.I
        mu = mu_ + K * yi
        Sigma = Sigma_ - K * C * Sigma_
        M.append(mu)

    return M

''' 設定 '''
def plot_pos():
    vlc = 30 #[kph]     
    x_0 = np.mat([[-80],[1.6]]) #[m]
    del_ts = 0.1 #[s]
    T_s = 10 #[s]
    
    ''' 定数 '''
    vlc_mps = vlc / 3.6
    T = int( T_s / del_ts )# 観測数
    
    # 状態方程式
    # x = A * x_ + B * u + w, w ~ N(0,Q)
    A = np.mat([[1,0], [0,1]])
    B = np.mat([[del_ts,0], [0,del_ts]])
    Q = np.mat([[0.001,0], [0,0.001]])#真値に乗る誤差
    u = np.mat([[vlc_mps],[0]]) # 入力（一定）
    # 観測方程式
    # y = C * x + v, v ~ N(0,R)
    C = np.mat([[1,0], [0,1]])#単位変換のための行列
    R = np.mat([[0.2,0], [0,0.2]])#観測値に乗る誤差
    
    # 観測のテストデータの生成
    x = x_0 # 初期位置
    X = [x] # 状態列
    Y = [x] # 観測列
    U = [u] # 入力列
    for i in range(T):
        x = A * x + B * u + np.random.multivariate_normal([0, 0], Q, 1).T
        X.append(x)
        y = C * x + np.random.multivariate_normal([0, 0], R, 1).T
        Y.append(y)
        U.append(u)
    
    # LKF
    mu0 = x_0 # 初期状態推定値
    Sigma0 = np.mat([[0,0],[0,0]]) # 初期誤差共分散行列
    M = lkf(T, Y, U, mu0, Sigma0, A, B, C, Q, R)
    
    # 描画
    fig = plt.figure()
    ax = fig.add_subplot(111)
    a, b = np.array(np.concatenate(X,axis=1))
    ax.plot(a,b,color='red',marker='o',label='gt')
    a, b = np.array(np.concatenate(Y,axis=1))
    ax.plot(a,b,color='blue',marker='o',label='obseved')
    a, b = np.array(np.concatenate(M,axis=1))
    ax.plot(a,b,color='orange',marker='o',label='lkf output')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc="lower right")
    
if __name__ == "__main__":
    plot_pos()

#例
# Q = np.mat([[0,0], [0,0]])の時
# K = np.mat([[0,0], [0,0]]), mu = mu_となるので、真値とlkf出力は一致する