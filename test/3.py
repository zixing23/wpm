james_list=[]
julie_list=[]
mikey_list=[]
sarah_list=[]
with open("./resource/james.txt") as james_db:
    for each_item in james_db:
        james_list.append(each_item)
print("james:",james_list)

with open("./resource/julie.txt") as julie_db:
    for each_item in julie_db:
        julie_list.append(each_item)
print("julie:",julie_list)

with open("./resource/mikey.txt") as mikey_db:
    for each_item in mikey_db:
        mikey_list.append(each_item)
print("mikey:",mikey_list)

with open("./resource/sarah.txt") as sarah_db:
    for each_item in sarah_db:
        sarah_list.append(each_item)
print("sarch:",sarah_list)
