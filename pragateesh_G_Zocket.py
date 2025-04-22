import requests as r
from bs4 import BeautifulSoup as b
from transformers import pipeline as p
su = p("summarization", model="sshleifer/distilbart-cnn-12-6") 

a = 'https://en.wikipedia.org/wiki/Wikipedia:About'
print(a)
d = r.get(a)
print(d)
da = b(d.content,'html.parser')
s = ''
for i in da.find_all('p'):
    s += i.text
print(s)
ans = su(s, max_length=120, min_length=30, do_sample=False)
ans[0]['summary_text']