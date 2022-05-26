class Student:
    # [assignment] Skeleton class. Add your code here
    #Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
    Bob = 'Student'
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
Bob = Student("bob", 26, ["FE","BE"], 20.90)
print('Bob details:')
print("my name is", Bob.name)
print("I am", Bob.age)
print("my track is", Bob.tracks)
print("my score is", Bob.score)

# Expected methods
Bob_change_details = Student("Peter", 34, "UI/UX", 20.90)
print('other details:')
print("my name is:", Bob_change_details.name)
print("I am", Bob_change_details.age)
print("my track is", Bob_change_details.tracks)
print("my score is", Bob_change_details.score)

#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
