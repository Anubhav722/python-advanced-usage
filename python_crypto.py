# About encrypting data with python.

# It contains symmetric and asymmetric Ciphers, Hashing algorithms, Cryptographic
# Protocols, Public-key encryption and signature algorithms and it's
# own crypto-strong random functions.

# What is cryptography?

# Typically cryptography refers to encryption of plaintext (readable) into
# ciphertext (unreadable) and the reverse, decryption of ciphertext into plaintext.

# A cipher is used with a key which will produce what looks like a random output.
# The strength of an algorithm is measured in how easily an adversary
# is measured in how easily an adversary can break the encryption.

# AES
# We will be using AES
# Advanced Encryption Standard
# Symmetric Cipher (sender and the receiver share the same key)
# 16 byte block size
# The keys can be 128, 192, or 256 bits long.
# Has many block cipher modes.
# http://en.wikipedia.org/wiki/Block_cipher_mode_of_operation

# IV
# Stands for initialization vector.
# Used to randomize and produce distinct ciphertext's for certain
# cipher modes.
# You should not reuse the same IV for two separate encryptions with the same
# key/password
# The IV can be known for most modes.

# Hashing a password.
# Because a cipher requires a key of certain length it's useful
# to hash the users password to produce the same length key every time.

# SHA256 produces a 16 byte output and works great with AES-256.


# We will be encrypting the file here.

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, filename):
	chunk_size = 64 * 1024
	outputFile = "(encrypted)"+ filename
	# filling in 16 bytes
	filesize = str(os.path.getsize(filename)).zfill(16)

	IV = Random.new().read(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, 'rb') as infile:
		with open(outputFile, 'wb') as outfile:
			outfile.write(filesize.encode('utf-8'))
			outfile.write(IV)

			while True:
				chunk = infile.read(chunk_size)

				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += b' ' * (16- (len(chunk) % 16))

				outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
	chunk_size = 64 * 1024
	outputFile = filename[11:]

	with open(filename, 'rb') as infile:
		filesize = int(infile.read(16))

		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outputFile, 'wb') as outfile:

			while True:
				chunk = infile.read(chunk_size)

				if len(chunk) == 0:
					break
				# elif len(chunk) % 16

				outfile.write(decryptor.decrypt(chunk))

			outfile.truncate(filesize)

def getKey(password):
	hasher = SHA256.new(password.encode('utf-8'))
	return hasher.digest()

def Main():
	choice = input("Would you like to (E)ncrypt or (D)ecrypt? :")

	if choice == 'E':
		filename = input("File to encrypt: ")
		password = input("password: ")
		encrypt(getKey(password), filename)
		print("Done.")

	elif choice == 'D':
		filename = input("File to decrypt: ")
		password = input("password: ")
		decrypt(getKey(password), filename)
		print("Done")

	else:
		print("No option selected. Closing ...")


if __name__ == '__main__':
	Main()


# NOTE:
# Not all of ciphers and hashes in pycrpto library are considered safe.
# Make sure you atleast look up the correct algorithm to be using for situation.
# All of the algorithms are open source
Never try to create your own algorithm unless you know what you are doing
and have a team of experts.
