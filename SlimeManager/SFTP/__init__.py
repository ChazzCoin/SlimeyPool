import paramiko
import pysftp
import F.OS
cnopts = pysftp.CnOpts()
# cnopts = pysftp.CnOpts(knownhosts='known_hosts')

# rsa_key = paramiko.RSAKey.from_private_key_file('~/.ssh/id_rsa', password='plant8294')


SERVER = "192.168.1.80"
PORT = 22
USERNAME = "gtvradio"
PASSWORD = "plant8294"

UTB_FOLDER = "/media/gtvradio/GTvRadio/ftp"
MEDIA_DIRECTORY = "/Users/chazzromeo/ChazzCoin/SlimeyPool/completed/"

FILES = F.OS.get_files_in_directory(MEDIA_DIRECTORY)
KEY = "/Users/chazzromeo/.ssh/id_rsa"
HKEY = "/home/gtvradio/.ssh/id_rsa"
host_key = (cnopts.hostkeys.load(KEY))

# srv = pysftp.Connection(host=SERVER, username=USERNAME, password=PASSWORD)
#
# with srv.cd('public'): #chdir to public
#     srv.put(UTB_FOLDER) #upload file to nodejs/
#
# # Closes the connection
# srv.close()

with pysftp.Connection(host=SERVER, port=PORT, username=USERNAME, password="wonderwall", private_key_pass=PASSWORD) as sftp:
    print("Connected!")
    sftp.cwd(UTB_FOLDER)  # The full path
    for file in FILES:
        print("Uploading:", file)
        sftp.put(MEDIA_DIRECTORY + file)  # Upload the file