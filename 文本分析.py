import re
import jieba
import csv
from pyecharts import options as opts
from pyecharts.charts import Page, WordCloud
from pyecharts.globals import SymbolType
# 读取⽂件中的⽂本
text = open(r'C:\Users\TingZhouZiMu\Desktop\Python\结题.txt', encoding='utf-8').read()
#剔除⾮中⽂的内容（只保留中⽂）
text = ''.join(re.findall(r'[\u4e00-\u9fa5]+', text))
#jieba分词
wordlist = jieba.lcut(text)
wordset = [w for w in set(wordlist) if len(w)>1]
wordfreq = []
#词语计数
for word in wordset:
    freq = wordlist.count(word)
    wordfreq.append((word, freq))
 
# 词频排序
wordfreq = sorted(wordfreq, key=lambda k:k[1], reverse=True)
wordcloud =WordCloud()
wordcloud.add("",
 wordfreq,
 word_size_range=[20,100])
wordcloud.set_global_opts(title_opts=opts.TitleOpts(title="项目"))
wordcloud.render('C:\\Users\TingZhouZiMu\Desktop\Python爬虫与文本分析\项目.html')
wordcloud.render_notebook()


import jieba 
import re
from collections import Counter
import json
import matplotlib.pyplot as plt
 
stopfile=open(r'C:\Users\TingZhouZiMu\Desktop\Python\结题.txt', 'r', encoding='UTF-8').read() 
stopfile = stopfile.replace(" ","")
stoplist = stopfile.split('\n') 
words = [x for x in jieba.lcut(stopfile) if len(x) >= 2 and x not in stoplist] 

top10 = Counter(words).most_common(10) 
print(json.dumps(top10, ensure_ascii=False)) 
# 画出柱状图 
plt.rcParams['font.sans-serif'] = ['SimHei'] 
c=top10
plt.rcParams['font.family']='sans-serif' 
name_list=[x[0] for x in c] 
num_list=[x[1] for x in c] 
b=plt.bar(range(len(num_list)), num_list,tick_label=name_list)








import jieba 
import re
from collections import Counter
import json
import matplotlib.pyplot as plt

stopfile=open(r'C:\Users\TingZhouZiMu\Desktop\Python\结题.txt', 'r', encoding='UTF-8').read() 
# 将中文停用词文档读取为python列表 
stopfile = stopfile.replace(" ","")
stoplist = stopfile.split('\n') 
# 分词，并按照 if 后的条件对分词进行筛选 
words = [x for x in jieba.lcut(stopfile) if len(x) >= 2 and x not in stoplist] 

keywords = ['全球价值链','创新','产品质量','政策','位置','制造业']
b=Counter(words)
#提取重点词汇的频次
wordsfreq = [b[x] for x in keywords]
totalfreq = sum(wordsfreq)
 # 所有词语的总数
s= sum(b.values())
# 计算比重
weight = totalfreq/s
print(keywords)
print(wordsfreq)
print(totalfreq)
print(weight)