def solution(num):
    try:
        # Convert number to string, add dashes around odd digits, replace double dashes, and strip leading/trailing dashes
        return ''.join(['-' + i + '-' if int(i) % 2 else i for i in str(abs(num))]).replace('--', '-').strip('-')
    except:
        # Return 'None' if an exception occurs
        return 'None'

