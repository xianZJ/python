import itchat
import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# from collections import defaultdict
# import re
# import jieba
# import os
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import PIL.Image as Image


def wechat(friends):
    '''
    微信朋友男女比例分析
    :param friends:
    :return:
    '''
    male = 0
    female = 0
    other = 0
    # friends[0]是自己的信息，因此我们要从[1:]开始
    for i in friends[1:]:
        sex = i['Sex']  # 注意大小写，2 是女性， 1 是男性
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    # 计算好友总数
    total = len(friends[1:])
    # print('好友总数：', total)
    # print('男性比例：%2f%%' % (float(male) / total * 100))
    # print('女性比例：%2f%%' % (float(female) / total * 100))
    # print('未知性别：%2f%%' % (float(other) / total * 100))
    # 柱状图显示
    arr = ['1'] * male  # 男性
    arr1 = ['2']*female # 女性
    arr2 = ['0'] * other    #未知
    arr.extend(arr1)
    arr.extend(arr2)
    plt.hist(arr)
    plt.show()
    msg = '好友总数：' + str(total) + '\n' +'男性比例：%2f%%' % (float(male) / total * 100) + '\n' +'女性比例：%2f%%' % (float(female) / total * 100) + '\n' +'未知性别：%2f%%' % (float(other) / total * 100)
    return msg


if __name__ == '__main__':

    itchat.login()

    # itchat.send('Hello, filehelper', toUserName='filehelper')  #测试是否可以使用发送给文件助手消息

    friends = itchat.get_friends(update=True)
    loginPer = friends[0]["NickName"] + ".txt"
    # print(friends)
    # 设置需要爬取的信息字段
    result = [('RemarkName', '备注'), ('NickName', '微信昵称'), ('Sex', '性别'), ('City', '城市'), ('Province', '省份'),
              ('ContactFlag', '联系标识'), ('UserName', '用户名'), ('SnsFlag', '渠道标识'), ('Signature', '个性签名')]
    for user in friends:
        with open(loginPer, 'a', encoding='utf8') as fh:
            fh.write("-----------------------\n")
        for r in result:
            with open(loginPer, 'a', encoding='utf8') as fh:
                fh.write(r[1] + ":" + str(user.get(r[0])) + "\n")
    print("完成")
    msg = wechat(friends)
    itchat.send(msg,toUserName='filehelper')
