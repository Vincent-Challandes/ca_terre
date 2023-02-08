# Function
def print_alphabet(a):
    result = ""
    for i in a:
        i = i.lower()
        result += i
    return result

# Variables
#alphabet = ["A", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet = "AbcdefghijKlmnopqrstuvwxyz"

# Resolution
resultat = print_alphabet(alphabet)

# Display
print(resultat)
