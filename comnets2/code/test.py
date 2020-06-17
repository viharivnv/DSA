import Routing as r
import HostDictionary as hD

c=r.Routing("")
key_list = list(hD.hostDic.keys()) 
val_list = list(hD.hostDic.values())
for value in hD.hostDic.values():
        if value[0]=='127.0.0.1':
            print(val_list.index(value))
            print(key_list[val_list.index(value)])
            
            

send

count 5
while(count>0)            
if data:
    print("recived")
    break
else:
    count-=1
    
    
receive
while (t<10):
  if(t==4):  
      send
  else    