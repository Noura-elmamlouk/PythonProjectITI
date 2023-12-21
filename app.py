from user import register_user, login, save_data, load_data
from project import create_project, view_all_projects, edit_project, delete_project, search_project_by_date

def main():
    users = load_data()
    print(f"Type of 'users': {type(users)}")

    while True:
        print("\n1 - Register")
        print("2 - Login")
        print("3 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = register_user(users)
            if user:
                print(f"Welcome, {user['first_name']} {user['last_name']}!")
                show_menu(user, users)
        elif choice == '2':
            user = login(users)
            if user:
                print(f"Welcome, {user['first_name']} {user['last_name']}!")
                show_menu(user, users)
        elif choice == '3':
            save_data(users)
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def show_menu(user, users):
    while True:
        print("\n1 - Create Project")
        print("2 - View Projects")
        print("3 - Edit Project")
        print("4 - Delete Project")
        print("5 - Search Project by Date")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_project(user, users)
        elif choice == '2':
            view_all_projects(user)
        elif choice == '3':
            edit_project(user, users)
        elif choice == '4':
            delete_project(user, users)
        elif choice == '5':
            search_date = input("Enter the date (YYYY-MM-DD) to search for projects: ")
            search_project_by_date(user, search_date)
        elif choice == '6':
            save_data(users)
            print("Exiting to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()