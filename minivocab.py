"""
mini-vocab v0 — Basitlestirilmis implementasyon
Ogrenci: Elif Hazar(251478082)

Kapsam: Sadece init ve add komutlari.
Sinirlamalar: Dongu ve liste henuz kullanilmadi.
  - list komutu sadece dosya icerigini yazdiriyor (formatsiz)
  - learn/delete henuz implemente edilmedi
"""
import sys
import os

def initialize():
    """minivocab dizini ve bos words.dat dosyasini olusturur."""
    if os.path.exists(".minivocab"):
        return "Already initialized"
    
    os.mkdir(".minivocab")
    f = open(".minivocab/words.dat", "w")
    f.close()
    return "Initialized empty minivocab in .minivocab/"

def add_word(word, translation):
    """Yeni kelime ekler. ID tespiti dongusuz, dosyadaki satir sayisi ile yapilir."""
    if not os.path.exists(".minivocab"):
        return "Not initialized. Run: python minivocab.py init"
    
    # Dosyayi okuma modunda acip icerigi aliyoruz
    f = open(".minivocab/words.dat", "r")
    content = f.read()
    f.close()
    
    # Basit ID hesabi: dosyadaki satir (enter) sayisi + 1
    word_id = content.count("\n") + 1
    
    # Dosyayi ekleme (append) modunda aciyoruz
    f = open(".minivocab/words.dat", "a")
    f.write(str(word_id) + "|" + word + "|" + translation + "|LEARNING\n")
    f.close()
    
    return "Added word #" + str(word_id) + ": " + word + " - " + translation

def show_not_implemented(command_name):
    """Henuz kodlanmamis komutlar icin bilgi mesaji dondurur."""
    return "Command '" + command_name + "' will be implemented in future weeks."

# --- Ana Program ---
# Not: sys.argv sistem tarafindan verilen argumanlardir. 
# Yeni bir liste olusturulmamis, sadece arguman sayisina gore if-else yapilmistir.

if len(sys.argv) < 2:
    print("Usage: python minivocab.py <command> [args]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 4:
        print("Usage: python minivocab.py add <word> <translation>")
    else:
        print(add_word(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == "list":
    print(show_not_implemented("list"))
elif sys.argv[1] == "learn":
    print(show_not_implemented("learn"))
elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))
else:
    print("Unknown command: " + sys.argv[1])