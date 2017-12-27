def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' +secs)

with open("./resource/james.txt") as jaf:
    data = jaf.readline()
    james = data.strip().split(',')
with open("./resource/julie.txt") as juf:
    data = juf.readline()
    julie = data.strip().split(',')
with open("./resource/mikey.txt") as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open("./resource/sarah.txt") as saf:
    data = saf.readline()
    sarah = data.strip().split(',')

unique_james = []
for each_t in sorted([sanitize(t) for t in james]):   #使用了列表推导，把james的数据进行排序，同时使用了for遍历
    if each_t not in unique_james:                    #如果james中的数据不在unique_james中，则追加到unique_james
        unique_james.append(each_t)
print(unique_james[0:3])                              #结果是把james不重复的速度最快的前三数据给抓取出来