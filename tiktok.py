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
# Adat betöltése
df = pd.read_csv("tiktok_dataset.csv", sep=",")

# Like/View arány számítása
df['like_view_ratio'] = df['video_like_count'] / df['video_view_count']

# Claim és opinion videók szűrése
claim_videos = df[df['claim_status'] == 'claim']
opinion_videos = df[df['claim_status'] == 'opinion']


# Számosság
claim_count = len(claim_videos)
opinion_count = len(opinion_videos)

#claim statisztikák
claim_stats = {
    'átlag': claim_videos['like_view_ratio'].mean(),
    'medián': claim_videos['like_view_ratio'].median(),
    'szórás': claim_videos['like_view_ratio'].std()
}

#opinion statisztikák
opinion_stats = {
    'átlag': opinion_videos['like_view_ratio'].mean(),
    'medián': opinion_videos['like_view_ratio'].median(),
    'szórás': opinion_videos['like_view_ratio'].std()
}

#kiírás
print("Claim videók száma:", claim_count)
print("Opinion videók száma:", opinion_count)
print("Claim statisztikák:", claim_stats)
print("Opinion statisztikák:", opinion_stats)

#Megosztó videók keresése
global_mean = df['like_view_ratio'].mean()
global_std = df['like_view_ratio'].std()
threshold = global_mean - global_std
high_view_threshold = df['video_view_count'].quantile(0.75)

divisive_videos = df[
    (df['video_view_count'] >= high_view_threshold) &
    (df['like_view_ratio'] < threshold)
]

divisive_count = len(divisive_videos)
total_count = len(df)
divisive_sample = divisive_videos[['video_id', 'video_view_count', 'video_like_count', 'like_view_ratio']].head(5)

#kiírás
print("Megosztó videók száma:", divisive_count)
print("Összes videó száma:", total_count)
print("Példák megosztó videókra:\n", divisive_sample)