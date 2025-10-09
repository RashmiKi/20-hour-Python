import pandas as pd

data = {'Name': ['Rashmi', 'Krishna', 'Aman', 'Toothless'],
        'Age': [22, 1000, 23, 24],
        'City': ['Kolkata', 'Dwarka','Mumbai', 'Kolkata']
        }

df = pd.DataFrame(data)


df.to_csv('output.csv')
df.to_csv('output_no_index_header.csv', index=False)