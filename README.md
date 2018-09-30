# py_proxy
Python proxy manager. <br>
Please use diligently and respectfully. <br>
Always respect a website's ROBOTS.txt
This fork automatically validates returned proxies using threading. Easier to use.

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

validproxiees = proxy.validproxy
```

## license
You're free to use this package which is licensed under the [MIT-LICENSE](LICENSE)

## contributing
Contribution is always appreciated. <br>
If you are contributing please remember to update the README. <br>
If your contribution is accepted you will be credited for it.

## Original Author
[Dylan Randall aka HOWZ1T](https://github.com/howz1t)
