import pickle
f = open('data2.pkl','rb')
info = pickle.load(f)
#data = pickle.load(f)
#info.strip('')

#texts = [d[1] for d in data.items()]
#texts = []
#print(texts)
print(info)