word = input('give your word please !!!')
vowel = ['a','e','i','o','u','y']
consonant = ['b' ,'c' ,'d' ,'f' ,'g' ,'h' ,'j' , 'k' ,'l' , 'm' , 'n' , 'p' , 'q' ,'r' ,'s' ,'t' ,'v' ,'w','x','z' ]
if word[0] in vowel:
    word = word +'ay'
    print(word)

elif word[0] in consonant:
    word = word[1:] + word[0] + 'ay'
    print(word)
