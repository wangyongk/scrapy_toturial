import requests
import csv
from lxml import etree
with open('data.csv', 'a', newline='',encoding='utf-8') as f:
    spamwriter = csv.writer(f)
    spamwriter.writerow(['title', 'star', 'date', 'score'])