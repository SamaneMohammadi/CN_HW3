filename=("u.data","r")

from itertools import groupby

with open('u.data') as f_input, open('C:\Users\samaneh\Desktop\data.txt', 'w') as f_output:
    for k, g in groupby(f_input, lambda x: x != '\n'):
        if k:
            entries = [line.strip() for line in g]
            block_header = []
            entries = sorted([line.split() for line in entries[:]], key=lambda x: int(x[0]))
            f_output.write('\n'.join(block_header) + '\n')

            for row in entries:
                f_output.write(' '.join(row) + '\n')


