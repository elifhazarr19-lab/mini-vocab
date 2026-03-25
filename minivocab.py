"""
mini-vocab v1 — Döngüler eklendi + Bonus Yapay Zeka Komutu
Ogrenci: Elif Haazar (251478082)
"""
import sys
import os

def initialize():
    if os.path.exists(".minivocab"):
        return "Zaten baslatildi (Already initialized)"
    os.mkdir(".minivocab")
    f = open(".minivocab/words.dat", "w")
    f.close()
    return "minivocab basariyla baslatildi."

def add_word(word, translation):
    if not os.path.exists(".minivocab"):
        return "HATA: Once projeyi baslatin. Komut: python minivocab.py init"
    f = open(".minivocab/words.dat", "r")
    content = f.read()
    f.close()
    word_id = content.count("\n") + 1
    f = open(".minivocab/words.dat", "a")
    f.write(str(word_id) + "|" + word + "|" + translation + "|LEARNING\n")
    f.close()
    return "Eklendi #" + str(word_id) + ": " + word + " - " + translation

def list_words():
    if not os.path.exists(".minivocab/words.dat"):
        return "Hic kelime bulunamadi."
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    if len(lines) == 0:
        return "Hic kelime bulunamadi."
    
    result = ""
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 4:
            result += "[" + parts[0] + "] [" + parts[3] + "] " + parts[1] + " - " + parts[2] + "\n"
    return result.strip()

# --- BONUS: YAPAY ZEKA ILE URETILEN FONKSIYON ---
def learn_word(word_id):
    if not os.path.exists(".minivocab/words.dat"):
        return "HATA: Dosya bulunamadi."
    
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    found = False
    f = open(".minivocab/words.dat", "w")
    for line in lines:
        parts = line.strip().split("|")
        # Eger satir bizim aradigimiz ID ise durumunu LEARNED yap
        if len(parts) == 4 and parts[0] == str(word_id):
            f.write(parts[0] + "|" + parts[1] + "|" + parts[2] + "|LEARNED\n")
            found = True
        else:
            f.write(line)
    f.close()
    
    if found:
        return "Kelime #" + str(word_id) + " 'LEARNED' (Ogrenildi) olarak isaretlendi."
    else:
        return "Kelime #" + str(word_id) + " bulunamadi."

def show_not_implemented(command_name):
    return "Bu komut (" + command_name + ") ileriki haftalarda eklenecektir."

# --- Ana Program ---
if len(sys.argv) < 2:
    print("HATA: Komut girmediniz! Kullanim: python minivocab.py <komut> [argumanlar]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 4:
        print("HATA: Eksik kelime. Kullanim: python minivocab.py add <kelime> <ceviri>")
    else:
        print(add_word(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "list":
    print(list_words())
elif sys.argv[1] == "learn": # BONUS KISMI BURAYA EKLENDI
    if len(sys.argv) < 3:
        print("HATA: ID girmediniz. Kullanim: python minivocab.py learn <id>")
    else:
        print(learn_word(sys.argv[2]))
elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))
else:
    print("Bilinmeyen komut: " + sys.argv[1])
