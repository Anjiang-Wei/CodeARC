def solution(text):
    # Replace dashes and underscores with spaces, then split into words
    removed = text.replace('-', ' ').replace('_', ' ').split()
    # If the list is empty, return an empty string
    if len(removed) == 0:
        return ''
    # Join the first word with the capitalized versions of the remaining words
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])

