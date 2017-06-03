import subprocess
from socket import *
from re import search
import os

def scan(scanSpeed,mask):
    Tab=[]
    limit=int(input('[*] Enter scan limit : '))
    nullPrint=open(os.devnull,'w')
    if (mask=='255.255.255.0'):
        for i in range(1,limit+1):
            PipeRes=subprocess.Popen('timeout {} ping -c 1 192.168.43.'.format(scanSpeed/1000)+str(i),shell=True,stdout=subprocess.PIPE)# On ping chaque IP pour connaître sa disponiblité

            res, errors=PipeRes.communicate()
            res=res.decode()

            if(search('0% packet loss',res)==None): # Si on voit que l'output du ping contient pas '0% loss', on ne valide pas l'IP
                print('No')
            else: # Sinon, on valide
                Tab.append('192.168.43.'+str(i))
            os.system('clear')
            print('\r{}/{}'.format(i,limit),end='')

    os.system('clear')
    print(len(Tab))
    for ip in Tab:
        try:
            print('{} | {}'.format(ip,gethostbyaddr(ip)[0]))
        except herror:
            print('{} | Unknown'.format(ip))
