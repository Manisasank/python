import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df = sns.load_dataset("anscombe") #x,y,datasets
print(df.head())
print(df.tail())
print(df.shape())
print(df.size())
print(len(df))