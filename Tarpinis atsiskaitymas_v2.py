# Turimas "audi" dict.

# Parašykite funkciją "showObjectKeys", kuri kaip argumentą priims objektą 
# ir grąžins visus jo "values" list'e.

audi = {
  "make": 'audi',
  "model": 'A6',
  "year": 2005,
  "color": 'white',
}



def showObjectValues(obj):
    values = []
    for key in obj:
        values.append(obj[key])
    return values



print(showObjectValues(audi))
  
  
  