grades = [85, 78, 92, 45, 33, 67, 88, 41]

# a
print("Grade Categories:")
for grade in grades:
    if grade > 80:
        category = "A"
    elif 60 <= grade <= 80:
        category = "B"
    elif 40 <= grade <= 60:
        category = "C"
    else:
        category = "F"
    print(f"Score: {grade} - Grade: {category}")

# b
def boost_grades(grades):
    return list(map(lambda x: round(x * 1.05, 2), grades))

boosted_grades = boost_grades(grades)
print("\nBoosted Grades:")
print(boosted_grades)

# c
above_90 = list(filter(lambda x: x > 90, boosted_grades))
print("\nBoosted Grades Above 90:")
print(above_90)