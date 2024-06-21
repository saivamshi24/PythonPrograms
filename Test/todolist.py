class Task:
    def __init__(self, description, status="Not Completed"):
        self.description = description
        self.status = status

    def __str__(self):
        return f"Task: {self.description}, Status: {self.status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' added successfully.")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")

    def update_task(self, task_number, new_description=None, new_status=None):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if new_description:
                task.description = new_description
            if new_status:
                task.status = new_status
            print(f"Task {task_number} updated successfully.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task.description}' deleted successfully.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            todo_list.display_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_description = input("Enter new description (or leave blank to keep current): ")
            new_status = input("Enter new status (or leave blank to keep current): ")
            todo_list.update_task(task_number, new_description or None, new_status or None)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
