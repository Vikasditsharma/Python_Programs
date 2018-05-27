import re
phone_regex=re.compile(r'(?:\d{3}|\(\d{3}\))-\d{3}-\d{4}')
mo=phone_regex.findall("412-555-5566 and (412)-556-5555")
print(mo)
