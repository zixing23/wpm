def sanitize(time_string):
    #如果'-'在time_string中，则splitter赋予'-'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' +secs)

# with open("./resource/james.txt") as jaf:
#     data = jaf.readline()
#     james = data.strip().split(',')
# with open("./resource/julie.txt") as juf:
#     data = juf.readline()
#     julie = data.strip().split(',')
# with open("./resource/mikey.txt") as mif:
#     data = mif.readline()
#     mikey = data.strip().split(',')
# with open("./resource/sarah.txt") as saf:
#     data = saf.readline()
#     sarah = data.strip().split(',')

#定义get_data函数，用于获取文件内容，文件数据已经去除空格并以','进行分隔，遇到文件不存在报错。
def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File Error: '+str(ioerr))
        return(None)

james = get_data("./resource/james.txt")
julie = get_data("./resource/julie.txt")
mikey = get_data("./resource/mikey.txt")
sarah = get_data("./resource/sarah.txt")

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])











