server1=["gbl06671","gbl06672","gbl06673","gbl06674","gbl06675"]
server2=["hk06671","hk06672","hk06673","hk06674","hk06675"]
print(server1)
print(server2)
server=server1+server2
print(server)
print(server1[1])
server1[0]="us656565"
print(server1)
del server1[0]
print(server1)
print("Length Of List is",len(server))
number=[1,2,3,4,5,6,7,8,9]
print("Maximum Number in list",max(number))
print("Manimum Number in list",min(number))
print("Reverse List",number.pop(5))
print("After Pop from list",number)

server_append=[]
title=["Server_Name","IP_Address","Superstack_Version","Operating_System"]
s1=["gbl06662","182.17.6.20","rhel_2.7.3","Linux"]
s2=["gbl06663","182.17.6.21","rhel_2.7.3","Linux"]
server_append.append(title)
server_append.append(s1)
server_append.append(s2)
for l in server_append:
    print(l[0],l[1],l[2],l[3])