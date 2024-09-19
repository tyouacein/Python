def course():
    # 1. Create a dictionary
    courses = {
        "CSE101": {"Course name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"}
    }

    # 2. Update
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."

    # 3. Add
    courses["CSE104"] = {"Course name": "Algorithms", "Credits": 4, "Instructor": "Dr. Dave"}

    # 4. Remove
    del courses["CSE101"]

    # 5. Loop through the dictionary and print the course code along with its details
    for code, details in courses.items():
        print(f"Course Code: {code}")
        print(f"Name: {details['Course name']}")
        print(f"Credits: {details['Credits']}")
        print(f"Instructor: {details['Instructor']}")
        print()
course()