

print(2+2)

x= {
    "name":"A", "Age":1,
   "name":"B", "Age":2,
}

Y = {"Naboo" :
        {
        "name":"A", "Age":1,
        },
        "Piu" :
        {
        "name":"B", "Age":2,
        }
}

print(x)
print(type(x))
print(x["Age"])


print(Y["Piu"]["Age"])

Y["Piu"]["Age"] += 1

print(Y["Piu"]["Age"])

Y["Piu"]["Age"] += 1

Y["book"] =  {
        "name":"C", "Age":3,
        }

print(Y)

z = {"Naboo" :
        {
        "name":"A", "Age":1,
        },                          # dict
        (1,2) : "piu",               # tuple
       # ["a", "b"] : "test",            #list
        "sample" : [1, 2, 3],           #str
        1 : "learning",              #int
        True : False,               #bool
        2.3 : "x"
}

print(z)
print(z[(1,2)])