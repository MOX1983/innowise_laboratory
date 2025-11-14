
def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
current_age = 2025 - int(birth_year_str)
life_stage = generate_profile(current_age)
hobbies = list()

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby != "stop":
        hobbies.append(hobby)
    else:
        break

user_profile = {"name": user_name,
                "age": current_age,
                "life_stage": life_stage,
                "hobbies": hobbies}
print(f"---"
      f"\nProfile Summary:\n"
      f"Name: {user_profile.get("name")}\n"
      f"Age: {user_profile.get("age")}\n"
      f"Life Stage: {user_profile.get("life_stage")}")

if user_profile.get("hobbies"):
    print(f"Favorite Hobbies ({len(user_profile.get("hobbies"))}):")
    for hobby in user_profile.get("hobbies"):
        print(f"-{hobby}")
else:
    print(f"You didn't mention any hobbies.")
print("---")
