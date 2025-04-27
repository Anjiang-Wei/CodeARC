def solution(label, target):
    import re

    # Check for invalid input: more than one type of separator or mixed case
    if ('_' in label) + ('-' in label) + (label != label.lower()) > 1:
        return None
    
    # Convert to snake_case
    if target == 'snake':
        return re.sub('([A-Z])', r'_\1', label.replace('-', '_')).lower()
    
    # Convert to kebab-case
    if target == 'kebab':
        return re.sub('([A-Z])', r'-\1', label.replace('_', '-')).lower()
    
    # Convert to camelCase
    if target == 'camel':
        return re.sub('([_-])([a-z])', lambda m: m.group(2).upper(), label)
    
    # Return None for invalid target case
    return None

