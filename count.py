a="jayakrishna "
count_char={}
for i in a:
    if i in count_char:
        count_char[i] += 1
    else:
        count_char[i] = 1
print("Count of all characters \n "+ str(count_char))

max_char = max(count_char, key=count_char.get)
print(max_char)

min_char = min(count_char, key=count_char.get)
print(min_char)




def reverseWordSentence(Sentence):
 
    # Splitting the Sentence into list of words.
    words = Sentence.split(" ")
     
    # Reversing each word and creating
    # a new list of words
    # List Comprehension Technique
    newWords = [word[::-1] for word in words]
     
    # Joining the new list of words
    # to for a new Sentence
    newSentence = " ".join(newWords)
 
    return newSentence
 
# Driver's Code 
Sentence = "This is jk"
# Calling the reverseWordSentence 
# Function to get the newSentence
print(reverseWordSentence(Sentence))
