#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

sentence = input("Enter sentence: ")
word_ = sentence.split()
vowel_ = 0
vowel_list =['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

for i in word_:
    sentence_ = sentence_ + len(word_)
for j in sentence:
    if j in vowel_list:
        vowel_ = vowel_+1
