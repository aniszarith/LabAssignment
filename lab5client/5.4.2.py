from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.56.108',  #Your Server IP
    'username': 'aniszarith', #your Server Username
    'password': 'zuho1996', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('sudo apt-get update')
print(output)
