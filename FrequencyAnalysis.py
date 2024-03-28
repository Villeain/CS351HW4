def frequencyAnalysis(text, num):
    newText = list(text)
    occurances = dict()
    for letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        occurances[letter] = 1
    realFrequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C', 'U',\
                     'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'Q', 'X', 'Z']

    for letter in text:
        if letter.isalpha():
            occurances[letter] += 1

    letters = sorted(occurances, key=occurances.get, reverse=True)
    for i in range(num):
        for j in range(len(newText)):
            # replace all letters[i] with realFrequency[i] in newText
            if newText[j] == letters[i]:
                newText[j] = realFrequency[i]
        print((letters[i], realFrequency[i]))
    newText = ''.join(newText)
    return newText
    
if __name__ == '__main__':
    replaced = 0
    inp = 'a'
    text = input("Enter a text to do frequency analysis on: ")
    num = input("Enter the number of letters you would like to replace: ")
    replaced = int (num)
    print(frequencyAnalysis(text, replaced))
    while inp.isalnum() and inp != 'Exit' and inp != 'exit':
        inp = input("Enter either:\n 1. A number of letters to replace with the \
most likely replacement.\n 2. Two letters with no space in between. \
The first letter in the encrypted text will be replaced with the second letter. \
3. Type Exit or any non-alphanumeric character to exit.\n")
        # if inp is numeric - replace letters:
        # elif inp is 2 letters - replace letter 0 with letter 1
        # else prompt again 
        

