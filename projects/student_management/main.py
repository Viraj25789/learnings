from utils import add_student,view_all_students,search_student,maximum_marks,delete_student,update_marks,statics

while True:

    print("1. Add student")
    print("2. View all students")
    print("3. Search student")
    print("4. Student with maximum marks")
    print("5. Delete student ")
    print("6. Update marks ")
    print("7. Statics")
    print("8. Exit")
    
    choice= input("Enter your choice: ")

    if choice=="1":
        add_student()

    elif choice=="2":
        view_all_students()

    elif choice=="3":
        search_student()

    elif choice=="4":
        maximum_marks()
        
    elif choice=="5":
        delete_student()

    elif choice=="6":
        update_marks()
    
    elif choice=="7":
        statics()

    elif choice=="8":
        break

