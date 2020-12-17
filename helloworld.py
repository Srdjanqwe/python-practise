# print('hello world')
# print('Hello','World', sep=", ", end=";")

# promenljiva= 'marko'
# print(promenljiva)
# promenljiva= 5
# print(promenljiva)
# promenljiva= 3.1454353453
# print(promenljiva)

# ime=input("Name: ")  # ime = "Marko"
# print(ime)

# if 23>2:
#     print('dsada')

# a = True
# print(a)
# b = False
# print(b)

# a=4
# print(type(a))
# a=4.13
# print(type(a))
# a='4'
# print(type(a))

# a='tec'
# b="ovo je recenica."
# c=""""trololo
# asdf
# qwerty"""
# print(a)
# print(b)
# print(c)

# a='I\'m Sergio. It\'s his book. He\'s '
# print(a)

# \' Jednostruki navodnik
# \" Dvostruki navodnik
# \t Tab
# \n Novi red

# a="ovo je \ttab , ovo je navdva\" ovo je  novi red \nred"
# print(a)

# x=int(1)
# y=int(2.8)
# z=int("3")
#
# print(x)
# print(y)
# print(z)
# print(type(z))
#
# x=float(1)
# y=float(2.8)
# z=float("3")
#
# print(x)
# print(y)
# print(z)
#
# x=str(1)
# y=str(2.8)
# z=str("3")
#
# print(x)
# print(y)
# print(z)
#
# a = int(input("unesi broj: "))
# print(type(a))

# a=(2*4)/3*8-1
# b=10//3
# c=(a**b)
# print(c)
# print(type(c))
# print(int(c))

# x=3
# x+=5
# print(x)

# a=input('unesi a:')
# b=input('unesi b:')
# if a==b:
#     print('a je jednako b')

# lista=[34,56,105.78,98,2,3.2,23,69,71]
# print(lista)
# lista.sort()
# lista.reverse()
# print(lista)
# print("-------------")
# print(lista[::3])


# x=0
# lozinka='qwerty'
# unos=input('unesi lozinku: ')
# brojPokusaja=2
# for x in range(brojPokusaja):
#     if unos != lozinka:
#         print('pogresno uneto unesi ponovo')
#         unos = input('unesi lozinku: ')
#     elif unos == lozinka:
#         sum = 0
#         for i in range(1, 101):
#             sum += i
#         print('zbir prvih 100',sum)
#         quit()
#     else:
#         print('Potrosili ste pokusaje')

# numElemetent=int(input('How many items you want: '))
# lista=[]
# for i in range(numElemetent):
#     typeNum=input('What type you want: s f i?')
#     elem=input('type:')
#     if typeNum =='s':
#         lista.append(elem)
#     elif typeNum =='f':
#         lista.append(float(elem))
#     elif typeNum =='i':
#         lista.append(int(elem))
# print(lista)

import json

# dictPersonJSON = '{ "name" : "Marko", '\
#                 ' "surname" : "Markovic", '\
#                 ' "age":33 '\
#                 '}'
# dictPerson = json.loads(dictPersonJSON)
# print(dictPerson["surname"])

# dictPerson = { "name" : "Marko",
#                 "surname" : "Markovic",
#                 "age":33
#                 }
#
# dictPersonJSON = json.dumps(dictPerson)
# print(dictPersonJSON)
# print(dictPerson["name"])


# import requests
# req = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Belgrade&APPID=82705ba5bdef2e420e9b9a82d4f11347")
# cont=req.json()
# lon=cont["coord"]["lon"]
# print(lon)
# desc=cont["weather"][0]["description"]
# print(desc)
#
# print(cont)

import csv

csvFile= open("csvFile.csv")
readCsv=csv.reader(csvFile, delimiter=",")
for i in readCsv:
    print(str.format("Name: {}, Surname: {}, Subject: {}", i[0],i[1],i[2]))





































































