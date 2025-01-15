#will update the revision and new update regarding the dictionary all in python


# dict:    store data in the key-value pair
# key:     unique identifier for the data
# value:   associated value for the key


d={
    1:"ganesh",
    2:"ram",
    3:"shyam",
    4:"hari",
    5:"sita",
    6:"gita"
}

print(d)


# key is not duplicate

dict2=dict(a="ganesh",B="ram",c="shyam",d="hari",e="sita",f="gita")
print(dict2)


#important thing: dict can be a set but not the list because list is not hashable #TODO

a={

    "('a',1)":"ganesh",

}
print(a)
print(a["('a',1)"])
print(a.get("('a',1)"))

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
d["age"] = 22
# Updating an existing value
d[1] = "Python dict"
print(d)


del d[1]
print(d)