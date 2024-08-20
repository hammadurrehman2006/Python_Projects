print("\tCaesar Cipher Program")
print("-------------------------------------")
# Define a function to find the truth by shifting the letter by the specified amount
def lasso_letter(letter, shift_amount):
    if letter.isalpha():  # Check if the letter is alphabetic
        # Determine if the letter is uppercase or lowercase
        if letter.isupper():
            a_ascii = ord('A') 
        else:
            a_ascii = ord('a')

        # The number of letters in the alphabet
        alphabet_size = 26

        # Calculate the ASCII number for the decoded letter
        true_letter_code = a_ascii + (((ord(letter) - a_ascii) + shift_amount) % alphabet_size)

        # Convert the ASCII number to the character or letter
        decoded_letter = chr(true_letter_code)
    else:
        # If the character is not a letter, don't change it
        decoded_letter = letter

    # Send the decoded letter back 
    return decoded_letter

# Define a function to find the truth in a secret message
# Shift the letters in a word by a specified amount to discover the hidden word
def lasso_word(word, shift_amount):

    # This variable is updated each time another letter is decoded
    decoded_word = ""

    # This for loop iterates through each letter in the word parameter
    for letter in word:
        # The lasso_letter() function is invoked with each letter and the shift amount
        # The result (the decoded letter) is stored in a variable called decoded_letter
        decoded_letter = lasso_letter(letter, shift_amount)

        # The decoded_letter value is added to the end of the decoded_word value
        decoded_word = decoded_word + decoded_letter

    # The decoded_word is sent back to the line of code that invoked this function
    return decoded_word


# Define a function to process the entire sentence
def lasso_sentence(sentence, shift_amount):
    words = sentence.split()  # Split the sentence into words
    decoded_words = [
        lasso_word(word, shift_amount) for word in words
    ]  # Decode each word
    return " ".join(decoded_words)  # Join the decoded words back into a sentence
sentence = input("Enter the sentence you want to encrypt or decrypt:..")
shift_amount = int(input("Enter the shift amount: "))
print(f"The encrypted/decrypted message of your sentence is :\n {lasso_sentence(sentence, shift_amount)}")