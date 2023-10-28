import csv
with open('student.csv',mode='a') as csvfile:
    mywriter=csv.writer(csvfile,delimiter=',')
    ans='y'
    ans=input("Do you want to Add Details of the Employee?(y/n):")
    while ans.lower()=='y':
     rno=int(input("Enter Student Register Number: "))
     name=input("Enter Student Name: ")
     math=int(input("Enter Student Math Marks: "))
     cse=int(input("Enter Student Computer Science Marks: "))
     chem=int(input("Enter Student Chemistry Marks: "))
     phy=int(input("Enter Student Physics Marks: "))
     eng=int(input("Enter Student English Marks: "))
     total=math+cse+chem+phy+eng
     percent=(total/500)*100
     mywriter.writerow([rno,name,math,cse,chem,phy,eng,total,percent])
     ans=input("Do you want to Add more?(y/n):")
    ans='y'
with open('student.csv',mode='r') as csvfile:
    myreader=csv.reader(csvfile,delimiter=',')
    while ans=='y':
        e=int(input("Enter Student Register Number to Search: "))
        for row in myreader:
            if len(row)!=0:
                if int(row[0])==e:
                    print("#######################################")
                    print("Student Register Number: ",row[0])
                    print("Student Name: ",row[1])
                    print("#################MARKS#################")
                    print("Maths Marks: ",row[2])
                    print("Computer Science Marks: ",row[3])
                    print("Chemistry Marks: ",row[4])
                    print("Physics Marks: ",row[5])
                    print("English Marks: ",row[6])
                    print("Total Marks: ",row[7])
                    print("Total Percentage: ",row[8])
                    print("#######################################")
                    break
                else:
                    print("#######################################")
                    print("#############EMP NOT FOUND#############")
                    print("#######################################")
        ans=input("Do you want to Add Details of the Employee?(y/n):")