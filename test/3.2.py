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

print(sorted([sanitize(each_t) for each_t in james]))
print(sorted([sanitize(each_t) for each_t in julie]))
print(sorted([sanitize(each_t) for each_t in mikey]))
print(sorted([sanitize(each_t) for each_t in sarah]))










