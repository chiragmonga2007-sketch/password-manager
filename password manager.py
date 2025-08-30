from cryptography.fernet import Fernet


'''def write_key():
     key=Fernet.generate_key()
     with open('key.key','wb') as key_file:
          key_file.write(key)'''


def load_key():
     file=open("key.key",'rb')
     key=file.read()
     file.close()
     return key

master_pwd=input('enter the master password:')
key= load_key() + master_pwd.encode()
print(key)
fer=Fernet(key)


def view():
    with open('passwords.txt','r' ) as f:
              for line in f.readlines():
                  data=line.rstrip()
                  user,pas = data.split(':')

                  print('user:',user,"| pass:",fer.decrypt(pas.encode()).decode() )

                 

def add():
    name= input('enter the username:')
    pwd=input('enter the password:')
    
    with open('passwords.txt','a') as f:
        f.write(name +':'+ fer.encrypt(pwd.encode()).decode()) 

while True:
    mode=input('please select the mode you want(vew or add) passwords, press q to quit:').lower()
    if mode == 'q':
        break
    elif mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue

