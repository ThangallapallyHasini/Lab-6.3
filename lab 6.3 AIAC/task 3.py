def Age_Classifies(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child (0-12)"
    elif age <= 17:
        return "Teenager (13-17)"
    elif age <= 64:
        return "Adult (18-64)"
    else:
        return "Senior (65+)"

# Example usage:
age_input = int(input("Enter age: "))
print("Age group:", Age_Classifies(age_input))