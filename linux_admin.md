
```bash
# create new user
useradd -m -s /bin/bash newuser
passwd newuser
usermod -aG wheel newuser  # sudo group

# create ssh key
ssh-keygen -t rsa
ssh-copy-id -i $HOME/.ssh/id_rsa.pub newuser@server-ip
ssh newuser@server-ip

# disable ssh root login
sudo vim /etc/ssh/sshd_config 
### PermitRootLogin no

# disable ssh password login
sudo vi /etc/ssh/sshd_config
### PasswordAuthentication no
### ChallengeResponseAuthentication no
### UsePAM no

sudo systemctl reload sshd
```
