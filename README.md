# py_proxy
Python proxy helper. 
Please use deligently and respectfully! 
Always respect a websites ROBOTS.txt!

## compatibility
This library is compatible with python 3

## dependancies
This library is dependant on:
- requests
- beautifulsoup4

## install
```bash
pip install py_proxy
```

## examples
```python
from proxy import Proxy

proxy = Proxy()

# getting the current proxy
cur_proxy = proxy.proxy

# testing the current proxy
res = proxy.test_proxy(cur_proxy)

if res == 1:
	print("success!")
else:
	print("failure!")
	
# cycling the proxy to a new proxy from the pool
proxy.cycle()
```

## license
You're free to use this package which is licensed under the [MIT-LICENSE](LICENSE)

## contributing
Contribution is always appreciated. 
If you are contributing please remember to update the README.
If your contribution is accepted you will be credited for it.

## Author
[Dylan Randall aka HOWZ1T](https://github.com/howz1t)