def main():
        path = "books/frankenstein.txt"
        text = getBookText(path)
        wordCount = getWordCount(text)
        numChars = getCharCount(text)
        alphaCharDict = alphaChars(numChars)
        sortedChars = sortChars(alphaCharDict)
        report(path, wordCount, sortedChars)

def report(path, wordCount, sortedChars):
     print(f"--- Begin report of {path} ---")
     print(f"{wordCount} words found in the document \n")
     for char, count in sortedChars:
          print(f"The '{char}' character was found {count} times")
     print("--- End report ---")

def getCharCount(text):
    chars = {}
    lowCaseText = text.lower()
    for char in lowCaseText:
        if char in chars:   
            chars[char] += 1
        else:
             chars[char] = 1
    return chars

def getWordCount(text):
     words = text.split()
     return len(words)


def getBookText(path):
    with open(path) as f:
        return f.read()
    
def alphaChars(numChars):
     alpha = {}
     for char in numChars:
          if char.isalpha():
               alpha[char] = numChars[char]
     return alpha
    
def sortChars(alphaChars):
     sortedChars = sorted(alphaChars.items(), key=lambda item: item[1], reverse=True)
     return sortedChars

main()