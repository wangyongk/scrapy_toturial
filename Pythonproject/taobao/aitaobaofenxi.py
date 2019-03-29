'''
Function:
	数据分析
作者:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import os
import jieba
import pickle
import seaborn
import numpy as np
import pandas as pd
from scipy.misc import imread
from pyecharts import Map
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"simkai.ttf", size=12)
seaborn.set(font=font.get_name())


'''画柱状图'''
def drawBar(data, x_label, y_label, title, savepath='results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	ax = seaborn.barplot(x=x_label, y=y_label, palette="RdBu_r", data=data)
	ax.set_title(title)
	plt.show()
	fig = ax.get_figure()
	fig.savefig(os.path.join(savepath, title+'.png'))


'''画地图'''
def drawMap(data, title, savepath='results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	map_ = Map(title, width=1200, height=600)
	attrs = [i for i, j in data.items()]
	values = [j for i, j in data.items()]
	map_.add('', attrs, values, maptype='china', is_visualmap=True, visual_text_color='#000')
	map_.render(os.path.join(savepath, title+'.html'))


# 词云
def DrawWordCloud(words, title, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080, margin=5, mask=imread('mask.jpg'))
	wc.generate_from_frequencies(words)
	wc.to_file(os.path.join(savepath, title+'.png'))


# 统计词频
def statistics(texts, stopwords):
	words_dict = {}
	for text in texts:
		temp = jieba.cut(text)
		for t in temp:
			if t in stopwords:
				continue
			if t in words_dict.keys():
				words_dict[t] += 1
			else:
				words_dict[t] = 1
	return words_dict


if __name__ == '__main__':
	f = open('data.pkl', 'rb')
	data = pickle.load(f)
	'''
	# 价格统计
	prices = []
	for key, value in data.items():
		if value[0]:
			prices.append(value[0])
	price1_count = (np.array(prices) < 3).sum()
	price2_count = (np.array(prices) < 10).sum() - price1_count
	price3_count = (np.array(prices) < 20).sum() - price1_count - price2_count
	price4_count = (np.array(prices) >= 20).sum()
	prices_stat = pd.DataFrame({'价格': ['小于3元', '3-10元之间', '10-20元之间', '20元以上'], '数量': [price1_count, price2_count, price3_count, price4_count]})
	drawBar(prices_stat, '价格', '数量', '圣诞帽价格分布柱状图')
	'''
	'''
	# 商家位置统计
	locations_dict = {}
	for key, value in data.items():
		loc = value[4].split(' ')[0]
		if loc not in locations_dict:
			locations_dict[loc] = 1
		else:
			locations_dict[loc] += 1
	drawMap(locations_dict, '圣诞帽商家分布')
	'''
	'''
	salecounts_dict = {}
	for key, value in data.items():
		salecounts_dict[key] = value[2]
	temp = sorted(salecounts_dict.items(), key=lambda item: -item[1])
	salecounts_stat = {'商家': [], '销售数量': []}
	count = 0
	for key, value in temp:
		count += 1
		salecounts_stat['商家'].append(key[:4]+'...')
		salecounts_stat['销售数量'].append(value)
		if count == 10:
			break
	salecounts_stat = pd.DataFrame(salecounts_stat)
	seaborn.set(font_scale=0.7, font=font.get_name())
	drawBar(salecounts_stat, '商家', '销售数量', '圣诞帽销量最高的前10家店铺')
	'''
	stopwords = open('./stopwords.txt', 'r', encoding='utf-8').read().split('\n')[:-1]
	texts = [d[1][-1] for d in data.items()]
	words_dict = statistics(texts, stopwords)
	DrawWordCloud(words_dict, '商家描述词云', savepath='./results')
	texts = [d[0] for d in data.items()]
	words_dict = statistics(texts, stopwords)
	DrawWordCloud(words_dict, '商家名词云', savepath='./results')