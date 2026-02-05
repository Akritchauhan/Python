countries=['uk','india','america','pak']
print(countries)

for i in countries:
    print(i)

print(countries[0:])
print(countries[:-1])

print(type(countries))

countries[0]='ban'
print(countries)

print(len(countries))

#we can add multiple datatypes in a list

#list constructor
countries1=list(('nigeria',34,False))
print(countries1)