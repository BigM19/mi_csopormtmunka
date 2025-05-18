# Feladatleírás

A mellékelt adathalmaz TikTok videokkal kapcsolatos adatokat tartalmaz. Az oszlopok rövid leírás:

TikTok assigned number for video with claim/opinion.
claim_status - Whether the published video has been identified as an “opinion” or a “claim.” In this dataset, an “opinion” refers to an individual’s or group’s personal belief or thought. A “claim” refers to information that is either unsourced or from an unverified source.
video_id - Random identifying number assigned to video upon publication on TikTok.
video_duration_sec - How long the published video is measured in seconds.
video_transcription_text - Transcribed text of the words spoken in the published video.
verified_status	- Indicates the status of the TikTok user who published the video in terms of their verification, either “verified” or “not verified.”
author_ban_status - Indicates the status of the TikTok user who published the video in terms of their permissions: “active,” “under scrutiny,” or “banned.”
video_view_count - the total number of times the published video has been viewed.
video_like_count - the total number of times the published video has been liked by other users.
video_share_count - the total number of times the published video has been shared by other users.
video_download_count - the total number of times the published video has been downloaded by other users.
video_comment_count - the total number of comments on the published video.

Felelősségek lebontása:
- Adatfeldolgozás
- Modellezés
- Prototipizálás / teszelés

Főbb megválaszolandó kérdések:
- Mi a videók hosszának átlaga, mediánja, szórása?
- Ha külön nézzük a "claim" és az "opinion" típusú videókat, melyik halmaznak mekkora a számossága, és hogyan alakul az értékelésük átlaga, mediánja, szórása?
- Nevezzük azokat a videókat "megosztónak", melyeket sokan néztek meg de a like-ok száma ettől jelentős részben elmarad. Azonosítható-e a videóknak egy ilyen szűk köre, vagy az ilyesmi nem jellemző egyáltalán?
- Lehet-e összefüggés a videók hossza és népszerűsége között?
