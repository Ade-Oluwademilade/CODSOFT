#!/usr/bin/python3

class ToDoApp:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append({"task": task, "done": False})
        print(f"Added: '{task}'")

    def viewTask(self):
        if not self.tasks:
            print("No tasks has been added yet. Try adding a new task.")
            return
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['task']} [{status}]")

    def markTaskAsDone(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1]["done"] = True
            print(f"Marked task {task_id} as done.")
        else:
            print("Invalid task id.")

    def delTask(self, task_id):
        if 0 < task_id <= len(self.tasks):
            removed_task = self.tasks.pop(task_id - 1)
            print(f"Deleted: '{removed_task['task']}'")
        else:
            print("Invalid task id.")

    def run(self):
        while True:
            print("\nTo-Do List App")
            print("1. Add a Task")
            print("2. View Tasks")
            print("3. Mark a Task as Done")
            print("4. Delete a Task")
            print("5. Exit App")
            try:
                options = int(input("Choose an option: "))
                if options == 1:
                    task = input("Add task: ")
                    self.addTask(task)
                elif options == 2:
                    self.viewTask()
                elif options == 3:
                    task_id = int(input("Enter task id to mark the task as done: "))
                    self.markTaskAsDone(task_id)
                elif options == 4:
                    task_id = int(input("Enter task id to delete the task: "))
                    self.delTask(task_id)
                elif options == 5:
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
            except ValueError:
                print("Please enter a valid task id.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()