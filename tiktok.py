import pandas as pd
import numpy as np

# 2. Adat betöltése
df = pd.read_csv("tiktok_dataset.csv")

# 3. Alapvető adatellenőrzés: fejléc és hiányzó értékek
print(df.info())
print(df.isnull().sum())

# 4. Duplikált sorok ellenőrzése és eltávolítása
df = df.drop_duplicates()

# 5. Oszlopnevek ellenőrzése és átnevezés a könnyebb hivatkozásért
df.columns = df.columns.str.strip().str.lower()
df.rename(columns={"#": "index"}, inplace=True)

# 6. Hiányzó értékek kitöltése vagy törlése (konzervatív megközelítés: törlés)
df_clean = df.dropna(subset=["claim_status", "video_view_count", "video_like_count"])