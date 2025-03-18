# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.

# String
string = "Hello World"
print(string) # Hello World

# Number
number = 49
print(number) # 49

# List
list = [1, 2, 3, 4, 5]
print(list) # [1, 2, 3, 4, 5]

# Boolean
boolean = True
print(boolean) # True

# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.

string = "Hello World"
first_three_letters = string[:3]
print(first_three_letters) # Hel

# Exercise 3: Use an index to grab the first element from your list.

list = [1, 2, 3, 4, 5]
first_element = list[0]
print(first_element) # 1

# Exercise 4: Create a new number variable that adds 10 to your original number.

number = 49
new_number = number + 10
print(new_number) # 59

# Exercise 5: Use an index to get the last element in your list.

list = [1, 2, 3, 4, 5]
last_element = list[-1]
print(last_element) # 5

# Exercise 6: Use split to transform the following string into a list.

names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(',')
print(names_list) # ['harry', 'alex', 'susie', 'jared', 'gail', 'conner']

# Exercise 7: Get the first word from your string using indexes. Use the upper function to 
# transform the letters into uppercase. Create a new string that takes the uppercase word 
# and the rest of the original string.

string = "Hello World"
first_word = string[:5]
first_word_upper = first_word.upper()
rest_of_string = string[5:] 
new_string = first_word_upper + rest_of_string
print(new_string) # HELLO World

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.

number = 49
print(f"The lucky number is {number}") # The lucky number is 49

# Exercise 9: Print “hello world”.

print("hello world") # hello world

# Cadena que contenga la palabra "Hola". Usando la palabra clave en el método de búsqueda o el índice, 
# busque y seleccione "Hola" en su cadena. Y usando la función de reemplazo, reemplace "Hola" en su cadena 
# con "adiós".

string = "Hola Mundo"
print("Hola" in string) # True
print(string.index("Hola")) # 0

new_string = string.replace("Hola", "Adiós")
print(new_string) # Adiós Mundo



