import re
email_regex=re.compile(r'[\d\w]{5,30}@[\d\w]{3,30}\.(?:com|co.in|biz|in)')
mo=email_regex.findall("vikasditsharma@gmail.com is the email vik@gnail.com bu actual is vijay12@hotmail.com or may be vik_1985@xyz.in")
print(mo)

for item in mo:
    print(item)
    output_file=open("C:\\Users\\E740487\\Documents\\Python\\Videos\\Python_Program\\list.txt",'a')
    output_file.write("\n" +item)
    output_file.close()


