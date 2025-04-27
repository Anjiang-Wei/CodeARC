def solution(start_tag):
    # Extract the tag name by removing the angle brackets and splitting by space
    tag_name = start_tag[1:-1].split(" ")[0]
    # Construct the end tag
    return "</" + tag_name + ">"

