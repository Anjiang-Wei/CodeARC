def solution():
    def tag(tag_str, content):
        return f"<{tag_str}>{content}</{tag_str}>"

    def a(content):
        return tag("a", content)

    def b(content):
        return tag("b", content)

    def p(content):
        return tag("p", content)

    def body(content):
        return tag("body", content)

    def div(content):
        return tag("div", content)

    def span(content):
        return tag("span", content)

    def title(content):
        return tag("title", content)

    def comment(content):
        return f"<!--{content}-->"

    # Return a dictionary of functions to simulate the class methods
    return {
        'a': a,
        'b': b,
        'p': p,
        'body': body,
        'div': div,
        'span': span,
        'title': title,
        'comment': comment
    }

