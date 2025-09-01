from pathlib import Path

tasks = Path("Week_5")


tasks = []
def add_task(task):
    tasks.append(task)
    print(f"Task {task} added")

def completed_task(tasks):
    tasks.all(tasks)
    print(f"Tasks {tasks} completed")

def view_completed_tasks(completed_task):

    return completed_task

# edit_task = task[]


print("\nMenu options:")
print("\n1. Eating. ")
print("\n2. Reading. ")
print("\n3. Add task")

while True:
    try:
        task = input("Enter your task here: ")
        if task == "1":
            print("Eat to your satisfaction")
        # else:   
        #     print("Input a valid option")
        if task == "2":
            task = input("Enter your task here: ")
            print("Welldone")
        if task == "3":
            task = input("Enter the task you want to add: ")
            add_task(task)
            # print(f"Task {task} added")
            break
        else:
            print("try again")
            
    except ValueError:
        print("Invalid option")


# To add a priority system:
Urgency = sorted(tasks)

print(f"{Urgency}")





# Email slicer
Email = input("Enter your email address: ")
Username, domain = Email.split('@')
print(f"Username: {Username}, Domain: {domain}")

"""
Enter your email address: signage@gmail.com
Username: signage, Domain: gmail.com
"""