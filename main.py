from random import choice 


PASSWORD_CHOICES_ASCII = [
    # Uppercase letters: A-Z
    list(range(65, 91)),
    
    # Lowercase letters: a-z
    list(range(97, 123)),
    
    # Numbers: 0-9
    list(range(48, 58)),
    
    # Common symbols
    [ord(symbol) for symbol in "!@#$%^&*"],
    
    # Punctuation marks
    [ord(symbol) for symbol in ".,:;-_"],
    
    # Special characters
    [ord(symbol) for symbol in "[]{}()<>|\\/?=+"]
]
PASSWORD_CHOICES_ASCII = [char for sublist in PASSWORD_CHOICES_ASCII for char in sublist]

if __name__ == "__main__":
  is_generating_passwords = True
  while is_generating_passwords:
    try:
      n = int(input("Enter the number of passwords you want to generate: "))
      lenght = int(input("Enter the lenght of dersired password (min 3): "))
      if lenght < 3:
        raise ValueError("Minimum lenght of password is 3")
      
      passwords = []

      for _ in range(n):
        password = []
        for _ in range(lenght):
          password.append(chr(choice(PASSWORD_CHOICES_ASCII)))
        passwords.append("".join(password))
      
      print("\nYour passwords are: ")
      with open("passwords.txt","w") as file:
        for password in passwords:
          print(password)
          file.write(password + "\n")
      
      is_generating_passwords = False

    except ValueError as e:
      print("Error: ",e)