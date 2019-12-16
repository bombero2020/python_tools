import pyAesCrypt
from os import stat, remove, path
import sys, getpass

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


# file to encrypt
file_path = "C:\\Users\\Marcelo\\Documents\\cuentas.txt"


# encrypt
def encrypt():
    if path.exists(file_path):
        password = getpass.getpass('Ingrese contraseña para encriptar el archivo ({})'.format(file_path))
        file_encrypted_path = file_path+".aes"
        pyAesCrypt.encryptFile(file_path, file_encrypted_path, password, bufferSize)
        remove(file_path)
        print('Archivo encriptado: --->', file_encrypted_path)
        print('Tamaño del archivo: ', str(stat(file_encrypted_path).st_size) + ' bytes')
    else:
        print('No hay archivo a encriptar: %s' %file_path)


# decrypt
def decrypt():
    file_encrypted_path = file_path + ".aes"
    if path.exists(file_encrypted_path):
        password = getpass.getpass('Ingrese contraseña para desencriptar el archivo ({})'.format(file_encrypted_path))
        pyAesCrypt.decryptFile(file_encrypted_path, file_path, password, bufferSize)
        remove(file_encrypted_path)
        print('Archivo desencriptado: --->', file_path)
        print('Tamaño del archivo: ', str(stat(file_path).st_size) + ' bytes')
    else:
        print('No hay archivo a desencriptar: %s' %file_encrypted_path)

# print(len(sys.argv))
arguments = sys.argv[1:]
# print(sys.argv[1], len(arguments))
if len(arguments) >= 1 and sys.argv[1] == 'decrypt':
    decrypt()
else:
    encrypt()