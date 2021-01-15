def drinkOrDrive(age):
    if age > 16 and age < 18:
        print("You are allowed to drive. You cannot drink.")
    elif age > 18:
        print("You are allowed to drink and drive, but not both")
    else:
        print("You cannot drink or drive, you are underage.")


drinkOrDrive(13)
