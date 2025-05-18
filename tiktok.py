import pandas as pd
import numpy as np

### Adatfeldolgozás ###

#Adatok beolvasása
data = pd.read_csv("tiktok_dataset.csv", sep=",")
print(data.head)

#Adatmezők és típusaik kiíratása
print("Adatmezők és típusaik:")
print(data.dtypes)

#Felesleges oszlopok kiszűrése
data.drop(columns=["#", "video_id", "video_transcription_text",
                   "verified_status", "author_ban_status"], inplace=True)

#Hiányzó adatok kezelése
missing_values = data.isnull().sum()
print("\nHiányzó értékek oszloponként:")
print(missing_values)
#Ahol a claim_status hiányzik, ott a többi érték is, ezeket töröljük
data=data.dropna()

#Duplikált sorok ellenőrzése és eltávolítása
data = data.drop_duplicates()

### Adatok vizsgálata ###

#Alapstatisztikák kiszámítása: videóhossz, nézettség, like
duration_stats = data["video_duration_sec"].agg(['mean', 'median', 'std'])
print("Videóhossz statisztikák:")
print(duration_stats)

# Like/View arány számítása
data['like_view_ratio'] = data['video_like_count'] / data['video_view_count']

# Claim és opinion videók szűrése
claim_videos = data[data['claim_status'] == 'claim']
opinion_videos = data[data['claim_status'] == 'opinion']

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
global_mean = data['like_view_ratio'].mean()
global_std = data['like_view_ratio'].std()
threshold = global_mean - global_std
high_view_threshold = data['video_view_count'].quantile(0.75)

divisive_videos = data[
    (data['video_view_count'] >= high_view_threshold) &
    (data['like_view_ratio'] < threshold)
]

divisive_count = len(divisive_videos)
total_count = len(data)
divisive_sample = divisive_videos[['video_view_count', 'video_like_count', 'like_view_ratio']].head(5)

#kiírás
print("Megosztó videók száma:", divisive_count)
print("Összes videó száma:", total_count)
print("Példák megosztó videókra:\n", divisive_sample)

### Modellezés ###

#Korrelációs mátrix
# Csak az érdekes oszlopok
correlation = data[['video_duration_sec', 'video_view_count', 'video_like_count', 'video_comment_count']].corr()

# Külön a hossz és a népszerűségi mutatók közötti korreláció
duration_corr = correlation.loc['video_duration_sec']

print(duration_corr)

#Sűrűségtérkép
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.hexbin(data['video_duration_sec'], data['video_view_count'],
           gridsize=50, cmap='viridis', bins='log')
plt.xlabel('Videó hossza (mp)')
plt.ylabel('Nézettség')
plt.title('Videóhossz vs. Nézettség (Hexbin térkép)')
plt.colorbar(label='Pontok száma (log)')
plt.yscale('log')
plt.show()

#Regresszió a hossz és a megtekintések száma közötti kapcsolat vizsgálatára
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Jellemzők és célváltozó
X = data[['video_duration_sec']]
y = data['video_view_count']

# Tanító és teszt halmaz
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modell létrehozása
model = LinearRegression()
model.fit(X_train, y_train)

# Modell értékelése
r_squared = model.score(X_test, y_test)
print(f"R² érték (magyarázott variancia): {r_squared:.4f}")

from sklearn.metrics import r2_score

# Célváltozók listája
targets = ['video_like_count', 'video_share_count', 'video_download_count', 'video_comment_count']

# Független változó: videó hossza
X = data[['video_duration_sec']]

# Eredmények tárolása
results = {}

for target in targets:
    y = data[target]

    # Oszd fel az adatokat tanító és teszt adathalmazra
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Modell betanítása
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Előrejelzés
    y_pred = model.predict(X_test)

    # R² érték kiszámítása
    r2 = r2_score(y_test, y_pred)

    # Eredmény eltárolása
    results[target] = round(r2, 4)

# Eredmények kiírása
for target, r2 in results.items():
    print(f"{target}: R² = {r2}")





