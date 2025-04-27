def solution(msg):
    # Replace spaces with dots and pad the message to fit into a 6-column matrix
    msg = msg.replace(' ', '.') + '.' * ((6 - len(msg) % 6) % 6)
    
    # Read the message column by column and join them with spaces
    encrypted_message = ' '.join(msg[n::6] for n in range(6))
    
    return encrypted_message

