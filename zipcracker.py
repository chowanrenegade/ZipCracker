import zipfile

def extractFile(zfile, password):
    try:
        zfile.extractall(pwd=bytes(password, 'utf-8'))
        return password
    except:
        print('wrong password')
        return

#Make sure .zip file and password list .txt file are typed bellow 


def main():
    zfile = zipfile.ZipFile('bannergrabber.zip')
    passFile = open('passwords.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zfile, password)
        if guess:
            print('Password = '+ password)
            break

if __name__ == '__main__':
    main()