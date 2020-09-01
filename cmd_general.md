
### ca-cert 

```bash
# curl default cacert .pem file
/usr/bin/curl-config --ca
/usr/local/bin/curl-config --ca
```

```python
from certifi import where
print(where())
```
