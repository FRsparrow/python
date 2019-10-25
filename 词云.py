import jieba as j
import wordcloud as w
a = w.WordCloud()
txt = " ".join(j.lcut("喵喵喵杨雨彤嘤嘤嘤"))
a.generate(txt)
a.to_file("hhh.png")
