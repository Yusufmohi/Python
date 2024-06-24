s_username="Yusuf"
s_password="132473"

uname=input("Username:")
password=input("Password:")

def validate():
    if(uname==s_username and password==s_password):
        return "True"
    else:
        return "False"

c=validate()
print(c)
