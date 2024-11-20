

```sh

# Obtain IP address
ipconfig

# Create port forwarding
netsh interface portproxy add v4tov4 listenport=8080 listenaddress=192.168.1.10 connectport=8080 connectaddress=172.31.167.x

# Verify port forwarding
netsh interface portproxy show all
```
