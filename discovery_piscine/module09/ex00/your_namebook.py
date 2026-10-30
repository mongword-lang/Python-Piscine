#!/opt/pyenv/shims/python

def array_of_names(names_dict):
    """
    Takes a dictionary of associating first names with last names.
    Returns a list of full names, each with the first letter capitalized
    """
    full_names = []
    for first, last in names_dict.items():
        full_names.append(first.capitalize() + " " + last.capitalize())
    return full_names

# Example
people = {"jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi":"brindacier"}
print(array_of_names(people))
# Output: ['Jean Valjean', 'Grace Hopper', 'Xavier Niel', 'Fifi Brindacier']
