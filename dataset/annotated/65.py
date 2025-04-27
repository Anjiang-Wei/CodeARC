def has_nested_brackets(string: str) -> bool:
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    has_nested_brackets('[[]]') ➞ True
    has_nested_brackets('[]]]]]]][[[[[]') ➞ False
    has_nested_brackets('[][]') ➞ False
    has_nested_brackets('[]') ➞ False
    has_nested_brackets('[[][]]') ➞ True
    has_nested_brackets('[[]][[') ➞ True
    '''

    for i in range(len(string)):
        if string[i] == "]": continue
        cnt, max_nest = 0, 0
        for j in range(i, len(string)):
            if string[j] == "[":
                cnt += 1
            else:
                cnt -= 1
            max_nest = max(max_nest, cnt)
            if cnt == 0:
                if max_nest >= 2:
                    return True
                break
    return False

