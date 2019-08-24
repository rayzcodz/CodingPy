# Count a number of vowels and consonants in a String?
vowels = ['a', 'e', 'o', 'u', 'i']  # everything else is consonant

# given
string = 'Python is fun'
vowel_counter = 0
consonant_counter = 0

for c in string:
    if c in vowels:
        vowel_counter += 1
    else:
        consonant_counter += 1

print('Number of vowels = {} \nNumber of consonats = {}'.format(vowel_counter, consonant_counter))
