import fonc
print('------------Network Scanner 1.0------------')
print('[*] Choice an option')
print('1 - Scan local network')
choice=int(input())
scanSpeed=int(input('[*] Choose testing delay(100+ if you want to be sure to detect everything)\n'))
if(choice==1):
        fonc.scan(scanSpeed,'255.255.255.0')
