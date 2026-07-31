total_task = 4
task_num = 1
while task_num <= total_task:
    if task_num == 1:
        next_task = "make your bed"
    elif task_num == 2:
        next_task = "brush your teeth"
    elif task_num == 3:
        next_task = "eat breakfast"
    else:
        next_task = "get dressed"
    answer = input(f"Have you finished {next_task}? (yes/no): ")
    print()
    if answer.lower() == "yes":
        print(f"Great! You have completed task {task_num}: {next_task}.")
        task_num += 1 
    else:
        print(f"Please complete task {task_num}: {next_task} before moving on.")