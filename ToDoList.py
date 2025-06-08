# To-do List

listTask = []
completedTask = []
running = True

print('''
Choose:

1. Add Task
2. View Tasks
3. Delete Task
4. Mark Task as Complete
5. Exit
''')

while running:
    try:
        chooseTask = int(input('> '))
    except ValueError:
        print("Please enter a valid number (1-5).")
        continue

    if chooseTask == 5:
        sure = input('Are you sure you want to exit (Y/N)? ')
        if sure.lower() == 'y':
            print("Goodbye!")
            break

    elif chooseTask == 1:
        addTask = input('Enter next task: ')
        listTask.append(addTask)

    elif chooseTask == 2:
        if not listTask:
            print('No task logged yet.')
        else:
            print('\nTo-Do Tasks:')
            for i, task in enumerate(listTask):
                print(f"{i}. {task}")
            print()

    elif chooseTask == 3:
        if not listTask:
            print('No tasks to delete.')
            continue
        for i, task in enumerate(listTask):
            print(f"{i}. {task}")
        try:
            deleteTask = int(input('Select index of task to delete: '))
            deleted = listTask.pop(deleteTask)
            print(f'Task "{deleted}" deleted successfully.')
        except (IndexError, ValueError):
            print('Invalid index.')

    elif chooseTask == 4:
        if not listTask:
            print('No tasks to complete.')
            continue
        for i, task in enumerate(listTask):
            print(f"{i}. {task}")
        try:
            completeTask = int(input('Select index of task to mark as complete: '))
            completed = listTask.pop(completeTask)
            completedTask.append(completed)
            print(f'Task "{completed}" marked as complete.')
            print(f'Tasks completed: {completedTask}')
        except (IndexError, ValueError):
            print('Invalid index.')

    else:
        print('Please choose a number from 1 to 5.')
