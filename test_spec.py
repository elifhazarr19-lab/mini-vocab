"""
mini-vocab SPEC test senaryolari
Ogrenci: Elif Hazar (251478082)
Proje: mini-vocab
"""
import subprocess
import os
import shutil

# --- Yardimci Fonksiyon ---
def run_cmd(args):
    """Komutu calistir, stdout dondur."""
    result = subprocess.run(
        ["python", "minivocab.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    """Her testten once temiz baslangic."""
    if os.path.exists(".minivocab"):
        shutil.rmtree(".minivocab")

# --- init testleri ---
def test_init_creates_directory():
    output = run_cmd(["init"])
    assert os.path.exists(".minivocab"), ".minivocab dizini olusturulmali"
    assert os.path.exists(".minivocab/words.dat"), "words.dat dosyasi olusturulmali"

def test_init_already_exists():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output

# --- add testleri ---
def test_add_single_word():
    run_cmd(["init"])
    output = run_cmd(["add", "apple", "elma"])
    assert "Added word #1" in output
    assert "apple" in output

def test_add_missing_arguments():
    run_cmd(["init"])
    output = run_cmd(["add", "apple"])
    assert "Usage:" in output

# --- list testleri ---
def test_list_empty():
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "No words found" in output

def test_list_shows_words():
    run_cmd(["init"])
    run_cmd(["add", "apple", "elma"])
    output = run_cmd(["list"])
    assert "apple" in output
    assert "LEARNING" in output

# --- learn testleri ---
def test_learn_marks_word():
    run_cmd(["init"])
    run_cmd(["add", "apple", "elma"])
    output = run_cmd(["learn", "1"])
    assert "marked as learned" in output

def test_learn_nonexistent():
    run_cmd(["init"])
    output = run_cmd(["learn", "99"])
    assert "not found" in output

# --- delete testleri ---
def test_delete_removes_word():
    run_cmd(["init"])
    run_cmd(["add", "apple", "elma"])
    output = run_cmd(["delete", "1"])
    assert "Deleted" in output
    list_output = run_cmd(["list"])
    assert "apple" not in list_output

def test_delete_nonexistent():
    run_cmd(["init"])
    output = run_cmd(["delete", "99"])
    assert "not found" in output

# --- hata testleri ---
def test_command_before_init():
    output = run_cmd(["add", "apple", "elma"])
    assert "Not initialized" in output

def test_unknown_command():
    run_cmd(["init"])
    output = run_cmd(["fly"])
    assert "Unknown command" in output