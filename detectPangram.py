import string

# set is a collection of unique elements
alphabet=string.ascii_lowercase

def checkPangram(pangram):
    for letter in alphabet:
        if letter not in pangram.lower():
            return False
    return True

with open('data/pangrams.txt', 'r') as f:
    for line in f:
        pangram=line.strip()
        for character in string.punctuation:
            pangram = pangram.replace(character, '')
        print(pangram+": ")
        if (checkPangram(pangram) == True):
            print("yes\n")
        else:
            print("no\n")
    f.close()
