import jenkspy
import pandas as pd

file_path = 'data.xlsx'
df = pd.read_excel(file_path)
breaks = jenkspy.jenks_breaks(df['Population'], n_classes=3)
print(breaks)