# Node Classification Classical Dataset


dataset:  'cora', 'citeseer','pubmed','chameleon','squirrel','film','cornell','texas','wisconsin',

split_index: '0','1','2','3','4','5','6','7','8','9'

Related papers:

https://arxiv.org/abs/2002.05287

https://arxiv.org/pdf/2105.07634v1.pdf

https://arxiv.org/pdf/2109.05641v1.pdf



Kind note: if you run GCN/GAT/....  message passing algorithems on `chameleon` and `squirrel`, using `flow: str ='target_to_source'` instead of `flow: str ='source_to_target'` will help a lot.