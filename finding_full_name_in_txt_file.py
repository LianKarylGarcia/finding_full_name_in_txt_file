def find_user_info(full_name_to_find): # Define the function find_user_info
    
    try:
        with open("user_infos.txt", "r") as file: # to open and read the file in prog 1
            found = False # To track if the user is in the file
            for line in file: # Loop
                if line.strip().startswith("Full Name: "): # Make sure line starts with "Full Name:"
                    name_in_file = line.strip()[11:]
            
                # Compare it with the full name being searched
                elif name_in_file == full_name_to_find:
                        print(f"User found: {name_in_file}")
                        found = True
                        break  # Exit the loop after finding the user
            if not found:
                print("User not found")
        
    except FileNotFoundError:
        print("Error: 'user_info.txt' file not found.")

