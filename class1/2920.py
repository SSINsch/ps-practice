list_nodes = list(map(int, input().split()))

if list_nodes == sorted(list_nodes):
    print('ascending')
elif list_nodes == sorted(list_nodes, reverse=True):
    print('descending')
else:
    print('mixed')