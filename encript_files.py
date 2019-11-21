import pyAesCrypt
from os import stat, remove, path

# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024


# file to encrypt
file_path = "C:\\Users\\Marcelo\\Documents\\cuentas.txt"


# encrypt
def encrypt():
    if path.exists(file_path):
        password = input('ingrese contraseña para encriptar el archivo ')
        file_encypted_path = file_path+".aes"
        pyAesCrypt.encryptFile(file_path, file_encypted_path, password, bufferSize)
        remove(file_path)
        print('Archivo encriptado: --->', file_encypted_path)
        print('Tamaño del archivo: ', str(stat(file_encypted_path).st_size) + ' bytes')
    else:
        print('No hay archivo a encriptar: %s' %file_path)


# decrypt
def decrypt():
    file_encypted_path = file_path + ".aes"
    if path.exists(file_encypted_path):
        password = input('ingrese contraseña para desencriptar el archivo ')
        pyAesCrypt.decryptFile(file_encypted_path, file_path, password, bufferSize)
        remove(file_encypted_path)
        print('Archivo desencriptado: --->', file_path)
        print('Tamaño del archivo: ', str(stat(file_path).st_size) + ' bytes')
    else:
        print('No hay archivo a desencriptar: %s' %file_encypted_path)


#encrypt()
decrypt()