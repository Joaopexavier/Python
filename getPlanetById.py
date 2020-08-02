def get_planet_name(id):
  name: " "
  if id == 1: 
     name = "Mercury"
  if id == 2:
     name = "Venus"
  if id == 3: 
     name = "Earth"
  if id ==  4: 
     name = "Mars"
  if id == 5: 
     name = "Jupiter"
  if id ==  6: 
      name = "Saturn"
  if id == 7: 
     name = "Uranus"  
  if id ==  8: 
     name = "Neptune"
  return name


if __name__ == "__main__":
  id = int(input())
  answer = get_planet_name(id)
  print(answer)
