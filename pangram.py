alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
isPangram = "The quick brown fox jumps over the lazy dog"
liste = list(isPangram.lower())
ok = True
print(liste)
for i in alphabet:
    if ok:
        if i not in liste:
           ok = False
           break
if ok:
    print(f"{isPangram} is a PANGRAM")
else:
    print(f"{isPangram} is not a PANGRAM")
