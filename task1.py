favfruitsnum = int(input("Enter num of fruits : " ))
nameoffruits = []

for i in range(favfruitsnum):
    fruitname = input("Enter name of fruits : ")
    nameoffruits.append(fruitname)
   
    if nameoffruits == "apple":
       print("Happy Eating")
    elif nameoffruits == "banana":
    break


print(nameoffruits)