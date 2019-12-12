import json

children = {}
with open('RC_2015-01', 'r') as r:
	for l in r:
		d = json.loads(l)
		if d['edited'] or d['author'] == '[deleted]' or d['body'] == '[deleted]':
			continue
		if d['name'] not in children:
			children[d['name']] = (None, None)
		if d['parent_id'] not in children:
			children[d['parent_id']] = (None, None)
		children[d['parent_id']] = max((d['score'], d['name']), children[d['parent_id']])

with open('RC_2015-01_ids', 'w') as w:
	for p in children:
		if p[:3] == 't3_':
			w.write('<|startoftext|>\n' + p + '\n')
			c = children[p][1]
			while c in children:
				w.write(c + '\n')
				c = children[c][1]
			w.write('<|endoftext|>\n')
