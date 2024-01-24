def first_n_lowercase_letters(n):
    alphabet_fiesta = {
        'a': "apple",
        'b': "banana",
        'c': "cherry",
        'd': "donut",
        'e': "elephant",
        'f': "flamingo",
        'g': "grape",
        'h': "hedgehog",
        'i': "ice cream",
        'j': "jellyfish" 

    }

    return [alphabet_fiesta[word] for word in sorted(alphabet_fiesta.keys())[:n]]
    # return sorted(alphabet_fiesta.keys())[:n]

result = first_n_lowercase_letters(5)
print(result)