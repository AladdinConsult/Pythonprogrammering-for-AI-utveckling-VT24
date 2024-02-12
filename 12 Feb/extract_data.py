

ITERATTION = 1000

with open('./12 Feb/data/Pet_Supplies.json', 'r') as in_file:
    with open (f'./12 Feb/data/Pet_Supplies_{ITERATTION}.json', 'w') as out_file:
        for _ in range(ITERATTION):
            line = in_file.readline() 
            out_file.write(line)