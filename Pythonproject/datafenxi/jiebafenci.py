# encoding=utf-8
import jieba
sentence="我来到北京清华大学"
w1=jieba.cut(sentence,cut_all=True) # 全模式
w2=jieba.cut(sentence,cut_all=False) # 精确模式
w3=jieba.cut(sentence) # 默认是精确模式
w4=jieba.cut_for_search(sentence)# 搜索引擎模式
print("/".join(w1))
print("/".join(w2))
print("/".join(w3))
print("/".join(w4))
#词性标注
import jieba.posseg as pseg
words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))