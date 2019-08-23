# check if two Strings are anagrams of each other? Ex. mary and army

namea = 'armwy'
nameb = 'mary'
anagrama = ''
anagramb = ''

if len(namea) != len(nameb):
    for a in namea:
        if a not in nameb:
            anagrama = 'No'
            break
    for b in nameb:
        if b not in namea:
            anagramb = 'No'
            break

    if anagrama == anagramb:
        print('{} and {} ara anagrams of each other'.format(namea, nameb))
    else:
        print('{} and {} ara not anagrams of each other'.format(namea, nameb))

else:
    print('{} and {} ara not anagrams of each other'.format(namea, nameb))
