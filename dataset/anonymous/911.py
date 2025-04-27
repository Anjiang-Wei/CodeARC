def solution(start, end):
    from ipaddress import ip_address
    
    # Calculate the difference between the two IP addresses
    return int(ip_address(end)) - int(ip_address(start))

