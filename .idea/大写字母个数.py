import string
s='Watch Sizing Guide Colossal design that packs quite a punch. Made in USA or Imported.Case size: 59mm; Band size: 26mm; quartz movement with 3-hand analog display, date window, and 3 chronograph subdials; iridescent mineral crystal face.'
c=0
d={}
for i in range(len(s)-1):
    if s[i] in string.ascii_uppercase:
        if s[i+1] not in string.ascii_uppercase:
            d['大写']=d.get('大写',0)+1
print(d)