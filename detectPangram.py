import string

# set is a collection of unique elements
letters=set(string.ascii_lowercase)

with open('data/pangrams.txt', 'r') as f:
    for line in f:
        pangram=line.strip()
        for character in string.punctuation:
            pangram = pangram.replace(character, '')
    
        print(pangram)
    f.close()
