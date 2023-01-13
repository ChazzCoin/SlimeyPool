import inventory as inventory
import paramiko

rsa_key = paramiko.RSAKey.from_private_key_file('~/.ssh/the_key', password='plant8294')
transport = paramiko.Transport((inventory[0], 8055))
transport.connect(username='theUser', pkey=rsa_key)
sftp = paramiko.SFTPClient.from_transport(transport)
print(sftp.listdir())