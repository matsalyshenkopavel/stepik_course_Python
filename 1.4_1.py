quantity = int(input())

def get(bd, nmsp, arg):
    if arg in bd[nmsp]['variables']:
        return nmsp
    if nmsp == 'global':
        return 'None'
    else:
        return get(bd, bd[nmsp]['parent'], arg)

bd = {'global': {'parent':'None', 'variables':[]}}
for _ in range(quantity):
    cmd, nmsp, arg = input().split()
    if cmd == 'create':
        bd[nmsp] = {'parent': arg, 'variables':[]}
    elif cmd == 'add':
        bd[nmsp]['variables'].append(arg)
    else:
        print(get(bd, nmsp, arg))