# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:44:00 2017

@author: mi_o3
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def show_central_limit_theorem(Name_dstribution):
    nbin = 100
    Sig = 0
    Mu = 0
    N_sample = 50000

    N_mean = 128
    N_mean_sample = 5000
    
    fig = plt.figure()
    ax = fig.add_subplot(2,1,1)  
    ax2 = fig.add_subplot(2,1,2)  
    
    if Name_dstribution == 'Gaussian':
        Sig = 1.0
        Mu = 0
        x = np.random.normal(Mu,Sig,N_sample)
    elif Name_dstribution == 'Poisson':
        lam = 2.0
        Sig = lam 
        Mu = lam 
        x = np.random.poisson(lam ,N_sample)
    elif Name_dstribution == 'Bin':
        p = 0.5
        n = 2
        Sig = n*p*(1-p)
        Mu = np
        x = np.random.binomial(2,0.5, N_sample)

    x_l = np.floor(x.min() - 1)
    x_u = np.floor(x.max() + 1)
    ax.set_title(Name_dstribution + ' x hist\t' +'$\mu=$' + str(Mu) + ' $\sigma=$' + str(Sig))
    ax.set_xlabel('x')
    ax.set_ylabel('prb')
    #ax.set_xlim([x_l,x_u])
    ax.hist(x,bins=nbin, normed=True)
    
    x_ave = []
    for j in range(N_mean_sample):
        x_array = []
        for i in range(N_mean):
            x_array.append(np.random.choice(x))
        x_array = np.array(x_array)
        x_ave.append(x_array.mean())
    
    x_ave = np.array(x_ave)
    #ax2.set_xlim([x_l,x_u])
    histInfo = ax2.hist(x_ave-Mu,bins=nbin, normed=True)
    clt_std = Sig / np.sqrt(N_mean)
    bin_cent = []
    for i in range(len(histInfo[1]) -1 ):
        bin_cent.append( (histInfo[1][i+1] + histInfo[1][i]) / 2.0 )
    bin_cent = np.array(bin_cent)
    ax2.plot(bin_cent,(1 / np.sqrt(2 * np.pi * clt_std**2 ) ) * np.exp(-(bin_cent - 0)** 2 / (2 * clt_std**2)),color='#ff0000',label='$\sigma$=' + str(clt_std) )
    ax2.set_title('$ave(x) - \mu$ hist')
    ax2.set_xlabel('$ave(x)$')
    ax2.set_ylabel('prb')
    ax2.legend(loc="upper right")
    
    plt.tight_layout()

if __name__ == '__main__':
    show_central_limit_theorem('Gaussian')
    #show_central_limit_theorem('Bin')
    show_central_limit_theorem('Poisson')