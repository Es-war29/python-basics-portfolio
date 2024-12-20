import json
def main():
    print("Welcome to the To-Do List App")
    tasks= []   # list to store tasks

    while True:
        print("\n-------Menu-------")
        print("1. New Task")
        print("2. View Tasks")
        print("3. Completed Tasks")
        print("4. Exit")

        choice = input("Select an option:")
        if choice == '1':
            new_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            completed_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("GoodBye!")
            break
        else:
            print("Invalid Option. Please select a valid option")

def new_task(tasks):
    print("Enter your tasks one by one. Type 'q' when you are finished:")
    while True:
        task = input("Enter the task or 'q' to quit:").strip()
        if task.lower() == 'q':
            print("Finished adding tasks.")
            break
        elif task:
            task_id = len(tasks)+1
            tasks.append({"task":task,"done":False})
            print(f"{task_id}.Task '{task}' added!")

        else:
            print("Task cannot be empty. Please add an valid task")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks,1):
        status = "Done" if task["done"] else "Not Done"
        print(f"{i}. {task['task']} [{status}]")

def completed_tasks(tasks):

    if not tasks:
        print("No Tasks to mark as complete.")
        return
    print("Enter the task numbers to mark as completed or Type 'q' when finished:")
    while  True:
        view_tasks(tasks)
        task_input = input("Enter Task number to mark as completed or Type 'q' to quit ")
        if task_input.lower() == 'q':
            print("Finished marking tasks as completed.")
            break
        try:
            task_num = int(task_input)
            if  1 <= task_num <= len(tasks):
                if not tasks[task_num - 1]["done"]:
                    tasks[task_num - 1 ]["done"] = True
                    print(f"Task '{tasks[task_num - 1] ['task']}' marked as complete!")
                else:
                    print(f"Task '{tasks[task_num - 1]['task']}' is already completed.")
            else:
                print("Invalid task number! Please enter a valid task number.")
        except ValueError:
            print("Please enter a valid task number or type 'q' to finish")



def save_tasks(tasks):
    try:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
        print("Tasks saved successfully.")
    except IOError:
        print("Error saving tasks.")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading tasks file. Starting with an empty list.")
        return []
if __name__=="__main__" :
    main()


