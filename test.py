if __name__ == "__main__":
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
    proxy = Proxy("US")  # gets US only proxies from the pool

    # format a proxy for use with requests library
    ip = "100.100.100.100"  # example ip, not real
    port = "1989"  # example port, not real
    addr = [ip, port]
    proxies = proxy.format_proxy(addr)  # returns the requests proxies dictionary

    # validating all proxies concurrently
    proxy.validate_proxies()

    # cycling through valid only proxies
    proxy.cycle(valid_only=True)
