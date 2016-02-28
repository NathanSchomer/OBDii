outputFile = open('dataFixed.bin', 'w+')

with open('data.bin', 'r') as f:
    raw_data = f.readlines()

data = []

for line in raw_data:
    val = line[11:16].replace(' ', '')
    data.append(int(val, 16))

for item in data:
      outputFile.write("%s\n" % item)
    
