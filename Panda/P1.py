import pandas as pd
data = {'Name': ['Rashmi', 'Krishna', 'Aman', 'Toothless'],
        'Age': [22, 1000, 23, 24],
        'City': ['Kolkata', 'Dwarka','Mumbai', 'Kolkata']
        }

df = pd.DataFrame(data)
print(df)