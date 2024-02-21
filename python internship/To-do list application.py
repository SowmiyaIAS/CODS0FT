# Agenda Application

# Function to exhibit the card
def exhibit_card():
    print("Agenda Application")
    print("a. Visit Agenda")
    print("b. Attach Task")
    print("c. Improve Task")
    print("d. Mark Task as finished")
    print("e. Remove Task")
    print("f. Leave")

# Function to visit the Agenda
def visit_Agenda(Agenda):
    print("Agenda:")
    if not Agenda:
        print("No tasks")
    else:
        for idx, task in enumerate(Agenda,1):
            print(f"{idx}. {task}")

# Function to Attach a task
def Attach_task(Agenda):
    task = input("Enter task: ")
    Agenda.append(task)
    print("Task Attached successfully!")

# Function to Improve a task
def Improve_task(Agenda):
    visit_Agenda(Agenda)
    idx = int(input("Enter task number to Improve: "))-1
    if 0 <= idx < len(Agenda):
        new_task = input("Enter new task: ")
        Agenda[idx] = new_task
        print("Task Improved successfully!")
    else:
        print("Unwell task number")

# Function to mark a task as finished
def mark_finished(Agenda):
    visit_Agenda(Agenda)
    idx = int(input("Enter task number to mark as finished: "))-1
    if 0 <= idx < len(Agenda):
        print("Task '{Agenda[idx]}' marked as finished!")
        del Agenda[idx]
    else:
        print("Unwell task number")

# Function to Remove a task
def Remove_task(Agenda):
    visit_Agenda(Agenda)
    idx = int(input("Enter task number to Remove: ")) - 1
    if 0 <= idx < len(Agenda):
        print(f"Task '{Agenda[idx]}' Removed!")
        del Agenda[idx]
    else:
        print("Unwell task number")

def main():
    Agenda = []
    while True:
        exhibit_card()
        option = input("Enter your option: ")
        if option == 'a':
            visit_Agenda(Agenda)
        elif option == 'b':
            Attach_task(Agenda)
        elif option == 'c':
            Improve_task(Agenda)
        elif option == 'd':
            mark_finished(Agenda)
        elif option == 'e':
            Remove_task(Agenda)
        elif option == 'f':
            print("Thank you for using the Agenda Application!")
            break
        else:
            print("Unwell option. Please try again.")

if __name__ == "__main__":
    main()
