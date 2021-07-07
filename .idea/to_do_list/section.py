from to_do_list.task import Task
class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return task.details()

    def complete(self, task_name):
        task_name.completed == True
    
    def clean_section(self):
        removed_counter = 0
        for task in self.tasks:
            if task.completed == True:
                self.tasks.remove(task)
                removed_counter += 1
            return f"Cleared {removed_counter} tasks."
    
    def view_section(self):
        result = f"Section {self.name}:" + '\n'.join([x.details() for x in self.tasks])
        return result


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.clean_section())
print(section.view_section())