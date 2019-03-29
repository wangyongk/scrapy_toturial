import pickle
f = open('data2.pkl','rb')
data = pickle.load(f)
#info.strip('')
#texts = [d[0] for d in data.items()]
texts = []
for d in data.items():
    texts = [d[0]]
    texts=' '.join((texts))
    print(texts)