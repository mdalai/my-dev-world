
## Requirements
```bash
cd security
python3 -m venv .venv
source .venv/bin/activate

pip install flask uwsgi requests


# install wireshark which is used to capture network packet
sudo apt install wireshark


pip install cryptography
```


### symmetric encryption

cipher, plaintext, ciphertext


```bash
# gen random key
key = Fernet.generate_key()

# then use this key to generate cipher
cipher = Fernet(key)

# gen ciphertext
ciphertext = cipher.encrypt(b"plaintext")

# decrypt
plaintext = cipher.decrypt(ciphertext)
```

How do you share your key betweem client and server? It turns out sharing secret is a hard problem.
- Impossible to remember the randomly generated key.
- Sharing initial key is problem.


### asymmetric encryption

Allows for two sides who have never communicated before to share a common secret. 


- Encryption: converts plaintext to ciphertext and back forth.
- Authentication: verfies that a person or thing is who they say they are.


Certificate is like passport. It is issued by CA (Certificate Authority) which is Trusted Third Party (TTP).
"From time A to time B I am X (server) according to Y (CA)"


PKI (Public Key Infrastructure)


Certificate Signing Request (CSR)

- generate your server's private key. output server-private-key.pem
- generate CSR (server-csr.pem) using the private key to sign
- generate your server's public key using csr, CA public key and CA private key.



Now, you can start Python HTTPS application by 
```bash
uwsgi --master --https localhost:5683 server-public-key.pem server-private-key.pem --mount /=server:app
```