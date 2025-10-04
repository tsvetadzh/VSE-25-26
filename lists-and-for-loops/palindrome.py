words = ["level", "python", "radar", "civic", "java", "kotlin", "refer"]
palindromes = []
for word in words:
    if word == word[::-1]: #slicing neshtoto - obryshta reda
        palindromes.append(word)
print("palindromes are:", palindromes)