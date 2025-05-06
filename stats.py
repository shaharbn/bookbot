def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    characters = {}
    for ch in text:
        if ch.lower() in characters:
            characters[ch.lower()] += 1
        else:
            characters[ch.lower()] = 1
    return characters

def sort_on(d):
    return d["num"]

def sort_dict(d):
    convert = []
    for k in d:
        convert.append({"name": k, "num": d[k]})
    convert.sort(reverse=True, key=sort_on)
    return convert