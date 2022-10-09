from process import full_load_data

#dataset:  'cora', 'citeseer','pubmed','chameleon','squirrel','film','cornell','texas','wisconsin',
#split_index: '0','1','2','3','4','5','6','7','8','9'
datastr = 'cora'
split_index=str(0)




splitstr = 'splits/'+datastr+'_split_0.6_0.2_'+split_index+'.npz'
g, features, labels, idx_train, idx_val, idx_test, num_features, num_labels = full_load_data(datastr,splitstr)


from torch_geometric.utils import add_self_loops,to_undirected,dense_to_sparse
A=g.toarray()
edge_index,_=dense_to_sparse(torch.tensor(A))
