def find_user_info(full_name_to_find): # Define the function find_user_info
    
    try:
        with open("user_infos.txt", "r") as file: # to open and read the file in prog 1
            found = False # To track if the user is in the file
            user_info = [] # To store user's informations

            for line in file: # Loop
                if line.strip().startswith("Full Name: "): # Make sure line starts with "Full Name:"
                    name_in_file = line.strip()[11:]
            
                # Compare it with the full name being searched
                if name_in_file == full_name_to_find:
                        found = True
                        user_info.append(line.strip())
                        break  # Exit the loop after finding the user
                elif found: 
                    if line.strip() == "":  # Stop at the blank line separating user blocks
                        break
                    user_info.append(line.strip())
            
            # Display the results
            if found:
                print("\n--- User Information Found ---")
                for info in user_info:
                    print(info)
            else:
                print("User not found.")
    except FileNotFoundError:
        print("Error: 'user_info.txt' file not found.")

if __name__ == "__main__": # Construct checks this variable to determine whether the script is being executed directly or imported.
    print("Welcome to the User Information Finder!")
    full_name = input("Enter the full name to search: ")
    find_user_info(full_name)