def xTree(datas):

    lists=[]

    tree={}

    parent_id=''

    for i in datas:

        item=i

        tree[item['id']]=item

    root=None

    for i in datas:

        obj=i

        if not obj['bid']:

            root=tree[obj['id']]

            lists.append(root)

        else:

            parent_id=obj['bid']

            if 'children' not in tree[parent_id]:   

                tree[parent_id]['children']=[]

            tree[parent_id]['children'].append(tree[obj['id']])

    return lists

print(xTree(data))
