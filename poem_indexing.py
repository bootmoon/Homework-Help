stopWords = [ "a", "i", "it", "am", "at", "on", "or", "in", "of", \
              "to", "is", "so", "too", "my", \
              "the", "and", "but", "are", "very", "here", "from", \
              "them", "then", "they", "than", "this", "that", \
              "though", "why", "yet", "has" ] 

noStemWords = [ "feed", "mass", "make", "rest", "ring", \
                "thing", "walrus", "wing", "wish" ]

endings = [ "s", "es", "ed", "est", "ish", "ing", "ly" ]

punctuation = [".",",",":",";","!","?","&","'","-"]

file = open("input.txt", "r")
lines = file.readlines()
file.close()

def remove_punctuation_and_lowercase(line, punctuation): #function that takes a line and removes punctuation and lowercases everything
    new_line = ""
    for char in line:
        if char not in punctuation:
            new_line += char.lower()
    return new_line
    
def remove_words(line, stopWords): #function that takes a line and removes all stopWords from it
    words = [word for word in line.split() if word not in stopWords]
    return words    

def stem(word, endings, noStemWords): #function that stems a word
    for i in range(3): #repeats the process 3 times (this assumes no word needs to be stemmed more than 3 times)
        if word not in noStemWords:
            last_char = word[-1:]
            last_two_chars = word[-2:]
            last_three_chars = word[-3:]
            
            if last_three_chars in endings:
                word = word[:-3]
            elif last_two_chars in endings:
                word = word[:-2]
            elif last_char in endings:
                word = word[:-1]
    return word

#create a 2d array of the format [['word1 in line1', 'word2 in line 1', 'word3 in line1', ...], ['word1 in line 2', 'word2 in line 2', ...],['word1 in line3', ...]]
new_lines = []
for line in lines:
    new_line = []
    updated_line = remove_words(remove_punctuation_and_lowercase(line, punctuation), stopWords)
    for word in updated_line:
        new_line.append(stem(word, endings, noStemWords))
    new_lines.append(new_line)
    new_lines = [x for x in new_lines if x != []] #remove empty lines (space between stanzas)

#create a dictionary with each instance of a word as a key and the line numbers on which it appears as values associated with the key
index = {}
for line_number, line in enumerate(new_lines, start = 1):
    for word in line:
        if word not in index: #if a word is not in the dict yet, add it and a list containing its line number
            index[word] = [line_number]
        elif word in index: #if a word is already in the dict, add line_number of current instance of word to the list of line numbers and update dict
            new_index = index[word]
            new_index.append(line_number)
            index[word] = new_index

print(index)

    

    






