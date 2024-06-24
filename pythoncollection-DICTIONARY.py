a={"Name":"Sohail",
   "Age":20,
   "Fav Subjects":["Physics","Maths"]
    }
print(a)
print(a.keys())
print(a.values())
a["Age"]=21
print(a)
a["Degree"]="Phy"
print(a)
a.update(Age=20)
print(a)
a.pop("Degree")
print(a)
del a["Age"]
print(a)
a.clear()
print(a)
