sentence = input("give your sentences  ")
words = sentence.split(' ')
unique = []
for word in words:
    count = words.count(word)
    print(f"{word} occurs {count} times in {sentence}")  
    
    
