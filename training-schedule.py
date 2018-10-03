import pandas as pd
import numpy as np

print("This is Hal Higgon's Intermediate Half 2.")

cols = ['Cross','Easy Run','Tempo/Speedwork','Easy Run','Rest','Race Pace','Long Run']
data = np.array([['30 min cross','3 m run','5 x 400 5-K pace','3 m run','Rest','3 m run','5 m run'],
				['30 min cross','3 m run','30 min tempo','3 m run','Rest','3 m pace','6 m run'],
				['40 min cross','3.5 m run','6 x 400 5-K pace','3 m run','Rest','Rest','5-K Race'],
				['40 min cross','3.5 m run','35 min tempo','3 m run','Rest','3 m run','7 m run'],
				['40 min cross','4 m run','7 x 400 5-K pace','3 m run','Rest','3 m pace','8 m run'],
				['50 min cross','4 m run','40 min tempo','3 m run','Rest or easy run','Rest','10-K Race'],
				['Rest','4.5 m run','8 x 400 5-K pace','3 m run','Rest','4 m pace','9 m run'],
				['50 min cross','4.5 m run','40 min tempo','3 m run','Rest','5 m pace','10 m run'],
				['60 min cross','5 m run','9 x 400 5-K pace','3 m run','Rest or easy run','Rest','15-K Race'],
				['Rest','5 m run','45 min tempo','3 m run','Rest','5 m pace','11 m run'],
				['60 min cross','5 m run','10 x 400 5-K pace','3 m run','Rest','3 m pace','12 m run'],
				['Rest','4 m run','30 min tempo','2 m run','Rest','Rest','Half Marathon']])

df = pd.DataFrame(columns=cols, data=data)
df
