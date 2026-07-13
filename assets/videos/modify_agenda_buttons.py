import re
import os

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Pattern to find the buttons we just inserted
# <a href=".*?" target="_blank" style="color: var\(--color-primary\); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0\.95rem; border: 1px solid var\(--color-primary-light\); padding: 8px 20px; border-radius: 20px; transition: all 0\.3s;"><i class="ph ph-instagram-logo" style="font-size: 1\.2rem;"></i> .*?</a>

pattern = re.compile(
    r'<a href=".*?" target="_blank" style="color: var\(--color-primary\); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0\.95rem; border: 1px solid var\(--color-primary-light\); padding: 8px 20px; border-radius: 20px; transition: all 0\.3s;"><i class="ph ph-instagram-logo" style="font-size: 1\.2rem;"></i> .*?</a>'
)

new_button = r'<a href="https://wa.me/{{ site.phone }}?text=Olá,%20gostaria%20de%20saber%20sobre%20as%20próximas%20datas%20deste%20evento." target="_blank" style="color: var(--color-primary); background: var(--color-bg-sand); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem; border: 1px solid var(--color-primary-light); padding: 10px 25px; border-radius: 20px; transition: all 0.3s;"><i class="ph ph-calendar" style="font-size: 1.2rem;"></i> Consultar agenda para datas deste evento</a>'

new_html, count = pattern.subn(new_button, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {count} buttons.")
