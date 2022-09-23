# s_count,d_count,Cl_count ,sl_count = 0,0,0,0
password = input('enter the password_____: ')
def check_password(password):
    s_count,d_count,Cl_count ,sl_count = 0,0,0,0
    if len(password) <= 16 and len(password) >=8:
        print('length is okk !!!!')
        for i in password:
            if ord(i) >=48 and ord(i) <=57 :
                d_count +=1
            if (ord(i) >=36 and ord(i) <=47) or (ord(i) >=58 and ord(i) <=64) or (ord(i)>=91 and ord(i) <= 97):
                s_count+=1
            if (ord(i) >=65 and ord(i) <=90 ):
                Cl_count+=1
            if (ord(i) >=97  and ord(i) <=122):
                sl_count+=1
        if s_count >= 1 and d_count >= 1 and Cl_count >= 1 and sl_count >= 1:
            print('strong password ')
        else:
            if s_count ==0:
                print(s_count,"is not in the password")
                check_password(input("Re enter the password-"))
            print('weak password')

    else:
        print('your passwprd length is not okk')
check_password(password)