marks={'Class A':{'muthu':{'English':80,'Maths':70,'Tamil':90}
              ,'lokesh':{'English':90,'Maths':100,'Tamil':60}
              ,'deena':{'English':60,'Maths':80,'Tamil':95}},
            'Class B':{'gowtham':{'English':85,'Maths':75,'Tamil':95}
              ,'akash':{'English':96,'Maths':86,'Tamil':66}
              ,'ashwin':{'English':67,'Maths':87,'Tamil':97}}}
choice=0
while(choice !=4):
    print("1.Show the student list")
    print("2.Show the class topper")
    print("3.show the school topper")
    print("4.Exit")
    choice=int(input("Enter the choice : "))
    if(choice==1):
        for k,v in marks.items():
            rollno=1
            print(k)
            for key,value in v.items():
                print("{} : {}".format(rollno,key))
                rollno+=1
            print()
        std_marks="yes"
        while(std_marks!="no"):
            std_marks=input("Do you need to see the marks of the student? yes/no \n")
            if(std_marks=="yes"):
                std_marks=input("Enter student name:")
                s_marks = {
                        name_k: name_v
                        for class_k, class_v in marks.items()
                        for name_k, name_v in class_v.items()
                        for sub_k, sub_v in name_v.items()
                    }
                student = s_marks[std_marks]
                mark_sum_list = []
                print("\n{:<10} ===> {:>8}".format("Subject", "Marks"))

                for k, v in student.items():
                    print("{:<10} ===> {:>5}".format(k, v))
                    mark_sum_list.append(v)

                avg = (sum(mark_sum_list)//len(mark_sum_list))

                print("\nTotal of {} is {} \n".format(std_marks, sum(mark_sum_list)))
                mark_sum_list = []
                print("Average of {} is {} \n".format(std_marks, avg))
            else:
                break
    if choice == 2:

        toppers_list_in_class = {ck:{nk:sum(nv.values()) for nk, nv in cv.items()} for ck, cv in marks.items()}
        class_topper = {k:max(v.items(),key = lambda x:x[1]) for k,v in toppers_list_in_class.items()}
        for key,value in toppers_list_in_class.items():
            print("\n{}\n".format(key))
            for k,v in sorted(value.items(),reverse = True):
                print("{:<10}==>{:>10}".format(k,v))
            print("\n{} topper is {}".format(key,class_topper[key]))
    if choice == 3:
        toppers_list = {nk: sum(nv.values()) for ck, cv in marks.items() for nk, nv in cv.items()}
        toppers = {k: v for k, v in sorted(toppers_list.items(), key=lambda x: x[1], reverse=True)}
        print("{:<10}{:>12} \n".format("Name","Total"))
        for k,v in toppers.items():
            print("{:<10} ==> {:>5} ".format(k,v))
        print("\nSchool topper is : {} \n".format(max(toppers.items(), key=lambda x: x[1])))

   
