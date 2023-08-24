def is_vowel(character):
    try:
        if len(character) != 1:
            raise ValueError("Input should be a single character")

        if character.lower() in 'aeiou':
            return True
        else:
            return False
    except ValueError as e:
        print(f"Error: {e}")
        return False


# Test the function
input_char = input("Enter a character: ")
if is_vowel(input_char):
    print(f"{input_char} is a vowel.")
else:
    print(f"{input_char} is not a vowel.")
