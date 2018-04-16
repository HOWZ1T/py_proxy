# py_proxy
Python proxy manager. <br>
Please use diligently and respectfully. <br>
Always respect a website's ROBOTS.txt

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

## features
- Automatically fetches up to 80 proxies
- Cycle between proxies easily
- Test a proxy and get details about the proxy
- Format proxies for use with requests library

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

# filtering proxies by a country code
proxy = Proxy("US") #gets US only proxies from the pool

#format a proxy for use with requests library
ip = "100.100.100.100" #example ip, not real
port = "1989" #example port, not real
addr = [ip, port]
proxies = proxy.format_proxy(addr) #returns the requests proxies dictionary
```

## license
You're free to use this package which is licensed under the [MIT-LICENSE](LICENSE)

## contributing
Contribution is always appreciated. <br>
If you are contributing please remember to update the README. <br>
If your contribution is accepted you will be credited for it.

## Author
[Dylan Randall aka HOWZ1T](https://github.com/howz1t)