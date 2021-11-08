plain = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
cipher = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'] 

def decoding_atbash_cipher (code):
    decodind = ' '
    for i in code:
        if i == ' ':
            decodind += ' '
        else:
            decodind += cipher[plain.index(i)] 

    print(f"{decodind}")        

def encoding_atbash_cipher (sentence):
    coding = ' '
    for i in sentence:
        if i == ' ':
            coding += ' '
        else:
            coding += plain[cipher.index(i)] 

    print(f"{coding}")        
    
encoding_atbash_cipher('the quick brown fox jumps over the lazy dog')
decoding_atbash_cipher('gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt')