def GetLetterFreq(inputVal):
    freq = {}
    occuranceStr = ""
    for letter in inputVal:
        freq[letter] = freq.get(letter, 0) +1

    for letter in inputVal:
        if(freq.get(letter) == 1):
            occuranceStr=letter
            return letter
def CheckAnagram(inputStr1, inputStr2):
    if(sorted(inputStr1) == sorted(inputStr2)):
        print("Both strings are Anagram")
    else:
        print("strings are not Anagram")

def CheckAnagramDict(inputSt1, inputStr2):
    dict1 = {}
    dict2 = {}
    if len(inputSt1) != len(inputStr2):
        print("Not Anagram, Since the length of strings are different")
    for letter in inputSt1:
        dict1[letter] = dict1.get(letter, 0)+1
    for letter2 in inputStr2:
        dict1[letter2] = dict1.get(letter2, 0)-1 
    return all(values==0 for values in dict1.values())
     
def ListFreq():
    singleFreqVal = None
    sampLst = [2,4,4,2]
    dict_freq = {}
    for val in sampLst:
        dict_freq[val] = dict_freq.get(val, 0)+1
    for key, val in dict_freq.items():
        if val == 1:
            singleFreqVal = key
            break
    return singleFreqVal

def LstFreqXOR():
    listVals = [2,4,6,4,2]
    result = 0
    for val in listVals:
        result ^= val
        print(f"val",val)
        print(f"result",result)
    finalVal = result
    return finalVal

def FindMaxAndMin():
    numLst = [10,4,2,64,1,5,11]
    maxVal = numLst[0]
    minVal = numLst[0]  
    for val in numLst:  
        if(val > maxVal):
            maxVal = val
        if(val < minVal):
            minVal = val

    print(f"Max Value - ", maxVal)
    print(f"Min Value - ", minVal) 

if __name__ == "__main__":
    while(True):
        inputVal = input("Please String other than blank value: - ")
        if inputVal:
            break
    finalval = GetLetterFreq(inputVal)
    print(f"First one occurence char -", finalval) 
    result =  CheckAnagramDict("listen", "silent")
    if result:
        print("Strings are Anangram")
    else:
        print("Strings are not Anagram")
    singleFreq = LstFreqXOR()
    print(f"Value with single Frequency: ", singleFreq)

    FindMaxAndMin()