from cryptography.fernet import Fernet

'''
#create a key for cryptography
#commented because it's only needed to run the function once, to get the key
def write_key():
    key = Fernet.generate_key()
    # wb stands for writing bytes
    with open("C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\PasswordManager\\key.key","wb") as key_file:
        key_file.write(key)
''' 

def load_key(): 
    #rb stands for reading bytes
    file = open("C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\PasswordManager\\key.key","rb")
    key = file.read()
    file.close()
    return key


def view():
    with open('C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\PasswordManager\\password.txt',"r") as f:#w cleans the file and write from the beggining, a keeps writting from the end
        for line in f.readlines():
            data = line.rstrip()# rstrip strips out the '\n' from the line
            user, passw = data.split("|")
            print("#---------------#")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())
        print("#---------------#")
        
        
def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    
    with open('C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\PythonProjects\\PasswordManager\\password.txt',"a") as f:#w cleans the file and write from the beggining, a keeps writting from the end
        f.write(name + " | " + fer.encrypt(pwd.encode()).decode()  + "\n")#encode turns pwd into bytes



master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)#initializing the encryption module

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit: ")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue