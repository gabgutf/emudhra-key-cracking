A trivial script to crack eMudhra's single-byte private keys (which is wild). Read up on the incident [here](https://emudhra.we-have-a-problem.com/).

Install the Python cryptography module (`pip install cryptography`), download the intermediates from [here](https://emudhra.we-have-a-problem.com/chains.zip), extract them into a folder, and run the script:

```shell
# Replace `chains/` with the directory where you extracted the .pem files.
python crack_keys.py chains/
```

And you should get something like:
```
EM OV TLS CA - G3C:
	Private:	4
	Public:	04:13:82:51:cd:52:ac:92:98:c1:c8:aa:d9:77:32:1d:eb:97:e7:09:bd:0b:4c:a0:ac:a5:5d:c8:ad:51:dc:fc:9d:15:89:a1:59:7e:3a:51:20:e1:ef:d6:31:c6:3e:18:35:ca:ca:e2:98:69:a6:2e:16:31:e8:a2:81:81:ab:56:61:6d:c4:5d:91:8a:bc:09:f3:ab:0e:63:cf:79:2a:a4:dc:ed:73:87:be:37:bb:a5:69:54:9f:1c:02:b2:70:ed:67
EM EV TLS CA - G3C:
	Private:	56
	Public:	04:2d:56:e8:29:a6:fb:82:c6:4a:46:97:d9:60:af:95:1e:90:67:ae:91:f9:26:d3:43:06:da:48:a8:aa:eb:78:69:b6:a6:7e:6d:27:42:6e:04:42:aa:03:b3:6e:19:88:df:f6:36:51:4e:e1:cf:07:f5:ba:4b:3f:f2:a0:66:45:ae:7d:31:d5:86:6a:d3:1a:a3:d2:46:eb:0b:31:77:ee:99:cb:75:66:c5:16:ce:74:80:8a:66:8f:91:f0:c4:7f:ca
EM EV TLS CA - G3B:
	Private:	115
	Public:	04:25:db:a8:5a:64:d3:97:da:0b:10:52:e9:ea:54:6e:48:7b:ef:ea:9c:9d:9d:68:a0:c5:ea:dc:fe:ef:75:a6:9b:b5:d6:fc:01:f4:2b:fb:ca:6e:b4:0b:cd:64:c0:76:7e:36:ff:d0:5d:97:a8:13:c5:aa:0c:6c:95:30:e7:9c:f5:f0:86:64:68:f1:38:06:42:0a:a5:c8:51:84:0b:1e:25:25:40:e7:90:e4:b6:54:c3:85:2e:d6:4a:f1:e8:65:7d
EM OV TLS CA - G3B:
	Private:	155
	Public:	04:73:89:7a:a0:eb:3c:fd:ca:8b:12:40:2f:fa:f0:ab:c4:e1:21:2b:af:8d:ee:77:8a:c9:ee:2d:6d:b8:3f:ac:28:0c:5e:05:63:8a:e7:a2:ac:d7:1c:32:2a:8e:36:1c:de:b9:f6:9c:43:02:b9:dd:8d:73:d1:cc:6c:aa:b2:cc:0a:ee:4e:21:6c:e9:79:dd:51:8a:4a:f4:b6:26:e5:68:4c:dd:65:80:37:ed:0c:85:4e:4c:c1:2f:4c:f8:64:6d:0d
EM DV TLS CA - G3B:
	Private:	156
	Public:	04:e7:9e:d9:c0:4a:97:73:c4:73:5e:51:11:1d:a8:5a:c2:bd:5e:64:ab:37:4b:80:e1:2c:bc:20:38:ec:1e:4f:0e:3b:81:2f:c9:85:9e:1e:67:af:b0:4e:2f:8b:c9:7f:74:85:ba:65:aa:91:1e:e8:a4:e4:5b:62:d5:cc:03:d5:6b:e6:78:b3:c3:8c:b4:dc:93:7c:a2:46:0e:23:84:53:c8:92:93:5d:29:d4:4f:91:e1:56:06:b6:3c:ce:da:b4:68
EM DV TLS CA - G3C:
	Private:	230
	Public:	04:3a:7a:78:62:c8:c4:4d:32:4d:dd:69:03:3a:67:82:c0:ef:ee:fe:40:55:e6:8a:12:3f:a0:37:1b:a3:bd:91:94:51:4e:e1:72:a4:33:e3:63:0f:02:bd:18:80:37:d9:e5:14:9f:9b:77:db:94:a2:81:df:98:7b:2f:ea:88:8b:74:bd:fe:8f:da:4c:10:99:ee:6c:a1:95:66:fe:3e:f0:e5:f6:b0:9a:55:6c:cc:8b:a5:05:61:df:1b:2a:44:1d:01
```
