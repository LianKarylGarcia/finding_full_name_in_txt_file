def find_user_info(full_name_to_find): # Define the function find_user_info
    
    try:
        with open("user_infos.txt", "r") as file: # to open and read the file in prog 1
            found = False # To track if the user is in the file
            for line in file: # Loop
                if line.strip().startswith("Full Name: "): # Make sure line starts with "Full Name:"
                    print("User found: ")
                elif line.strip()[11:] == full_name_to_find: # Extract the name
                    print(line.strip())
            
            if not found:
                print("User not found")
        
    except FileNotFoundError:
        print("Error: 'user_info.txt' file not found.")

