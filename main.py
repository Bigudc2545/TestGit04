def reduce_to_20_chars(original_string):
    if len(original_string) > 20:
        return original_string[:20]
    else:
        return original_string

def convert_to_original(reduced_string, original_string):
    if len(reduced_string) <= 20:
        padding = 20 - len(reduced_string)
        return reduced_string + original_string[-padding:]
    else:
        return reduced_string

def custom_substitution(input_string):
    substitution = {
        'aa': 'A',
        'ab': 'B',
        'ac': 'C',
        'ad': 'D',
        'ba': 'E',
        'bb': 'F',
        'bc': 'G',
        'bd': 'H',
        'ca': 'I',
        'cb': 'J',
        'cc': 'K',
        'cd': 'L',
        'da': 'M',
        'db': 'N',
        'dc': 'O',
        'dd': 'P',
    }

    for pattern, substitution in substitution.items():
        input_string = input_string.replace(pattern, substitution)

    return input_string

original_str = "aa, ab, ac"
reduced_str = reduce_to_20_chars(original_str)
print("reduced string:", reduced_str)

substituted_str = custom_substitution(reduced_str)
print("Substituted String:", substituted_str)

restored_str = convert_to_original(substituted_str, original_str)
print("Restored Original String:", restored_str)