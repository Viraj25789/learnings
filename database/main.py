from database.database import insert_student,update_student,delete_student,all_students,search_student


while True:

    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update Student")
    print("5. Delete student ")
    print("6. Exit ")
  
    
    choice= input("Enter your choice: ")

    if choice=="1":
        insert_student()

    elif choice=="2":
        all_students()

    elif choice=="3":
        search_student()

    elif choice=="4":
        update_student()
        
    elif choice=="5":
        delete_student()

    elif choice=="6":
        break


