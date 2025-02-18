# Codewars Mod 1 Class work:

# Even or Odd:

def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
print(even_or_odd(6))
print('*' * 50)
print(even_or_odd(1))
print('*' * 50)

# Convert a number(num) to a string (str)
def number_to_string(num):
    return str(num) # Return a string of the number here!
print(number_to_string(591734))
print('*' * 50)

# Vowel Count:

def get_count(sentence):
    vowels = 'AEIOUaeiou'
    if vowels:
        return sum(1 for char in sentence if char in vowels)
    else:
        return 'not a vowel'
print(get_count("a dog in a park")) # 5 vowels
print(get_count(" AA BB CC DD EE FF GG II")) #6 vowels