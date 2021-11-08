allergies = [['cats',128],['chocolate',32],['eggs',1],['pollen',64],['peanuts',2],['shellfish',4],['strawberries',8],['tomatoes',16],['mites',256]]
def analyze(person,liste):
    score = 0
    if len(liste) > 1:
       print(f"Trying to find {person}'s allergies")
    else:
       print(f"Trying to find {person}'s allergie")

    for item in liste:
         for allergie in allergies:
            if item == allergie[0]:
              score += allergie[1]

    print(f"{person}'s allergic score is {score}")
             
            
person = 'doddy'
liste = ['cats','mites','pollen']
analyze(person,liste)