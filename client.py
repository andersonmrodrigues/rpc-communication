import xmlrpc.client

with xmlrpc.client.ServerProxy("http://YOURSERVERIP:8000/") as proxy:
    with open('data.txt') as f:
        lines = f.readlines()
    result = proxy.scaler(lines)
    with open('output.txt', 'w') as f:
        for line in result:
            f.write(str(line) + '\n')
