from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography import x509
import sys, os

def pubkey_bytes(pubkey: ec.EllipticCurvePublicKey) -> bytes:
	return pubkey.public_bytes(
		encoding=serialization.Encoding.X962,
		format=serialization.PublicFormat.UncompressedPoint
	)

def genkey(p: int) -> bytes:
	curve = ec.SECP384R1()
	privkey = ec.derive_private_key(p, curve)
	pubkey = privkey.public_key()
	return pubkey_bytes(pubkey)

def read_file(filename: str) -> str:
	with open(filename, "r") as file:
		return file.read()


CA_PATH = sys.argv[1] if len(sys.argv) > 1 else "."
cert_files = os.listdir(CA_PATH)
cert_pems = [read_file(f"{CA_PATH}/{filename}") for filename in cert_files if filename.endswith(".pem") or filename.endswith(".crt")]
certs = [cert for chain in cert_pems for cert in x509.load_pem_x509_certificates(chain.encode("utf-8"))]
secp384_certs = [cert for cert in certs if hasattr(cert.public_key(), "curve") and isinstance(cert.public_key().curve, ec.SECP384R1)]
cas = { cert.subject.get_attributes_for_oid(x509.oid.NameOID.COMMON_NAME)[0].value: pubkey_bytes(cert.public_key()) for cert in secp384_certs }

for privkey in range(1, 256):
	pubkey = genkey(privkey)
	for subject, key in cas.items():
		if key == pubkey:
			print(f"{subject}:")
			print(f"	Private:	{privkey}")
			print("	Public:	" + ":".join(f"{b:02x}" for b in pubkey))
