import datetime
d = datetime.datetime.now()
bool = True
liste = [ i for i in range(100000000)]
l = len(liste)
i = 0
number = 99
#while i < 100000000:
 #   if number == liste[i]:
  #      print(i)
        #bool = False
   # i = i+1

for i in range(1000000):
    if i == number:
       print(i)
       break
    
execution_time = datetime.datetime.now() - d
print(f"execution time is {execution_time}")

    
