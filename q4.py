def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome(str(7489617719749244646336564429479177169847)))
print(palindrome(str(6593036601359343374664733439531066303956)))
print(palindrome(str(8025833559061079503003059701609553385208)))
print(palindrome(str(5485839837501070045005400701057389385845)))