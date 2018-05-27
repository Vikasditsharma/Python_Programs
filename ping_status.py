import os

domain_list=open("/root/domain_list.txt",'r')
for item in domain_list:
    output=os.system('ping -c 3 {}'.format(item))
    if(output==0):
        success_status=open("/root/success_ping.txt",'a')
        success_status.write(item)
        success_status.close()
    else:
        failed_status=open("/root/failed_ping.txt",'a')
        failed_status.write(item)
        failed_status.close()

    
    
