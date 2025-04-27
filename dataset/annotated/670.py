def generate_html_tags() -> dict[str, callable]:
    def tag(tag_str: str, content: str) -> str:
        return f"<{tag_str}>{content}</{tag_str}>"

    def a(content: str) -> str:
        return tag("a", content)

    def b(content: str) -> str:
        return tag("b", content)

    def p(content: str) -> str:
        return tag("p", content)

    def body(content: str) -> str:
        return tag("body", content)

    def div(content: str) -> str:
        return tag("div", content)

    def span(content: str) -> str:
        return tag("span", content)

    def title(content: str) -> str:
        return tag("title", content)

    def comment(content: str) -> str:
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

