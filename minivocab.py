"""
mini-vocab v2 — Search, Delete ve Stats eklendi
Ogrenci: Elif Hazar (251478082)

V2 GÖREVLERİ (TASKS):
1. 'search' komutu ile dosya icinde kelime arama ozelligini eklemek.
2. 'delete' komutunu dongu ile dosyadan satir silinecek sekilde kodlamak.
3. 'stats' komutu ile ogrenilen/ogrenilmeyen kelime sayilarini gostermek.
"""
import sys
import os

def initialize():
    if os.path.exists(".minivocab"):
        return "Already initialized"
    os.mkdir(".minivocab")
    f = open(".minivocab/words.dat", "w")
    f.close()
    return "Initialized empty minivocab in .minivocab/"

def add_word(word, translation):
    if not os.path.exists(".minivocab"):
        return "Not initialized. Run: python minivocab.py init"
    
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    # ID uretimini guvenli hale getirdik (silinmelerde cakisma olmamasi icin)
    max_id = 0
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 4 and parts[0].isdigit():
            if int(parts[0]) > max_id:
                max_id = int(parts[0])
                
    new_id = max_id + 1
    
    f = open(".minivocab/words.dat", "a")
    f.write(str(new_id) + "|" + word + "|" + translation + "|LEARNING\n")
    f.close()
    return "Added word #" + str(new_id) + ": " + word + " - " + translation

def list_words():
    if not os.path.exists(".minivocab/words.dat"):
        return "No words found."
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    if len(lines) == 0:
        return "No words found."
    
    result = ""
    for line in lines:
        parts = line.strip().split("|")
        if len(parts) == 4:
            result += "[" + parts[0] + "] [" + parts[3] + "] " + parts[1] + " - " + parts[2] + "\n"
    return result.strip()

def search_word(query):
    if not os.path.exists(".minivocab/words.dat"):
        return "Not initialized."
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    result = ""
    for line in lines:
        if query.lower() in line.lower():
            parts = line.strip().split("|")
            if len(parts) == 4:
                result += "[" + parts[0] + "] [" + parts[3] + "] " + parts[1] + " - " + parts[2] + "\n"
                
    if result == "":
        return "Word not found."
    return result.strip()

def delete_word(word_id):
    if not os.path.exists(".minivocab/words.dat"):
        return "Not initialized."
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    found = False
    f = open(".minivocab/words.dat", "w")
    for line in lines:
        parts = line.strip().split("|")
        # Eger satir bizim silmek istedigimiz ID degilse, dosyaya geri yaz!
        if len(parts) == 4 and parts[0] != str(word_id):
            f.write(line)
        elif len(parts) == 4 and parts[0] == str(word_id):
            found = True
    f.close()
    
    if found:
        return "Deleted word #" + str(word_id) + "."
    else:
        return "Word #" + str(word_id) + " not found."

def show_stats():
    if not os.path.exists(".minivocab/words.dat"):
        return "Not initialized."
    f = open(".minivocab/words.dat", "r")
    lines = f.readlines()
    f.close()
    
    total = len(lines)
    learning = 0
    learned = 0
    for line in lines:
        if "LEARNING" in line:
            learning += 1
        elif "LEARNED" in line:
            learned += 1
            
    return "Total Words: " + str(total) + "\nLEARNING: " + str(learning) + "\nLEARNED: " + str(learned)

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
        if len(parts) == 4 and parts[0] == str(word_id):
            f.write(parts[0] + "|" + parts[1] + "|" + parts[2] + "|LEARNED\n")
            found = True
        else:
            f.write(line)
    f.close()
    if found:
        return "Word #" + str(word_id) + " marked as learned."
    else:
        return "Word #" + str(word_id) + " not found."

# --- Ana Program ---
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
    print(list_words())
elif sys.argv[1] == "search":
    if len(sys.argv) < 3:
        print("Usage: python minivocab.py search <word>")
    else:
        print(search_word(sys.argv[2]))
elif sys.argv[1] == "delete":
    if len(sys.argv) < 3:
        print("Usage: python minivocab.py delete <id>")
    else:
        print(delete_word(sys.argv[2]))
elif sys.argv[1] == "stats":
    print(show_stats())
elif sys.argv[1] == "learn":
     if len(sys.argv) < 3:
        print("Usage: python minivocab.py learn <id>")
     else:
        print(learn_word(sys.argv[2]))
else:
    print("Unknown command: " + sys.argv[1])