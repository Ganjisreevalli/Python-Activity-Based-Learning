


print("===== PASSWORD VALIDATION SYSTEM =====")

password = input("Enter a password to validate: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_characters = "!@#$%^&*()-_+=?"

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_digit = True
    elif character in special_characters:
        has_special = True

print("\n===== VALIDATION RESULTS =====")
print("Minimum 8 characters:", len(password) >= 8)
print("Contains uppercase letter:", has_upper)
print("Contains lowercase letter:", has_lower)
print("Contains digit:", has_digit)
print("Contains special character:", has_special)

if (
    len(password) >= 8
    and has_upper
    and has_lower
    and has_digit
    and has_special
):
    print("\nPassword Status: VALID")
else:
    print("\nPassword Status: INVALID")

print("======================================")
