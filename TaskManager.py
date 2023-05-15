

tasks = [

    {'name' : 'Build Resume', 'completed' : 'True'},
    {'name' : 'Secure a Cybersecurity Profession', 'completed' : 'False'}

]

def list_tasks():
    for index, task in enumerate(tasks):
        print(str.format('{}: {} (Completed: {})', index, task['name'], task['completed']))


def add_task():
    task_text = input('Please add a new task: ')
    new_tasks = {"name": task_text, "completed": False}
    tasks.append(new_tasks)
    
   
   
def remove_task():
    print(list_tasks())
    remove_tasks = int(input('Please select the task you want removed: ' ))
    del tasks[remove_tasks]
    


def mark_task_complete():
    print(list_tasks())
    completed_tasks = int(input("Please select the task that is to be marked completed: " ))
    tasks[completed_tasks]["completed"] = True



def mark_task_not_complete():
    print(list_tasks())
    Remark_tasks =  int(input("Please select the number tasks that is not completed: " ))
    tasks[Remark_tasks]["completed"] = False


menu_text = """

────────────────────────────────
───────────────██████████───────
──────────────████████████──────
──────────────██────────██──────
──────────────██▄▄▄▄▄▄▄▄▄█──────
──────────────██▀███─███▀█──────
█─────────────▀█────────█▀──────
██──────────────────█───────────
─█──────────────██──────────────
█▄────────────████─██──████
─▄███████████████──██──██████ ──
────█████████████──██──█████████
─────────────████──██─█████──███
──────────────███──██─█████──███
──────────────███─────█████████
──────────────██─────████████▀
────────────────██████████
────────────────██████████
─────────────────████████
──────────────────██████████▄▄
────────────────────█████████▀
─────────────────────████──███
────────────────────▄████▄──██
────────────────────██████───▀
────────────────────▀▄▄▄▄▀


1. List the tasks
2. Add a task
3. Remove a task
4. Mark task complete
5. Remark a task to do
6. Quit


What would you like to do? """



program_is_running = True 

while program_is_running:
    decision = input(menu_text)
    if decision == '0':
        print('Tasks is empty!')
    elif decision == '1':
        list_tasks()
    elif decision == '2':
        add_task()
        print(' ')
        print(' ')
        print('Please let this be a normal new task (brain cells) - NO WAY!!! CRUSIN DOWN MAIN STREET.....')
      
    elif decision == '3':
        remove_task()
        print(' ')
        print(' ')
        print('Hit the road Jack, And dont you come back no more no more no more no more!')
     
    elif decision == '4':
        mark_task_complete()
        print(' ')
        print(' ')
        print('I HAVE THE POWER !!!!!!!!!!!! FLASH !! GORDON!!!!!!!!!!!!!!!!!!!!')
       
    elif decision == '5':
        mark_task_not_complete()
        print(' ')
        print(' ')
        print(" I'LL BE BACK .... ")
            
    elif decision == '6':    
        program_is_running = False
    else:
        print('Please choose valid option')










