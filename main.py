meme_dict = {

            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": "Bir şakaya karşılık cevap",
            "SHEESH": "Onaylamamak",
            "CREEPY": "Korkunç",
            "AGGRO": "Agresifleşmek/Sinirlenmek",
            }

while True:
    print("--------------------------------------------------------------------------")
    word = input("Anlamadığınız bir kelimeyi yazın Hepsi Büyük Harfle.")
    print("--------------------------------------------------------------------------")
    if word in meme_dict.keys():
        print(meme_dict.values())
    else:
        print("Bu Kelime Sözlükte Mevcut Değil")
