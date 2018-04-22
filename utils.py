import math

def custom_paginator(current_page,total_page,max_page):
    # 根据当前页,判断分页的首页和最后一页
    # max_page,展示的页数最多为多少页;total_page,共有多少页
    middle = math.ceil(max_page/2)

    # 特殊情况,页最大页数小于最大显示的页数
    if total_page <= max_page:
        start = 1
        end = total_page
    else:
        # 当前页小于等于middle时
        if current_page <= middle:
            start = 1
            end = max_page
        else:
            # 中间情况
            start = current_page - middle
            end = current_page + middle -1
            # 当前页在尾巴的情况
            if current_page+middle>total_page:
                start = total_page - max_page +1
                end = total_page
    return start,end



