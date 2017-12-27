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

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return({'Name' :templ.pop(0),
                'DOB' :templ.pop(0),
                'times':str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    except IOError as ioerr:
        print("File Error: "+str(ioerr))
        return(None)
sarch = get_data("./resource/sarah2.txt")
print(sarch['Name'] + "'s fastest times are: " + sarch['times'])






