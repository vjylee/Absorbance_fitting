import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors 
import pandas as pd
from tkinter import Tk, filedialog
import os


#selecting file
root = Tk()
root.withdraw()
file_path = filedialog.askopenfilename(
    title="select your file",
    filetypes=[("Excel files", "*.xlsx *.xls"),
               ("CSV files", "*.csv"),
               ("All files", "*.*")]
)

if not file_path:
    print("No file selected.")
    exit()

#reading files
ext = os.path.splitext(file_path)[1].lower()
if ext in ['.xlsx', '.xls']:
    df = pd.read_excel(file_path)
elif ext == '.csv':
    df = pd.read_csv(file_path)
else:
    print("Unsupported file format.")
    exit()

df = df.apply(pd.to_numeric, errors="coerce")

num_cols = df.shape[1]

cmap = plt.cm.Blues
norm = mcolors.Normalize(vmin=0, vmax=(num_cols // 2) -1)
plt.figure(figsize=(10, 6))
for i in range(0, num_cols, 2):
    if i+1 < num_cols:  # 짝수 열이 있는 경우에만
        x = df.iloc[:, i]
        y = df.iloc[:, i+1]
        mask = x.notna() & y.notna()
        if mask.any():
            color = cmap(norm(i))
            label = f"{df.columns[i]} vs {df.columns[i+1]}"
            plt.plot(x[mask], y[mask], linestyle='solid', color=color, linewidth=1, label=label)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("overlap")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()