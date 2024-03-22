fp=open("192311102.txt","r")
line_count=0
for line in fp:
    if line_count<3:
        print(line)
        line_count+=1
    else:
        break
  
