from telnetlib import Telnet
import time


def telnet(host:str,username:str,password:str,lista_comando:list,prompt:str='#'):
    with Telnet(host, 23) as tn:
        tn.read_until(b"Username:")
        tn.write(f'{username}\n'.encode('utf-8'))
        tn.read_until(b"Password:")
        tn.write(f'{password}\n'.encode('utf-8'))
        tn.read_until(f'{prompt}'.encode('utf-8'))
        for comando1 in lista_comando:
            time.sleep(0.2)
            cmd_1 = f'{comando1}\n'.encode('utf-8')
            tn.write(cmd_1)
            time.sleep(0.1)
        ret = tn.read_very_eager().decode('utf-8')
        print(ret)
    tn.close()
        


if __name__ == '__main__':

    lista_comandos = ['conf t', 'show ip route', 'end', 'exit', 'yes']


    telnet('xx.xxx.xxx.xxx','admin','admin', lista_comandos)
