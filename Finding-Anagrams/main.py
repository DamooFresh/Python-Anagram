# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    str1 = input('Input your first word: ')
    str2 = input('Input your second word: ')

    if len(str1) == len(str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False

    else:
        return "Your input is not Anagram"

print(find_anagram(input, sorted))