

### Perl
- use `eval` instead of `try catch`. The latter works strangely.
- `untaint`: any data from external source is `taint` in `perl -T` taint mode. The var from command arg and glob is taint.  To untaint, apply regular expression. [How to use taint mode](http://www.perlmeme.org/howtos/secure_code/taint.html)


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
