# This is a Python script.
# You can save code and comments in a script, but you can't use it 
# to compose your narrative and render to a report containing 
# narrative, code, and output.

2 + 2

x = 2

import pandas as pd
from palmerpenguins import load_penguins

penguins = load_penguins()

print(penguins.head())

penguins['body_mass_g']

penguins['body_mass_g'].mean()

help(pd.Series.mean)

penguins['body_mass_g'].mean(skipna=True)
