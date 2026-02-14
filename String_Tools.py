
def CountVowels(inputStr):
    vowelsLst = ['a','e','i','o','u']
    vowelCnt = 0
    for letter in inputStr[:]:
        if(letter in vowelsLst):
            vowelCnt = vowelCnt+1
    return vowelCnt

def ImprovedCountVowels(inputStr): 
    #return sum(1 for letter in inputStr if letter.lower() in "aeiou")
    return sum(ovel in "aeiou" for ovel in inputStr.lower())

def CheckPalindrome(inputStr):
    if (inputStr == inputStr[::-1]):
        return "Palindrome"
    else:
        return "Not Palindrome"

def ReverseString(inputStr):
    return inputStr[::-1]

def RemoveDuplicates():
    someLst = [1,2,55,2,5,2,7,1]
    uniqLst = []
    emptySet = set()

    for val in someLst:
        if(val not in emptySet):
            uniqLst.append(val)
            emptySet.add(val)
    print(uniqLst)

if __name__ == "__main__": 
    while(True):
        inputStr = input("Enter a String - ")
        if not inputStr:
            print("Empty Values are not allowed")
        else:
            break
    reveredStr = ReverseString(inputStr)
    vowelCount = ImprovedCountVowels(inputStr)
    palindrome = CheckPalindrome(inputStr.lower())

    print(f"Reversed String", reveredStr)
    print(f"Count Vowels", vowelCount)
    print(f"Input is: ", palindrome)
    RemoveDuplicates()