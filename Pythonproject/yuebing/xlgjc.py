w_s_sum = []
for w in word_count.word:
 i = 0
 s_list = []
 for t in title_clean_dist:
   if w in t:
     s_list.append(df.sales[i])
   i+= 1
 w_s_sum.append(sum(s_list))
df_w_s_sum = pd.DataFrame({'w_s_sum':w_s_sum})
df_word_sum = pd.concat([word_count,df_w_s_sum],axis=1,ignore_index=True)
df_word_sum.columns = ['word','count','w_s_sum']
df_word_sum.sort_values('w_s_sum',inplace=True,ascending=True)
df_w_s = df_word_sum.tail(30)
attr = df_w_s['word']
v1 = df_w_s['w_s_sum']
bar = Bar("月饼关键词销量分布图")
bar.add("关键词",attr,v1,is_stack=True,xaxis_rotate=30,yaxix_min=4.2,
    xaxis_interval=0,is_splitline_show=False)
overlap = Overlap()
overlap.add(bar)
overlap.render('月饼关键词_销量分布图.html')