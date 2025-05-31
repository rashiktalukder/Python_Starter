
rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

mapping = {}

for char in rhyme:
    if char.isalpha():
        if char in mapping:
            mapping[char] += 1
        else:
            mapping[char] = 1    

mostFrequentCharacter = max(mapping, key = mapping.get)
print(mapping)
frequency = mapping[mostFrequentCharacter]

print(f"Most Frequent: {mostFrequentCharacter} and frequency {frequency}")



#Most frequent word

# refinedRhyme = ""

# for char in rhyme:
#     if (char >= 'A' and char <= 'Z') or (char >= 'a' and char <= 'z') or char == ' ':
#         refinedRhyme += char

# splittedWords = refinedRhyme.split()
# rhymeDict = {}

# for word in splittedWords:
#     if word in rhymeDict:
#         rhymeDict[word.lower()] += 1
#     else:
#       rhymeDict[word.lower()] = 1

# mostFrequentWord = max(rhymeDict, key = rhymeDict.get)

# print(mostFrequentWord)