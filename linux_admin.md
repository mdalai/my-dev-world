
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

## Linux utils

- `renice`: alter a process priority. Great tool to use if you want to your process has no impact on critical operations. 


## systemd
### systemd-analyze
- `systemd-analyze -h`
- `systemd-analyze critical-chain`: gives the time when unit became active or started. Also provide the time the unit took to start.
- `systemd-analyze blame`: Print list of running units ordered by time to init
- `systemd-analyze plot > os_start_order`: Output SVG graphic of service initialization order

### mount unit
- To auto mount filesystem, the systemd mount unit is an alternative other than /etc/fstab. 
- Create a file /etc/systemd/system/<path-to-mount-point>.mount with `what=` FileSystem, `where=` mountpoint.
  
  

  ## FAQ
  
  1. Why use bind mount? Not a fan of bind mount, symbolic link. Always find it so confusing when debug problem.
  
