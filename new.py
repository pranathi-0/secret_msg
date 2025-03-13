def getReverseletter(letter):
    alpha="abcdefghijklmnopqrstuvwxyz"
    reversealpha=alpha[::-1]
    for i in range(0,len(alpha)):
        if letter.lower() and letter==alpha[i]:
            return reversealpha[i]
        if letter.upper() and letter==alpha[i].upper():
            return reversealpha[i].lower()
    return letter
def main():
    inputstring=input()
    outputstring=""
    for letter in inputstring:
        reverseletter=getReverseletter(letter)
        outputstring+=reverseletter
    print(outputstring.lower())
main()