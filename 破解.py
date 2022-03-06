import zipfile
n=1
fp=zipfile.ZipFile('/Users/xbunax/Downloads/英语六级真题电子版21套（2016.12-2019.12）/全套大学英语六级（2016.12-2019.12）.zip')
password_file=open('/Users/xbunax/Downloads/crackdict/密码字典01.txt','r')
for pwb in password_file:
    pwb=pwb.rstrip()
    n = +1
    try:
        fp.extractall(path='/Users/xbunax/Downloads/英语六级真题电子版21套（2016.12-2019.12）/全套大学英语六级（2016.12-2019.12）.zip',pwb=pwb.encode())
        print("success"+pwb)
        fp.close()
        print(n)
    except:
        pass

password_file.close()
