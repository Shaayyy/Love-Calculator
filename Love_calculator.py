name1=input("Enter the first name: ").lower()
name2=input("Enter the second name: ").lower()
name=name1+name2
count1=name.count("t")+name.count("r")+name.count("u")+name.count("e")
count2=name.count("l")+name.count("o")+name.count("v")+name.count("e")
count=count1*10+count2
print(str(count)+"%")