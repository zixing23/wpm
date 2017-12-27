def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
        (mins, secs) = time_string.split(splitter)
    elif ':' in time_string:
        splitter = ':'
        (mins, secs) = time_string.split(splitter)
    else:
        return(time_string)
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

clean_james = []
clean_julie = []
clear_mikey = []
clear_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))
for each_t in julie:
    clean_julie.append(sanitize(each_t))
for each_t in mikey:
    clear_mikey.append(sanitize(each_t))
for each_t in sarah:
    clear_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clear_mikey))
print(sorted(clear_sarah))








