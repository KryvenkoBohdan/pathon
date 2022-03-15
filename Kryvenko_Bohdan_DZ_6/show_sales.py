from sys import argv

if  len(argv) == 2:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        content = f.read().split()
        i = argv[1]
        i = int(i) - 1
        while i < len(content):
            print(content[i])
            i += 1

elif len(argv) == 3:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        content = f.read().split()
        i = int(argv[1])-1
        j = int(argv[2])
        while i < j and len(content):
            print(content[i])
            i += 1