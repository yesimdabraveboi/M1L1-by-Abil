meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH ": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO": "untuk menjadi agresif/marah",
            "GYATT": "Expresi ketika melihat sesuatu yang mengejutkan",
            "RIZZ": "Karisma atau kemampuan untuk menarik perhatian secara romantis"
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print (meme_dict[word])
    # Apa yang harus kita lakukan jika kata itu ditemukan?
else:
    print("Maaf, kata tersebut tidak ada di kamus")
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
