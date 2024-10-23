databases = []

def sync_the_file():
    try:
        with open("database.txt", "r") as file:
            for datas in file:
                isi = datas.strip().split("~")
                database = {}
                database["band"] = isi[0]
                database["judul"] = isi[1]
                database["panjang lagu"] = isi[2]
                database["bahasa"] = isi[3]
                database["Genre"] = isi[4]
                database["Rilis"] = isi[5]
                databases.append(database)
            print("print file telah di simpan /n")
    except FileNotFoundError:
        print("Sepertinya Anda Memilih Berkas yang Salah, Coba Baca Dengan Baik... Otak Burung....\n")
    except IndexError:
        print("Daftar hanya memiliki 6 hal mengapa Anda meletakkan lebih atau kurang di atas meja?\n")

def view_the_database():
    for data in databases:
        print(f"\n{data['band']} - {data['title']}")
        print(f"\t\tDurasi : {data['length_song']}")
        print(f"\t\tBahasa : {data['language']}")
        print(f"\t\tGenre : {data['Genre']}")
        print(f"\t\tTahun Rilis : {data['Release']}\n")

def song_statistics():
    with open("database.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            for data in databases:
                if line == int(data['title']):
                    print(f"{lines['band']} Memiliki {line}")

# Additional functions
def number_of_songs_by_band():
    band_counts = {}
    for data in databases:
        band = data['band']
        band_counts[band] = band_counts.get(band, 0) + 1
    for band, count in band_counts.items():
        print(f"{band} memiliki {count} lagu")

def longest_song_duration():
    durations = [int(data['length_song']) for data in databases]
    max_duration = max(durations)
    print(f"Durasi lagu terpanjang adalah {max_duration} menit")

def most_common_genre():
    genres = [data['Genre'] for data in databases]
    most_common_genre = max(set(genres), key=genres.count)
    genre_count = genres.count(most_common_genre)
    print(f"Genre dengan lagu terbanyak adalah {most_common_genre} dengan total {genre_count} lagu")

def most_common_language():
    languages = [data['language'] for data in databases]
    most_common_language = max(set(languages), key=languages.count)
    language_count = languages.count(most_common_language)
    print(f"Bahasa dengan lagu terbanyak adalah {most_common_language} dengan total {language_count} lagu")

def most_common_year():
    years = [data['Release'] for data in databases]
    most_common_year = max(set(years), key=years.count)
    year_count = years.count(most_common_year)
    print(f"Tahun dengan lagu terbanyak adalah {most_common_year} dengan total {year_count} lagu")

while typing != 0:
    try:
        print("1. Sinkronisasi Berkas ke Database Python")
        print("2. Lihat Database Lagu")
        print("3. Statistik Lagu")
        print("0. Keluar")
        typing = int(input("\nPILIH KARAKTERMU!!.. Paham? : "))

        if typing == 1:
            sync_the_file()
        elif typing == 2:
            view_the_database()
        elif typing == 3:
            song_statistics()
        elif typing == 4:
            number_of_songs_by_band()
        elif typing == 5:
            longest_song_duration()
        elif typing == 6:
            most_common_genre()
        elif typing == 7:
            most_common_language()
        elif typing == 8:
            most_common_year()
        elif typing == 0:
            print("Terima kasih, Pergi berlari bersama teman-teman laki-laki Anda")
    except ValueError:
        print("\nJangan Menempatkan Kata di Menu, Itu kotor... Letakkan Angka di Menu")