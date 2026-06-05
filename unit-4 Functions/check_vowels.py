#### python a program to do the volume or not 


def check_vowels(vowel):
    if vowel in ["a","e","i","o","u"]: 
       return True 
    else:
        return False 

words = input("Enter a words:: ")
vlist = list(filter(check_vowels,words))
print(f"The vowels used in {words} are {vlist} and no. of vowels = {len(vlist)}")

###
n = int(input("Enter the number :: "))
result = lambda n:n**2 
print(result(5))
### using the lambda function to filter the number's 

number_list = ["a","e","i","o","u"]
word = input("Enter the words:: ")
result = list(filter(lambda word: word in number_list,word))
print(result)
