# Collin Pearce/Marcos Duran 60% (rest WA)

# parse the given XML and run stats on it
# not sure where the final errors are

import xml.etree.ElementTree as ET
import re


stops = input().strip().split(';')
index = sorted(input().strip().split(';'))


xml = []

while True:
    try:
        xml.append(input().strip())
    except:
        break

root = ET.fromstring('<A>A ' + ' '.join(xml) + '</A>')

scores = {item:0 for item in index}

special = {'title': 5, 'abstract': 3, 'body': 1 }


L = 0
def dfs(node, score):
    
    
    if node.tag in special:
        score = special[node.tag]
    
    
    if node.text:
        for word in re.sub(r'[,.!\?]','', node.text).split():
            word = word.lower()
            if len(word) < 4: continue
            if word in stops: continue
            if score != 0:
                global L
                L += 1
                if word in scores:
                    scores[word] += score
    
    try:
        list(node)
    except:
        return
    
    for child in node:
        dfs(child, score)
        
dfs(root, 0)

thing = sorted(scores.items())

best = sorted(thing, key = lambda x: -x[1])

out = 0
last = 0
for k, v in best:
    if v == 0: break
    if v != last and out > 2: break
    print(f'{k}: {100 * (v / L)}')
    
    out += 1
    last = v