def removezero_ip(ip):
    ip_split = ip.split('.')
    new_ip = []
    for i in ip_split:
        new_ip.append(str(int(i)))
    return '.'.join(new_ip)
