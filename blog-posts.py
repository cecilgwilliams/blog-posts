import xml.etree.ElementTree as ET
from collections import Counter

tree = ET.parse('wordpress.2013-11-12.xml')
root = tree.getroot()

authors = []

for author in root.iter('{http://purl.org/dc/elements/1.1/}creator'):
		authors.append(author.text)

cnt = Counter()
for name in authors:
	cnt[name] += 1
	
for result in sorted(cnt.items(), key=lambda x:x[1], reverse=True):
	print result