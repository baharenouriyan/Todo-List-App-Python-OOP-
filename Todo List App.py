class TaskManager:
    
    def init(self, file_name):
        self.file_name = file_name

    def add_task(self, task):
        with open(self.file_name, "a") as file:
            file.write(task + " | Pending\n")

    def view_tasks(self):
        try:
            with open(self.file_name, "r") as file:
                tasks = file.readlines()

                if not tasks:
                    print("No tasks found.")
                    return

                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")

        except FileNotFoundError:
            print("Task file not found.")

    def complete_task(self, task_number):
        try:
            with open(self.file_name, "r") as file:
                tasks = file.readlines()

            if 0 < task_number <= len(tasks):
                tasks[task_number-1] = tasks[task_number-1].replace("Pending", "Done")

                with open(self.file_name, "w") as file:
                    file.writelines(tasks)

                print("Task marked as completed!")

            else:
                print("Invalid task number.")

        except FileNotFoundError:
            print("File not found.")

    def delete_task(self, task_number):
        try:
            with open(self.file_name, "r") as file:
                tasks = file.readlines()

            if 0 < task_number <= len(tasks):
                tasks.pop(task_number-1)

                with open(self.file_name, "w") as file:
                    file.writelines(tasks)

                print("Task deleted!")

            else:
                print("Invalid task number.")

        except FileNotFoundError:
            print("File not found.")


manager = TaskManager("tasks.txt")

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Complete Task")
    print("4.Delete Task")
    print("5.Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        manager.add_task(task)

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        num = int(input("Task number: "))
        manager.complete_task(num)

    elif choice == "4":
        num = int(input("Task number: "))
        manager.delete_task(num)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
