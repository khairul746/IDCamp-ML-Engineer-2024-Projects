import csv
from google_play_scraper import reviews, Sort

# Mengakses ulasan dan informasi aplikasi dari Google Play Store.
scrapreview, continuation_token = reviews(
    'com.shopee.id',    # ID aplikasi
    lang='en',                 # Bahasa ulasan (default: 'en')
    country='id',              # Negara (default: 'us')
    sort=Sort.MOST_RELEVANT,   # Urutan ulasan (default: Sort.MOST_RELEVANT)
    count=3000,               # Jumlah maksimum ulasan yang ingin diambil
)

# Menyimpan data ke dalam file CSV
with open('app_reviews.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)

    # Menulis header (nama kolom)
    writer.writerow(scrapreview[0].keys())  # Mengambil nama kolom dari data

    # Menulis setiap baris data
    for review in scrapreview:
        writer.writerow(review.values())
