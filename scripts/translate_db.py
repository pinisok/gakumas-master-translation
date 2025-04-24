import os
import json
import shutil

T_PATH = "./scripts/db.json"
T_DB = {}
LOAD = False

def load_db():
    if os.path.exists(T_PATH):
        with open(T_PATH, 'r', encoding='utf-8') as f:
            T_DB = json.load(f)
    LOAD = True

def save_db():
    with open(T_PATH, 'w', encoding='utf-8') as f:
        json.dump(T_DB, f, ensure_ascii=False, indent=4)

def _find_db(text, fn, key):
    if text in T_DB:
        for idx, obj in enumerate(T_DB[text]):
            if obj['masterdb'] == fn and obj['key'] == key:
                return idx
    return -1

def add_db(text, translate_text, filename, key):
    if not LOAD:
        load_db()
    if not text in T_DB:
        T_DB[text] = []
    idx = -1
    if filename != "" and key != "":
        idx = _find_db(text, filename, key)
    if idx == -1:
        T_DB[text].insert(0,{
            'translate':translate_text,
            'masterdb': filename,
            'key': key
        })
    else:
        T_DB[text][idx]['translate'] = translate_text

def has_db(text):
    return text in T_DB

def get_db(text, fn, key):
    if not LOAD:
        load_db()
    if not text in T_DB:
        return ""
    if filename != "" or key != "":
        return T_DB[text]["translate"]
    for obj in T_DB[text]:
        if obj['masterdb'] == filename and obj['key'] == key:
            return obj["translate"]
    return T_DB[text]["translate"]
