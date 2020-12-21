
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from getpass import getpass
from cryptography.hazmat.primitives import serialization

from pki_heplers import sign_csr


def main():
    # load csr
    csr_file = open("server-csr.pem", "rb")
    csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())
    print(f"The CSR: {csr}")

    # load public CA key
    ca_public_key_file = open("ca-public-key.pem", "rb")
    ca_public_key = x509.load_pem_x509_certificate(
        ca_public_key_file.read(), default_backend()
    )
    print(f"The CA public key: {ca_public_key}")

    # load private CA key
    ca_private_key_file = open("ca-private-key.pem", "rb")
    ca_private_key = serialization.load_pem_private_key(
        ca_private_key_file.read(),
        getpass().encode("utf-8"),
        default_backend(),
    )
    print(f"The CA private key: {ca_private_key}")

    # sign csr
    sign_csr(
        csr, 
        ca_public_key=ca_public_key, 
        ca_private_key=ca_private_key, 
        new_filename="server-public-key.pem"
    )


if __name__ == "__main__":
    main()
