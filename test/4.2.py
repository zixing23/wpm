class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times
    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])
    def add_time(self,time_value):
        self.times.append(time_value)
    def add_times(self,list_of_times):
        self.times.extend(list_of_times)
def sanitize(time_string):
    # 如果'-'在time_string中，则splitter赋予'-'
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

def get_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            templ = data.strip().split(',')
        return(Athlete(templ.pop(0),templ.pop(0),templ))
    except IOError as ioerr:
        print("File Error: " + str(ioerr))
        return (None)

sarch = get_data("./resource/sarah2.txt")
print(sarch.name + "'s fastest times are: " + str(sarch.top3()))




