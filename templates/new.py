from jinja2 import Template

link = """{% raw %}In HTML-dok : <a hresf='#'>ss</a>{% endraw %}"""


msg = Template(link)
print(msg)