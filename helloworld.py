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

# import csv
#
# csvFile= open("csvFile.csv")
# readCsv=csv.reader(csvFile, delimiter=",")
# for i in readCsv:
#     print(str.format("Name: {}, Surname: {}, Subject: {}", i[0],i[1],i[2]))

# import csv
# csvFile = open('names.csv', 'w', newline='')
# fieldnames = ['name', 'surname']
# writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
# writer.writeheader()
# writer.writerow({'name': 'Sergio', 'surname': 'Ramos'})
# writer.writerow({'surname': 'Nadal'})
# writer.writerow({'name': 'Julio', 'surname': 'Hernandez'})

# import csv
# csvfile = open("csvFile.csv")
# procitanCSV = csv.DictReader(csvfile, delimiter=',')
# for a in procitanCSV:
#     print(a["name"], a["surname"], a["subject"])

# import pymysql
#
# db = pymysql.connect("localhost","root","password","python")
# print("Succsesfuly opened")
# cur = db.cursor()
# # sql = "SELECT * FROM users"
# # sql = "SELECT firstname, lastname, year FROM users WHERE firstname = 'Sergio'"
# # jedno = radi zasto dva ne rade ?
# # print(sql)
# # cur.execute(sql)
# cur.execute(" SELECT * FROM users WHERE firstname = 'Sergio' ")
# for row in cur:
#     print(str.format("id={}, firstname={}, lastname={}, year={}", row[0], row[1], row[2], row[3]))
# # for row in cur:
# #     print(str.format("firstname={}, lastname={}, year={}", row[0], row[1], row[2]))
# db.close()


# import mysql.connector
# mydb = mysql.connector.connect(host="localhost", user="root", password="password",  database="python")
#
# mycursor = mydb.cursor()
# # mycursor.execute("SELECT * FROM users")
# mycursor.execute(" SELECT * FROM users WHERE firstname = 'Sergio' ")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)


from tkinter import *
import tkinter as tk
from tkinter import ttk
import mysql.connector
import pymysql

# mydb = mysql.connector.connect(host="localhost", user="root", password="password",  database="aptk")
mydb = pymysql.connect(host="localhost", user="root", password="password",  database="aptk")
# mycursor = mydb.cursor()
cur=mydb.cursor()

def updatelist(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert("","end", values=i)

def getrow(event):
    rowid=trv.identify_row(event.y)
    item=trv.item(trv.focus())
    # print(item['values'][0])
    t1.set(item['values'][0])
    # t1.set(item['values'][0])
    # t2.set(item['values'][1])
    t2.set(item['values'][1])
    t3.set(item['values'][2])
  # w = event.widget
  # index= int(w.curselection()[0])
  # value=w.get(index)

def insert():
    # id = t1.get()
    name = t2.get()
    error = t3.get()
    # mycursor.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    # cur.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    cur.execute("INSERT INTO ticket (id,name,error) VALUES (NULL, %s, %s)",(id,name,error))
    # cur.execute("INSERT INTO ticket (name,error) VALUES (%s, %s)",(name,error))
    mydb.commit()
    mydb.close()

def delete():
    id = t1.get()
    # name = t1.get()
    # error = t2.get()
    # mycursor.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    # cur.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    # cur.execute("INSERT INTO ticket (id,name,error) VALUES (%s, %s)",(id,name,error))
    cur.execute("DELETE FROM ticket WHERE id="+id)
    mydb.commit()
    mydb.close()

def update():
    name = t2.get()
    error = t3.get()
    id = t1.get()
    # mycursor.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    # cur.execute("INSERT INTO ticket(name,error) VALUES ('{}','{}')".format(e1.get(),e2.get()))
    # cur.execute("INSERT INTO ticket (id,name,error) VALUES (%s, %s)",(id,name,error))
    cur.execute("UPDATE ticket SET name=%s, error=%s WHERE id="+id,(name,error))
    mydb.commit()
    mydb.close()


root= Tk()
q=StringVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()

wraper1=LabelFrame(root, text='Ticket list')
wraper2=LabelFrame(root, text='Entry data')

wraper1.pack()
wraper2.pack()


# lb= tkinter.Listbox(top)
# lb.pack()
#
# lb.bind('<<ListboxSelect>>', getrow)

trv = ttk.Treeview(wraper1, columns=(1,2,3), show='headings', height='6')
# trv = ttk.Treeview(wraper1, columns=(1,2), show='headings', height='6')
trv.pack()

trv.heading(1, text='id')
trv.heading(2, text='name')
trv.heading(3, text='error')

trv.bind('<Double 1>', getrow)

query="SELECT * FROM ticket"
cur.execute(query)
rows=cur.fetchall()
updatelist(rows)

lbl1=Label(wraper2, text='id')
lbl1.grid()
e1=Entry(wraper2, textvariable=t1)
e1.grid()

# lbl1=Label(wraper2, text='name')
# lbl1.grid()
# e1=Entry(wraper2, textvariable=t1)
# e1.grid()
#
# lbl2=Label(wraper2, text='error')
# lbl2.grid()
# e2=Entry(wraper2, textvariable=t2)
# e2.grid()

lbl2=Label(wraper2, text='name')
lbl2.grid()
e2=Entry(wraper2, textvariable=t2)
e2.grid()

lbl3=Label(wraper2, text='error')
lbl3.grid()
e3=Entry(wraper2, textvariable=t3)
e3.grid()

btn_add=tk.Button(root, text='Add', command=insert)
btn_add.pack()

btn_add=tk.Button(root, text='Delete', command=delete)
btn_add.pack()

btn_add=tk.Button(root, text='Update', command=update)
btn_add.pack()

root.geometry('800x600')
root.mainloop()





































































































