import pyAesCrypt
from os import stat, remove, path
import sys, getpass
import argparse

parser = argparse.ArgumentParser(description='Encrypt Files Program')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--encrypt", type=str, help="Encrypt the desired file")
group.add_argument("--decrypt", type=str, help="Decrypt the desired file")

args = parser.parse_args()

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024

# file to encrypt
# file_path = "C:\\Users\\Marcelo\\Documents\\Vaul\\cuentas.txt"
file_to_encrypt = args.encrypt
file_to_decrypt = args.decrypt
# encrypt
def encrypt(file_to_encrypt):
    file_path = file_to_encrypt
    if path.exists(file_path):
        password = getpass.getpass('Ingrese contraseña para encriptar el archivo ({})'.format(file_path))
        file_encrypted_path = file_path + ".aes"
        pyAesCrypt.encryptFile(file_path, file_encrypted_path, password, bufferSize)
        remove(file_path)
        print('Archivo encriptado: --->', file_encrypted_path)
        print('Tamaño del archivo: ', str(stat(file_encrypted_path).st_size) + ' bytes')
    else:
        print('No hay archivo a encriptar: %s' % file_path)


# decrypt
def decrypt(file_to_decrypt):
    decrypted_file_name = file_to_decrypt.rsplit('.aes')[0]
    if path.exists(file_to_decrypt):
        password = getpass.getpass('Ingrese contraseña para desencriptar el archivo ({})'.format(file_to_decrypt))
        pyAesCrypt.decryptFile(file_to_decrypt, decrypted_file_name, password, bufferSize)
        remove(file_to_decrypt)
        print('Archivo desencriptado: --->', decrypted_file_name)
        print('Tamaño del archivo: ', str(stat(decrypted_file_name).st_size) + ' bytes')
    else:
        print('No hay archivo a desencriptar: %s' % file_to_decrypt)


# print(len(sys.argv))
# arguments = sys.argv[1:]
# print(sys.argv[1], len(arguments))
# if len(arguments) >= 1 and sys.argv[1] == 'decrypt':
#     decrypt()
# else:
#     encrypt()

if args.encrypt:
    print('Encriptando archivo', file_to_encrypt)
    encrypt(file_to_encrypt)
elif args.decrypt:
    print('Desencriptando archivo: ', file_to_decrypt)
    decrypt(file_to_decrypt)
else:
    print('no hay orden')
