def single_root_words(root_word, *other_words ):
    if not other_words:
        return []

    if type(root_word) is not str:
        return []

    same_words = []

    for word in other_words:
        if type(word) is not str:
            continue

        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
