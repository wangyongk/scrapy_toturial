# # import matplotlib.pyplot as plt
# # # from pylab import mpl
# # # plt.figure(figsize=(8,8))
# # # mpl.rcParams['font.sans-serif'] = ['STKaiti'] # 指定默认字体
# # # mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# # # labels = 'girls','boys'
# # # sizes = [12,63]
# # # colors = ['red','orange']
# # # explode = (0,0.1) #0.1表示将Hogs那一块凸显出来
# # # plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%', colors=colors,shadow=False,startangle=90) #startangle表示饼图的起始角度
# # # plt.title(u'男女比例',fontsize=42)
# # # plt.legend(loc='upper left',bbox_to_anchor=(-0.15, 1),fontsize=22)
# # # plt.axis('equal')  #加入这行代码即可！
# # # plt.show()
# #coding:utf-8
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
# import jieba
# import numpy as np
# from PIL import Image
#
# #读入背景图片
# abel_mask = np.array(Image.open("filepath"))
#
# #读取要生成词云的文件
# text_from_file_with_apath = open('filepath').read()
#
# #通过jieba分词进行分词并通过空格分隔
# wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
# wl_space_split = " ".join(wordlist_after_jieba)
# #my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
# my_wordcloud = WordCloud(
#             background_color='white',    # 设置背景颜色
#             mask = abel_mask,        # 设置背景图片
#             max_words = 200,            # 设置最大现实的字数
#             stopwords = STOPWORDS,        # 设置停用词
#             font_path = 'D:/msyh.ttf',# 设置字体格式，如不设置显示不了中文
#             max_font_size = 50,            # 设置字体最大值
#             random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
#                 scale=.5
#                 ).generate(wl_space_split)
#
# # 根据图片生成词云颜色
# image_colors = ImageColorGenerator(abel_mask)
# #my_wordcloud.recolor(color_func=image_colors)
#
# # 以下代码显示图片
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()
#
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
