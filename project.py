from datetime import datetime
from user import save_data

def create_project(user, users):
    print("Create Project:")
    title = input("Title: ")
    details = input("Details: ")
    target_amount = input("Total Target (EGP): ")

    while True:
        start_date = input("Start Date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        end_date = input("End Date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    project = {'title': title, 'details': details, 'target_amount': target_amount,
               'start_date': start_date.strftime('%Y-%m-%d'), 'end_date': end_date.strftime('%Y-%m-%d')}

    # Ensure 'projects' key exists in the user dictionary
    if 'projects' not in user:
        user['projects'] = []

    user['projects'].append(project)
    save_data(users)
    print(f"Project '{project['title']}' created successfully.")
    return project

def view_all_projects(user):
    if 'projects' in user:
        print("All Projects:")
        for project in user['projects']:
            print(f"Title: {project['title']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")
    else:
        print("No projects available.")

def edit_project(user, users):
    print("Edit Project:")
    view_all_projects(user)

    project_index = int(input("Enter the index of the project you want to edit: ")) - 1

    if 0 <= project_index < len(user['projects']):
        project = user['projects'][project_index]

        print("Current Project Details:")
        print(f"Title: {project['title']}")
        print(f"Details: {project['details']}")
        print(f"Target Amount: {project['target_amount']}")
        print(f"Start Date: {project['start_date']}")
        print(f"End Date: {project['end_date']}")

        new_title = input("Enter new title (press Enter to keep current): ").strip() or project['title']
        new_details = input("Enter new details (press Enter to keep current): ").strip() or project['details']
        new_target_amount = input("Enter new target amount (press Enter to keep current): ").strip() or project['target_amount']

        # Validate and update dates similarly as in the create_project function

        user['projects'][project_index] = {
            'title': new_title,
            'details': new_details,
            'target_amount': new_target_amount,
            'start_date': project['start_date'],
            'end_date': project['end_date']
        }

        save_data(users)
        print("Project updated successfully.")
    else:
        print("Invalid project index.")

def delete_project(user, users):
    print("Delete Project:")

    # Display the user's projects for selection
    projects = user.get('projects', [])
    if not projects:
        print("No projects to delete.")
        return

    for index, project in enumerate(projects, start=1):
        print(f"{index} - {project['title']}")

    # Prompt the user to select a project to delete
    try:
        project_index = int(input("Enter the number of the project to delete: ")) - 1
        if 0 <= project_index < len(projects):
            deleted_project = projects.pop(project_index)
            save_data(users)
            print(f"Project '{deleted_project['title']}' deleted successfully.")
        else:
            print("Invalid project number.")
    except ValueError:
        print("Invalid input. Please enter a valid project number.")


def search_project_by_date(user, search_date):
    if 'projects' in user:
        matching_projects = [project for project in user['projects'] if
                             project['start_date'] <= search_date <= project['end_date']]
        if matching_projects:
            print(f"Projects within the specified date range ({search_date}):")
            for project in matching_projects:
                print(f"Title: {project['title']}, Start Date: {project['start_date']}, End Date: {project['end_date']}")
        else:
            print("No projects found within the specified date range.")
    else:
        print("No projects available.")