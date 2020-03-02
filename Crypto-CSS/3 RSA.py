import math

def PublicKeyFind(phin):
	for e in range(phin-3, 1, -1):
		if( math.gcd(e, phin) == 1):
			return e
	return 1
def PrivateKeyFind(e, phin, count):
	for x in range(0, count):
		d = (1 + x * phin) / e
		if d.is_integer():
			return int(d)
	raise Exception("Private Key Not Found in Range")
def RSAKeyFind(p, q):
	n = p * q
	phin = (p-1)*(q-1)
	e = PublicKeyFind(phin)
	d = PrivateKeyFind(e, phin, 900000)
	return ((e,n),(d,n))

def EncryptRSA(m, pub):
	(e,n) = pub
	if (m >= n):
		raise Exception("Unable to Encrypt")
	c = pow(m,e,n)
	return c

def DecryptRSA(c, priv):
	(d,n) = priv
	p = pow(c,d,n)
	return p
	
(pub, priv) = RSAKeyFind(3,11)

message = 31
print(message, "Init")
encrypt = EncryptRSA(message, pub)
print(encrypt, "Encrypted")
decrypt = DecryptRSA(encrypt, priv)
print(decrypt, "Decrypted")
