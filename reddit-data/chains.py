import json

chains = []
curr = []
with open('RC_2015-01_ids', 'r') as r:
	for l in r:
		if l.strip() == '<|startoftext|>' or l.strip()[:3] == 't3_':
			continue
		elif l.strip() == '<|endoftext|>':
			chains.append(curr)
			curr = []
		else:
			curr.append(l.strip())

chains = [c for c in chains if len(c) >= 5]
print(len(chains))
print(sum(len(c) for c in chains))
indices = {}
for i, c in enumerate(chains):
	for j, id in enumerate(c):
		indices[id] = (i, j)
remaining = [len(c) for c in chains]
trained = 0
split = int(len(chains) * 0.7)
subreddits = set()

with open('RC_2015-01', 'r') as r:
	with open('RC_2015-01_train.txt', 'w') as train:
		with open('RC_2015-01_test.txt', 'w') as test:
			for l in r:
				d = json.loads(l)
				if d['name'] in indices:
					i, j = indices[d['name']]
					chains[i][j] = d
					remaining[i] -= 1
					if remaining[i] == 0:
						subreddits.add(d['subreddit'])
						if trained <= split:
							train.write('<|startoftext|>\n')
							train.write('\n\n'.join(e['subreddit'] + '/' + e['author'] + ': ' + e['body'] for e in chains[i]).encode('utf-8'))
							train.write('\n<|endoftext|>\n')
							trained += 1
						else:
							test.write('<|startoftext|>\n')
							test.write('\n\n'.join(e['subreddit'] + '/' + e['author'] + ': ' + e['body'] for e in chains[i]).encode('utf-8'))
							test.write('\n<|endoftext|>\n')
						chains[i] = None

print(len(subreddits))