char1, char2 = input("Enter two space-separated characters: ").split()

greater_char = max(char1, char2)

print("--------------------------------")
print(f"The character with greater value is: {greater_char}")
print("--------------------------------")

ascii1 = ord(char1)
ascii2 = ord(char2)
print("This part is optional to include.")
print(f"Showing ASCII Values:\n{char1} : {ascii1}\n{char2} : {ascii2}")