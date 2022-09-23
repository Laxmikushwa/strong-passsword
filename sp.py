def chkps(password):
    s_count,d_count,Cl_count ,sl_count = 0,0,0,0
    if len(password) <= 16 and len(password) >=8:
        print('length is okk !!!!')
        for i in password:
            if ord(i) >=48 and ord(i) <=57 :
                d_count +=1
            if (ord(i) >=36 and ord(i) <=47) or (ord(i) >=58 and ord(i) <=64) or (ord(i)>=91 and ord(i) < 97):
                s_count+=1
            if (ord(i) >=65 and ord(i) <=90 ):
                Cl_count+=1
            if (ord(i) >=97  and ord(i) <=122):
                sl_count+=1
        if s_count >= 1 and d_count >= 1 and Cl_count >= 1 and sl_count >= 1:
            print('strong password ')
        else:
            if d_count == 0 :
                print('digit is not there')
            if s_count == 0 :
                print('symbol is not there')
            if Cl_count == 0 :
                print('Capitial latter is not there')
            if sl_count == 0 :
                print('small latter is not there')
            chkps(input('Re-Enter Password___:'))
    else:
        print('your passwprd length is not okk')
        chkps(input('Re-Enter Password___:'))
password = input('enter the password___: ')
chkps(password)