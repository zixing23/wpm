man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role,line_spoken) = each_line.split(':',1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The data file is missing!')
try:
    with open("man_data.txt",'w') as man_file:
        print(man, file=man_file, end='')
    with open("other_data.txt",'w') as other_file:
        print(other,file=other_file,end='')
except IOError as err:
    print('File error: ' +str(err))

with open('man_data.txt') as mdf:
    print(mdf.readline())




