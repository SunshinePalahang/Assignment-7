#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

sentence = input("Enter sentence: ")
sentence_ = sentence.split()
vowel_ = 0
vowel_list =['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
consonant_ = 0

for i in sentence_:
    word_ =+len(sentence_)
for j in sentence:
    if j in vowel_list:
        vowel_ = vowel_+1
    else:
        consonant_ =  consonant_+1
print("Output:""\nWords: ",word_, "\nVowels: ",vowel_, "\nConsonant: ", consonant_ )
