

### Perl
- use `eval` instead of `try catch`. The latter works strangely.
- `untaint`: any data from external source is `taint` in `perl -T` taint mode. The var from command arg and glob is taint. Throws error `Insecure dependency...`.  To untaint, apply regular expression. [How to use taint mode](http://www.perlmeme.org/howtos/secure_code/taint.html)


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

### security
- cksum, md5sum, sha1sum
```bash
cksum testfile1

md5sum file1
# gen checksum for multiple files
md5sum file1 file2 file3 > file_sum.md5
# verify 
md5sum -c file_sum.md5

# gen checksum for all files under a directory
find dir/ -type f -print -exec md5sum {} > file_sum.md5 \;

sha1sum file1 file2 > file.sha1
sha1sum -c file.sha1

```
