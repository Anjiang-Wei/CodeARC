def solution(subnet):
    import ipaddress as ip
    
    try:
        # Generate a list of all possible IP addresses in the network
        return list(map(str, ip.ip_network(subnet).hosts()))
    except:
        # Return None if the subnet is not a valid IPv4 network
        return None

