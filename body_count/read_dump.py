import pandas as pd
from io import StringIO
import re

def read_dump(dump_filename, target_table):
    sio = StringIO()
        
    fast_forward = True
    with open(dump_filename, 'rb') as f:
        for line in f:
            line = line.strip()
            if line.lower().startswith('insert') and target_table in line:
                fast_forward = False
            if fast_forward:
                continue
            data = re.findall('\([^\)]*\)', line)
            try:
                newline = data[0]
                newline = newline.strip(' ()')
                newline = newline.replace('`', '')
                sio.write(newline)
                sio.write("\n")
            except IndexError:
                pass
            if line.endswith(';'):
                break
    sio.pos = 0
    return sio

food_min_filedata = read_dump('demonne.sql', 'customers')

df_food_min = pd.read_csv(food_min_filedata)


