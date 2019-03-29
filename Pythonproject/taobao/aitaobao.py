'''
Function:
	ai.taobao.com数据爬取
作者:
	Charles
微信公众号:
	Charles的皮卡丘
'''
import time
import pickle
import csv
import requests
from urllib.parse import quote

HEADERS = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
URL = 'https://ai.taobao.com/search/getItem.htm'
PARMAS = {'key': None}


'''主函数'''
def main(keyword, num_pages=20):
	data = {}
	PARMAS['key'] = quote(keyword)
	for page in range(0, num_pages):
		print('[INFO]: Starting get the data of page.<%d>...' % page)
		PARMAS['page'] = str(page)
		res = requests.get(URL, headers=HEADERS, params=PARMAS)
		res_json = res.json()
		items = res_json['result']['auction']
		for item in items:
			description = item.get('description');
			#print(description)
			description=description.replace('&lt;span', '').replace('class=H&gt;', '').replace('&lt;/span&gt;', '')
			#description2 = description.strip('lt');
			#print(description2)
			price = item.get('price')
			#print(price)
			real_price = item.get('realPrice')
			#print(real_price )
			sale_count = item.get('saleCount')
			#print(sale_count)
			item_id = item.get('itemId')
			#print(item_id)
			item_location = item.get('itemLocation')
			#print(item_location)
			nick = item.get('nick')
			#print(nick)
			data[nick] = [price, real_price, sale_count, item_id, item_location, description]
		time.sleep(2)

	with open('data2.pkl', 'wb') as f:
		pickle.dump(data, f)
if __name__ == '__main__':
	keyword = input('请输入关键词:')
	print()
	num_pages = int(input('请输入爬取的页数:'))
	print()
	main(keyword, num_pages)