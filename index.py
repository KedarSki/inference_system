frontend_list = ['HTML', 'CSS', 'JavaScript', 'PHP']
object_oriented_list = ['C', 'C++', 'C#', 'Java', 'Go']
database_list = ['MySQL', 'SQL Server', 'PostgreSQL', 'Oracle', 'MongoDB']
mobile_list = ['Kotlin', 'React Native', 'Java', 'Scala', 'Dart']
ios_list = ['Swift']
result_list = []

helper_answer = False

print(f'Hello! Welcome to Inference System will help you find programming language you should learn based on your interests.'
      '\nPlease help us to find right tech-stack for you and answer few questions')
while True:
    web_app_q = input("Do you want to make websites? y/n: ")
    mobile_app_q = input("Do you want to make mobile apps? y/n: ")
    ios_q = input("Do you want to make application for apple device? y/n: ")
    backend_q = input("Do you want to make application but do not participate with design? y/n: ")

    if web_app_q == 'y':
        helper_answer = True
        result_list += frontend_list
    elif mobile_app_q == 'y':
        helper_answer = True
        result_list += mobile_list
    elif ios_q == 'y':
        helper_answer = True
        result_list += ios_list
    elif backend_q == 'y':
        helper_answer = True
        result_list += object_oriented_list
    elif backend_q == 'y' or ios_q == 'y':
        print(f"After you'll learn above the suggestion is to learn following:{database_list}")
    elif helper_answer == True:
        print(f"Programming language chosen according to your preference{result_list}")
    elif helper_answer == False:
        break


