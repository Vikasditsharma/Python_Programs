import pyperclip
file1=open("C:\\Users\\E740487\\Documents\\Python\\Videos\\Python_Program\\pyperclip.txt",'w')
mo=pyperclip.paste()

file1.write(mo)
file1.close()

file1=open("C:\\Users\\E740487\\Documents\\Python\\Videos\\Python_Program\\pyperclip.txt",'r')
for item in file1.readlines():

    if(len(item.strip())==0):
        continue

    print("*"+item,end="")
    
