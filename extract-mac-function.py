# Python Program to compute MAC address of host using UUID module 
  
import uuid 

# print (hex(uuid.getnode())) 

print ("Message Authentication Code : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 

# print (':'.join(re.findall('..', '%012x' % uuid.getnode()))) 