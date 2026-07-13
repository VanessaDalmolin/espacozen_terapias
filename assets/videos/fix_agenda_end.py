import re

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start of the trailing garbage
# The last valid thing is the button for Retorno às Origens
# "Consultar agenda para datas deste evento</a>"
# Then it closes the button div, the grid div, the Retorno div, the flex div, the margin div, the wrapper, the page-content.
# Wait, let's just find the last "Consultar agenda para datas deste evento</a>\n        </div>\n      </div>"

pattern = re.compile(r'(Consultar agenda para datas deste evento</a>\s*</div>\s*</div>)(.*?)$', re.DOTALL)

def replace_end(match):
    # We keep the last event closing tags, and then append the 4 closing tags for the page
    return match.group(1) + "\n    </div>\n  </div>\n</div>\n</div>\n"

new_html, count = pattern.subn(replace_end, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {count} instances.")
