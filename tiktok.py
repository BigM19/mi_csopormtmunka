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

# 7. Dátum/id mezők konvertálása (nincs ilyen mező most, megemlítjük)
# (Ebben az adatban nincs dátum mező, ezt dokumentáljuk.)
pass

# 8. Alapstatisztikák kiszámítása: videóhossz, nézettség, like
duration_stats = df_clean["video_duration_sec"].agg(['mean', 'median', 'std'])
print("Videóhossz statisztikák:")
print(duration_stats)

# 9. Claim vs Opinion szűrés és statisztika
grouped = df_clean[df_clean["claim_status"].isin(["claim", "opinion"])]
claim_stats = grouped.groupby("claim_status")[["video_view_count", "video_like_count"]].agg(['count', 'mean', 'median', 'std'])
print("Claim vs Opinion statisztikák:")
print(claim_stats)