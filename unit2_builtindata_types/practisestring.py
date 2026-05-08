### Commo string methods 

print(" Hello World !".upper())
print(" Hello World !".lower())
print(" Hello World !".title())
print(" Hello World !".strip())
print(" Hello World !".lstrip())
print(" Hello World !".rstrip())
print(" Hello World !".replace("Hello","Hi"))
print(" Hello World !".split())
country = ["India","Nepal","Bhutan","Bangladesh"]
print(" hello ".join(country))
print("you can use .find to search for character in a string".find("search"))


### write a  python script to count the no. of vowels , semicoons,comman, fullstops, 
### whitespaces, and consonants from the entered paragraph, of 100 Characters. 
### aslo count the no. of words used in a pargaraph.
paragraph = input("Enter the paragraph of 100 characters: ")
vowels = 0
semicolons = 0
commas = 0
fullstops = 0
whitespaces = 0
consonants = 0
for char in paragraph:
    if char in "aeiouAEIOU":
        vowels += 1
    elif char == ";":
        semicolons += 1
    elif char == ",":
        commas += 1
    elif char == ".":
        fullstops += 1
    elif char == " ":
        whitespaces += 1
    elif char.isalpha():
        consonants += 1
print(f"Vowels: {vowels}")
print(f"Semicolons: {semicolons}")  
print(f"Commas: {commas}")
print(f"Fullstops: {fullstops}")
print(f"Whitespaces: {whitespaces}")
print(f"Consonants: {consonants}")
words = paragraph.split()
print(f"Number of words: {len(words)}")
number = "subdin"
print(type(number))
print(number.isalpha())
print(number.isalphanumrc)
