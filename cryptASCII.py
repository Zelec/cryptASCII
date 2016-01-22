# This is a python file that transmitter and reciver use as a class to encrypt and decrypt messages
# This function encrypts messages by taking each individual letter, turning it to ASCII decimal, Displacing it my the provided ammount, then it returns the ASCII number to a readable letter
def encrypt(string, dis):
    newWord = ""
    cryptText = ""
    counter = 0
    displace = dis
    text = string
    for i in text:
        letterValue = ord(i) + displace
        # To make sure that if a letter value/displacement is too high the program can correct it
        if letterValue >= 256:
            letterValue -= 255
        asciiValue = chr(letterValue)
        cryptText = cryptText + asciiValue
        counter += 1
    return(cryptText)
# Works the same as the encrypt function, only the displacement goes in the negative direction
def decrypt(string, dis):
    newWord = ""
    cryptText = ""
    counter = 0
    displace = dis
    text = string
    for i in text:
        letterValue = ord(i) - displace
        if letterValue <= -1:
            letterValue += 255
        asciiValue = chr(letterValue)
        cryptText = cryptText + asciiValue
        counter += 1
    return(cryptText)
# Just a test function to show how the code can work
def test():
    test = encrypt("Hello, World!", 254)
    print test
    print decrypt(test, 254)
test()
