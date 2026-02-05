list1=[1,2,3,4]
list2=['mango','apple','oranges']
list1.append(list2)
print(list1)

list1.append("akki")

print(list1)

list2.insert(1,"chauhan")
print(list1)

list2.remove("chauhan")

list2.clear() #clear list

list2.index('akki') #to find index 

list2.count('mango') #counting the freq

print(list1.sort()) #sort list

print(list2.reverse())#to print in reverse

list3= list2.copy() #copy list2

list2.pop() #last value in list
