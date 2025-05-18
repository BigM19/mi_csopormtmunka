import pandas as pd
import numpy as np

#Adatok beolvasása
data = pd.read_csv("tiktok_dataset.csv", sep=",")
print(data.head)

#Adatmezők és típusaik kiíratása
print("Adatmezők és típusaik:")
print(data.dtypes)

#Felesleges oszlopok kiszűrése
data.drop(columns=["#", "video_id", "video_transcription_text"], inplace=True)

#Hiányzó adatok kezelése
missing_values = data.isnull().sum()
print("\nHiányzó értékek oszloponként:")
print(missing_values)
#Ahol a claim_status hiányzik, ott a többi érték is, ezeket töröljük
data=data.dropna()

#Duplikált sorok ellenőrzése és eltávolítása
data = data.drop_duplicates()

#Alapstatisztikák kiszámítása: videóhossz, nézettség, like
duration_stats = data["video_duration_sec"].agg(['mean', 'median', 'std'])
print("Videóhossz statisztikák:")
print(duration_stats)

#Repository cloned