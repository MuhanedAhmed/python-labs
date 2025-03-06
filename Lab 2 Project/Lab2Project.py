from re import fullmatch
from datetime import datetime
from time import sleep
from os import system

# ====================== Helper Functions ====================== #

def print_delay_alone(msg:str="", delay:int=0, alone:bool=False):
  if (alone):
    system("cls")
  if (len(msg) > 0):
    print(msg)
  if (delay > 0):
    sleep(delay)

# ====================== Validation Functions ====================== #

def validate_email(email):
  return fullmatch(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)

def validate_existing_email(email):
  with open("users.txt", "r") as file:
    for line in file:
      user_info = line.strip().split(",")
      if user_info[3] == email:
        return True
  return False

def validate_phone(phone):
  return fullmatch(r'^(010|011|012)\d{8}$', phone)

def validate_password(password):
  return fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[~!@#$%^&*()=+?><])[A-Za-z\d~!@#$%^&*()=+?><]{6,}$", password)

def validate_date(date_str):
  try:
    datetime.strptime(date_str, "%Y-%m-%d")
    return True
  except ValueError:
    return False

def validate_end_date(start_date_str, end_date_str):
  if not validate_date(end_date_str):
    print("Invalid date format. Please use YYYY-MM-DD !!!")
    return False
  
  if datetime.strptime(end_date_str, "%Y-%m-%d") < datetime.strptime(start_date_str, "%Y-%m-%d"):
    print("End Date can NOT be before Start Date !!!")
    return False
  
  return True

def is_project_title(project_title, user):
  with open("projects.txt", "r") as file:
    for line in file:
      project_data = line.strip().split(",")
      if project_data[0] == user and project_data[1] == project_title:
        return True
  
  return False

# ====================== User Functions ====================== #

def register():
  print_delay_alone(alone=True)
  print("\n========== Registration Form ==========\n")
  
  first_name = input("First Name : ")
  
  last_name = input("Last Name : ")
  
  user_phone = input("Mobile Phone : ")
  while not validate_phone(user_phone):
    print("Invalid Mobile Phone. Try again !!!")
    user_phone = input("Mobile Phone : ")
  
  user_mail = input("Email : ")
  while (not validate_email(user_mail)) or (validate_existing_email(user_mail)):
    print("Invalid Email. Try again !!!")
    user_mail = input("Email : ")
  

  user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")
  while not validate_password(user_password):
    print("Invalid Password. Try again !!!")
    user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")

  confirm_password = input("Confirm Password: ")
  while user_password != confirm_password:
    print("Passwords don't match. Try again !!!")
    user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")
    while not validate_password(user_password):
      print("Invalid Password. Try again !!!")
      user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")
    confirm_password = input("Confirm Password: ")

  with open("users.txt", "a") as file:
    file.write(f"{first_name},{last_name},{user_phone},{user_mail},{user_password}\n")
  print_delay_alone(msg="Registration Done !!!", delay=2, alone=True)

def login():
  print_delay_alone(alone=True)
  print("\n========== Login Form ==========\n")
  user_mail = input("Email : ")
  while not validate_email(user_mail):
    print("Invalid Email. Try again !!!")
    user_mail = input("Email : ")
  
  user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")
  while not validate_password(user_password):
    print("Invalid Password. Try again !!!")
    user_password = input("Password (6 characters at least, 1 lower, 1 upper, 1 digit, 1 special): ")
  
  with open("users.txt", "r") as file:
    for line in file:
      user_info = line.strip().split(",")
      if user_info[3] == user_mail and user_info[4] == user_password:
        print_delay_alone(msg="Login successfully !!!", delay=2, alone=True)
        return user_mail
  print_delay_alone("Invalid email or password !!!", delay=2, alone=True)
  return None

# ====================== Project Functions ====================== #

def create_project(user_email):
  print_delay_alone(alone=True)
  print("\n========== Create Project ==========\n")
  
  title = input("Title: ")
  
  details = input("Details: ")
  
  target = input("Total Target (EGP): ")
  
  start_date = input("Start Date (YYYY-MM-DD): ")
  while not validate_date(start_date):
    print("Invalid date format. Please use YYYY-MM-DD !!!")
    start_date = input("Start Date (YYYY-MM-DD): ")
  
  end_date = input("End Date (YYYY-MM-DD): ")
  while not validate_end_date(start_date,end_date):
    end_date = input("End Date (YYYY-MM-DD): ")

  with open("projects.txt", "a") as file:
    file.write(f"{user_email},{title},{details},{target},{start_date},{end_date}\n")
  
  print_delay_alone(msg="Project created successfully !!!", delay=2, alone=True)

def view_projects(user_email):
  system('cls')
  try:
    print("\n========== All Projects ==========\n")
    with open("projects.txt", "r") as file:
      projects_found = 0
      for line in file:
        project_data = line.strip().split(",")
        if project_data[0] == user_email:
          print(f"### {projects_found+1} ###\nTitle: {project_data[1]}\nDetails: {project_data[2]}\nTarget: {project_data[3]} EGP\nStart: {project_data[4]}\nEnd: {project_data[5]}\n\n\n")
          projects_found += 1

      
      if projects_found == 0:
        print_delay_alone(msg="No projects found for your account !!!", delay=3)
      else:
        input(">>")  

  except FileNotFoundError:
    print_delay_alone(msg="No projects found. The projects file does not exist yet !!!", delay=3)

def edit_project(user_email):
  print_delay_alone(alone=True)
  print("\n========== Edit Project ==========\n")
  title = input("Enter the title of the project to edit : ")
  while not is_project_title(title, user_email):
    print(f"No project with name : '{title}' is FOUND !!!")
    title = input("Enter the title of the project to edit : ")

  projects = []
  with open("projects.txt", "r") as file:
    for line in file:
      project_data = line.strip().split(",")
      if project_data[0] == user_email and project_data[1] == title:
        print("Enter new details:")
        
        project_data[2] = input("Details: ")
        
        project_data[3] = input("Total Target (EGP): ")
        
        start_date = input("Start Date (YYYY-MM-DD): ")
        while not validate_date(start_date):
          print("Invalid date format. Please use YYYY-MM-DD !!!")
          start_date = input("Start Date (YYYY-MM-DD): ")
        project_data[4] = start_date
        
        end_date = input("End Date (YYYY-MM-DD): ")
        while not validate_end_date(start_date,end_date):
          end_date = input("End Date (YYYY-MM-DD): ")
        project_data[5] = end_date

      projects.append(project_data)
  
  with open("projects.txt", "w") as file:
    for project in projects:
      file.write(",".join(project) + "\n")
  
  print_delay_alone(msg=f"'{title}' updated successfully !!!", delay=3, alone=True)

def delete_project(user_email):
  print_delay_alone(alone=True)
  print("\n========== Delete Project ==========\n")
  title = input("Enter the title of the project to delete : ")
  while not is_project_title(title, user_email):
    print(f"No project with name : '{title} is FOUND !!!'")
    title = input("Enter the title of the project to delete : ")

  projects = []
  with open("projects.txt", "r") as file:
    for line in file:
      project_data = line.strip().split(",")
      if not (project_data[0] == user_email and project_data[1] == title):
        projects.append(project_data)
  
  with open("projects.txt", "w") as file:
    for project in projects:
      file.write(",".join(project) + "\n")
  
  print_delay_alone(msg=f"'{title}' deleted successfully !!!", delay=2, alone=True)

# ====================== Main Menu ====================== #

def main_menu():
  while True:
    print_delay_alone(alone=True)
    print("\n========== Crowd-Funding App ==========\n")
    print("1) Register")
    print("2) Login")
    print("3) Exit")
            
    match(input("\n>>")):
      case "1": register()
      case "2":
        user_email = login()
        if user_email:
          user_menu(user_email)
      case "3": break
      case _: print("Invalid choice. Please try again !!!")
              
              
# ====================== User Menu ====================== #

def user_menu(user_email):
  while True:
    system('cls')
    print("\n========== User Menu ==========\n")
    print("1) Create Project")
    print("2) View All Projects")
    print("3) Edit Project")
    print("4) Delete Project")
    print("5) Logout")

    match(input("\n>>")):
      case "1": create_project(user_email)
      case "2": view_projects(user_email)
      case "3": edit_project(user_email)
      case "4": delete_project(user_email)
      case "5": break
      case _: print("Invalid choice. Please try again !!!")
        
# ====================== Program Start ====================== #

main_menu()