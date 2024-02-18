with open("C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\MadlibsGenerator\\story.txt","r") as f:
    story = f.read()

words = set() #uses a set to only contain unique elements
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):# enumerate gives access to both, the position and the element
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

#print(words)

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
    
#print(answers)

for word in words:
    story = story.replace(word, answers[word])
    
print(story)
