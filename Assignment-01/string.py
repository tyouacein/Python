sentence = "Learning Python is fun and rewarding."

# a. Extract the substring "Python is fun" using negative slicing
substring = sentence[-28:-14]
print("Extracted substring:", substring)
print()

# b. Modify the original string by replacing "rewarding" with "exciting"
sentence = sentence.replace("rewarding", "exciting")
print("Modified sentence:", sentence)
print()

# c. Insert the phrase " Keep practicing!" after "exciting" in the modified string
Insert_index = sentence.find("exciting.") + len("exciting.")
sentence = sentence[:Insert_index] + " Keep practicing!" + sentence[Insert_index:]
print("Modified sentence with inserted phrase:", sentence)
print()

# d. Capitalize the first letter of each word in the final output
Final = " ".join(word.capitalize() for word in sentence.split())
print("Final output:", Final)