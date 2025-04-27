def solution(ip, subnet):
    # Convert IP and subnet to integer lists
    ip_parts = [int(part) for part in ip.split('.')]
    subnet_parts = [int(part) for part in subnet.split('.')]
    
    # Calculate network and host parts
    network = [ip_part & subnet_part for ip_part, subnet_part in zip(ip_parts, subnet_parts)]
    host = [ip_part & ~subnet_part for ip_part, subnet_part in zip(ip_parts, subnet_parts)]
    
    # Convert back to string format
    network_str = '.'.join(map(str, network))
    host_str = '.'.join(map(str, host))
    
    return network_str, host_str

