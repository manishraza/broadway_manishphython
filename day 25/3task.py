def is_vowel(character):
    try:
        if character.lower() in 'aeiou':
            return True
        else:
            return False
#test the function
input_char = input("Enter a character: ")
if is_vowel(input_char):
    print(f"{input_char} is a vowel.")
else:
    print(f"{input_char} is not a vowel.")

