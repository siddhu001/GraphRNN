file=open("result_caveman_small/result_caveman_4_4_128_16_64_4.txt")
min_degree=100
min_value=''
for line in file:
	if "degree" in line:
		line1=line.rstrip().split(" ")
		if (float(line1[3])<min_degree):
			min_degree=float(line1[3])
			min_value=line
print(min_value)
file=open("result_caveman_small/result_caveman_4_4_128_16_64_8.txt")
min_degree=100
min_value=''
for line in file:
	if "degree" in line:
		line1=line.rstrip().split(" ")
		if (float(line1[3])<min_degree):
			min_degree=float(line1[3])
			min_value=line
print(min_value)
file=open("result_caveman_small/result_caveman_4_4_128_16_64_16.txt")
min_degree=100
min_value=''
for line in file:
	if "degree" in line:
		line1=line.rstrip().split(" ")
		if (float(line1[3])<min_degree):
			min_degree=float(line1[3])
			min_value=line
print(min_value)
file=open("result_caveman_small/result_caveman_4_4_128_16_64_32.txt")
min_degree=100
min_value=''
for line in file:
	if "degree" in line:
		line1=line.rstrip().split(" ")
		if (float(line1[3])<min_degree):
			min_degree=float(line1[3])
			min_value=line
print(min_value)