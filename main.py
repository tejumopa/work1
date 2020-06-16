rooms = open(r'Rooms.txt')
s=rooms.readlines()
floor=[]
capacity=[]
time1=[]
time2=[]
result=[]
for s1 in s:
    s2=s1.split(',')
    s2[-1]=s2[-1][0:-1]
    floor.append(s2[0])
    capacity.append(s2[1])
    i=2
    temp=[]
    while i<len(s2)-1:
        s3=s2[i].split(':')
        s4 = s2[i+1].split(':')

        temp.append([int(s3[0])*60+int(s3[1]),int(s4[0])*60+int(s4[1])])
        i=i+2
    time1.append(temp)
print(time1)
team_capacity,current_floor,start_time,end_time=input().split(',')
start_time=int(start_time.split(':')[0])*60+int(start_time.split(':')[1])
end_time=int(end_time.split(':')[0])*60+int(end_time.split(':')[1])
for i in range(len(floor)):
    if(team_capacity<=capacity[i]):
        z=0
        while z<len(time1[i]):
            if (start_time>=time1[i][z][0] and end_time<=time1[i][z][1]) and i not in result:
                result.append(i)
            z=z+1
min=abs(int(current_floor)-int(floor[0].split('.')[0]))
min_index=result[0]
for i in result:
    temp=abs(int(current_floor)-int(floor[i].split('.')[0]))
    if min>temp:
        min=temp
        min_index=i
print(floor[min_index])