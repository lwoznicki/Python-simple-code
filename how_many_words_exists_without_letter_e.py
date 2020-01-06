fin = open('words.txt')

NUMBER_OF_WORDS_IN_DICTIONARY = 113809.0

def find_words_without_letter_e(word):
    for char in word:
        if char in 'eE':
            return False
    return True  

counter = 0
for line in fin:
    word = line.strip()
    if find_words_without_letter_e(word):
        counter += 1
        print (word)

percent = (counter / NUMBER_OF_WORDS_IN_DICTIONARY) * 100

print str(percent) + "% of the words without a letter 'e'."