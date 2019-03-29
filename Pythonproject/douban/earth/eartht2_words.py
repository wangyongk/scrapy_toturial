import jieba
import wordcloud


with open('liulangdiqiu.txt','r',encoding='utf-8') as f:
    txt = f.read()
    txt = txt.replace('来自', '').replace('豆瓣', '').replace('电影', '').replace('作者', '').replace('来源', '') \
        .replace('版权', '').replace('这个', '').replace('就是', '').replace('我们', '').replace('不是', '').replace('没有', '') \
        .replace('还是', '').replace('但是', '').replace('这样', '').replace('这部', '').replace('一个', '').replace('自己','')\
        .replace('真的','').replace('如果','').replace('感觉','').replace('觉得','').replace('什么','').replace('所以','')\
        .replace('还有','').replace('最后','').replace('因为','').replace('那么','')

ls = jieba.lcut(txt)
txt = ' '.join(ls)

w = wordcloud.WordCloud( width = 1000,height = 700,
                        font_path = 'msyh.ttc',)
w.generate(txt)
w.to_file('comments.png')


