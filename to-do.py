class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the list.")

    def edit_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]
            self.tasks[task_number - 1] = new_task
            print(f"Task '{old_task}' updated to '{new_task}'.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed from the list.")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List App")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '3':
            task_number = int(input("Enter the task number to edit: "))
            new_task = input("Enter the new task: ")
            todo_list.edit_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
