#!/opt/pyenv/shims/python

def famous_births(people):
    for key in sorted(people, key=lambda k: people[k]["date_of_birth"]):
        print(f"{people[key]['name']} is a great scientist born in {people[key]['date_of_birth']}")  

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecelia": {"name": "Cecelia Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}
famous_births(women_scientists)

 
