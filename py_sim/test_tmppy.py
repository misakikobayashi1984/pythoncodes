# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 22:57:20 2017

@author: mi_o3
"""


#エクセル読み込み


#開始点検出

arr_miss = [0,0,0,0,0]
arr_gt_no_miss = [0,0,0,0,-1,-2,-3,-4,-5]
serch_delta = 2

def sig_no_miss(arr=[], arr_miss=[]):
    arr_res = []
    for idx, val in enumerate(arr):
        if arr_miss[idx] == 0:
            arr_res.append(val)
    return arr_res

def get_search_point(arr=[]):
    gt_s = arr[get_gt_sIdx(arr=arr)]
    gt_e = arr[len(arr)-1]
    
    s_point = 0
    if gt_s > 0 and gt_e > 0:
        smaller = gt_s if gt_s < gt_e else gt_e
        s_point = smaller
        
    elif gt_s < 0 and gt_e < 0:
        bigger = gt_s if gt_s > gt_e else gt_e
        s_point = bigger
        
    else:
        s_point = 0
    return s_point

def get_gt_sIdx(arr=[]):
    gt_sIdx = 0
    for idx, val in enumerate(arr):
        if val != 0:
            gt_sIdx = idx
            break
    return gt_sIdx

def get_s(arr=[],arr_miss=[],s_range=[]):
    sIdxs = []
    for idx, val in enumerate(arr):
        if arr_miss[idx] == 0 and s_range[0] <= val and s_range[1] >= val:
            sIdxs.append(idx)
    return sIdxs 

if __name__ == "__main__":
    s_point = get_search_point(arr=arr_gt_no_miss)
    s_range = [s_point - serch_delta, s_point + serch_delta]
    print("s_point: ", s_point)