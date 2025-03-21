# Python Dictionaries

thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisDict) # output: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(thisDict["brand"]) # output: Ford

x = thisDict.get("model")
print(x) # output: Mustang
x = thisDict.keys()
print(x) # output: dict_keys(['brand', 'model', 'year'])
x = thisDict.values()
print(x) # output: dict_values(['Ford', 'Mustang', 1964])
x = thisDict.items()
print(x) # output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# Update Dictionary
thisDict["year"] = 2018
thisDict.update({"year": 2020})

# Adding Items
thisDict["color"] = "red"
thisDict.update({"color": "red"})

# Removing Items
thisDict.pop("model")
del thisDict["brand"]
thisDict.popitem() # The popitem() method removes the last inserted item
thisDict.clear() # The clear() method empties the dictionary.
del thisDict # The del keyword can also delete the dictionary completely.