file1 = open(file='text.txt', mode='r',encoding='utf-8')
lines = file1.readlines()
  
count = 0

for line in lines:
    count += 1
    print("Line {}: {}".format(count, line.strip()))

