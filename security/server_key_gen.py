
from pki_heplers import generate_csr, gen_private_key


def main():
    server_private_key = gen_private_key("server-private-key.pem", "serverpass")
    print(server_private_key)
    
    generate_csr(
        server_private_key,
        filename="server-csr.pem",
        country="US",
        state="Maryland",
        locality="Baltmore",
        org="My Company",
        alt_names=["localhost"],
        hostname="my-site.com"
    )

if __name__ == "__main__":
    main()