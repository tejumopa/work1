rooms = open(r'Rooms.txt')  
s=rooms.readlines()  # Readlines from rooms.txt and stores it as a list
# initialized floor, capacity, time1, time2, result as null or empty
floor=[]            
capacity=[]
time1=[]
time2=[]
result=[]
# Takes each row and using split method splits each row using comma
for s1 in s:         
    s2=s1.split(',') 
    s2[-1]=s2[-1][0:-1]
    floor.append(s2[0])  # It appends s2[0], i.e floor value
    capacity.append(s2[1]) # adds s2[1], i.e capacity 
    i=2        # Here time starts at index 2
    temp=[]                 # initlalized temp to null

# Here we are assigning a pair of times say (eg: 9:00 & 9:15) , splitting it using ':'
    while i<len(s2)-1:
        s3=s2[i].split(':')
        s4 = s2[i+1].split(':')
# calculates the time & adds to temp
        temp.append([int(s3[0])*60+int(s3[1]),int(s4[0])*60+int(s4[1])])
        i=i+2       # increments the value of i-> i+2
    time1.append(temp)
print(time1)        # prints the time

# Assigning the capacity, floor, start and end time to input and splitting them and converting the time into minutes
team_capacity,current_floor,start_time,end_time=input().split(',')
start_time=int(start_time.split(':')[0])*60+int(start_time.split(':')[1])
end_time=int(end_time.split(':')[0])*60+int(end_time.split(':')[1])

# Checks each floor for capacity and next it checks for time, whether the room is available or not.
for i in range(len(floor)):     
    if(team_capacity<=capacity[i]):
        z=0
        while z<len(time1[i]):
            if (start_time>=time1[i][z][0] and end_time<=time1[i][z][1]) and i not in result:
                result.append(i)  # appends the ith floor to result
            z=z+1

# Here, it calculates min absolute floor, checking the differrence between current floor and floor of 1st row in rooms.txt
min=abs(int(current_floor)-int(floor[0].split('.')[0]))   
min_index=result[0]
for i in result:    # hold the floor which is close
    temp=abs(int(current_floor)-int(floor[i].split('.')[0]))
    if min>temp:
        min=temp
        min_index=i     # assigns the room that is closest
print(floor[min_index])
