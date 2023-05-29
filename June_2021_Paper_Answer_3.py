# Q03(a)

# Initialise variables
alphabet = ["a","b","c","d","e","f","g","h","i","j",
            "k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z"]

plaintext = ""
ciphertext = ""
key = 0
plaintextLength = 0
count = 0

# Add your code to get the plaintext and convert it to lowercase
plaintext = str(input("write the plaintext:").lower())


# Add your code to get the key and make sure the key is between 1 and 25
key = int(input("1-25 for the key: "))
while key < 1 or key > 25:
    key = int(input("1-25 for the key: "))



    
# Ciphertext is generated
plaintextLength = len(plaintext)

# Each plaintext letter is convereted into a ciphertext letter
while count <  plaintextLength:
    found = False
    alphabetCount = 0
    while alphabetCount < 26 and found == False:
        if alphabet[alphabetCount] == plaintext[count]:
            found = True
            if alphabetCount + key - 26 < 0:
                ciphertext += alphabet[alphabetCount + key]
            else:
                ciphertext += alphabet[alphabetCount + key - 26]
        alphabetCount = alphabetCount + 1
    count = count + 1

# Add your code to write the ciphertext to a text file    
f = open("ciphertext.txt", 'w')
f.write(ciphertext)
f.close()

# Add your code to display the ciphertext
print(ciphertext)
