users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

def user_twitter(person):
    return users[person]["twitter"]

print(user_twitter("Jonathan"))
# 2. Get Erik's hometown

def user_hometown(person):
    return users[person]["home_town"]

print(user_hometown("Erik"))
# 3. Get the list of Erik's lottery numbers

def user_lotto(person):
    return users[person]["lottery_numbers"]

print(user_lotto("Erik"))

# 4. Get the species of Avril's pet Monty

def user_pet_species(person, pet_index):
    return users[person]["pets"][pet_index]["species"]

print(user_pet_species("Avril", 0))

# 5. Get the smallest of Erik's lottery numbers

def get_lowest_number(person):
    return min(user_lotto(person))

print(get_lowest_number("Erik"))

# 6. Return an list of Avril's lottery numbers that are even

def get_even_numbers(person):
    return list(filter(lambda x: (x % 2 == 0), user_lotto(person)))

print(get_even_numbers("Avril"))

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

def add_lotto_num(person, number):
    users[person]["lottery_numbers"].append(number)

add_lotto_num("Erik", 7)

print(user_lotto("Erik"))

# 8. Change Erik's hometown to Edinburgh

def change_hometown(person, hometown):
    users[person]["home_town"] = hometown

change_hometown("Erik", "Edinburgh")

print(user_hometown("Erik"))
# 9. Add a pet dog to Erik called "fluffy"

def add_pet(person, pet, species):
    users[person]["pets"].append({
        "name": pet,
        "species": species
    })

add_pet("Erik", "fluffy", "dog")

print(user_pet_species("Erik", 4))

# 10. Add another person to the users dictionary

def add_user(person):
    users.update({person: {}})

add_user("Shelby")

print(users)

