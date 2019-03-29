# encoding=utf-8
import jieba
sentence="我来到北京清华大学"
w1=jieba.cut(sentence,cut_all=True)
w2=jieba.cut(sentence,cut_all=False)
w3=jieba.cut(sentence)
print("/".join(w1))
print("/".join(w2))
print("/".join(w3))