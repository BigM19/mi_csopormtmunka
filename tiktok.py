import pandas as pd
import numpy as np

# 2. Adat betöltése
df = pd.read_csv("tiktok_dataset.csv")

# 3. Alapvető adatellenőrzés: fejléc és hiányzó értékek
print(df.info())
print(df.isnull().sum())

# 4. Duplikált sorok ellenőrzése és eltávolítása
df = df.drop_duplicates()