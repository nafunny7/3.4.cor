def single_root_words(root_word, *other_words):
    same_words = []
    up = root_word.upper()
    for i in other_words:
        if up in i.upper() or i.upper() in up:
            same_words.append(i)
    return same_words


print(single_root_words("miCrO", "micrOfOn", "tOAster", "mIcrobe", "laZy", "MiCrobe", "mAcro", "microScope", "mInI"))

