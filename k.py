class TodoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("Your tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

    def delete_task(self, index):
        try:
            removed_task = self.tasks.pop(index - 1)
            print(f'Task "{removed_task}" removed.')
        except IndexError:
            print("Invalid task number.")

def main():
    todo_list = TodoList()
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "_main_":
    main()