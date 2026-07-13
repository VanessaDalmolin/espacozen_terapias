import re
import os

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

pattern = re.compile(
    r'<div style="background: var\(--color-bg-sand\); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba\(0,0,0,0\.05\); margin-top: 3rem;">\s*'
    r'<h3 style="color: var\(--color-secondary\); font-family: var\(--font-heading\); margin-bottom: 1rem; text-align: center;">(.*?)</h3>\s*'
    r'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin-top: 2rem;">\s*'
    r'<!-- Embed .*? -->\s*'
    r'<div style="text-align: center;">\s*'
    r'(<blockquote class="instagram-media".*?</blockquote>)\s*'
    r'<script async src="//www\.instagram\.com/embed\.js"></script>\s*'
    r'</div>\s*'
    r'<!-- Descrição e Links -->\s*'
    r'<div style="display: flex; flex-direction: column; justify-content: center;">\s*'
    r'<p style="text-align: justify; line-height: 1\.6; color: var\(--color-text-dark\); margin-bottom: 2rem; font-size: 1\.1rem;">(.*?)</p>\s*'
    r'<a href="(.*?)" target="_blank" class="btn-outline" style="border-color: var\(--color-primary\); color: var\(--color-primary\); padding: 12px 25px; border-radius: 30px; text-decoration: none; font-weight: bold; display: inline-flex; align-items: center; justify-content: center; gap: 10px;"><i class="ph ph-instagram-logo" style="font-size: 1\.5rem;"></i> (.*?)</a>\s*'
    r'</div>\s*'
    r'</div>\s*'
    r'</div>',
    re.DOTALL
)

def replace_event(match):
    title = match.group(1)
    blockquote = match.group(2)
    description = match.group(3)
    link = match.group(4)
    btn_text = match.group(5)

    return f"""<div style="background: var(--color-white); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-top: 3rem; border-top: 4px solid var(--color-primary-light);">
        <h3 style="color: var(--color-primary); font-family: var(--font-heading); margin-bottom: 1rem; text-align: center;">{title}</h3>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin-top: 2rem;">
          <!-- Embed -->
          <div style="text-align: center;">
            {blockquote}
            <script async src="//www.instagram.com/embed.js"></script>
          </div>
          
          <!-- Descrição -->
          <div style="display: flex; flex-direction: column; justify-content: center;">
            <p style="text-align: justify; line-height: 1.6; color: var(--color-text-dark); margin-bottom: 0; font-size: 1.1rem;">{description}</p>
          </div>
        </div>

        <!-- Botão Menor Abaixo -->
        <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var(--color-bg-sand);">
          <a href="{link}" target="_blank" style="color: var(--color-primary); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem; border: 1px solid var(--color-primary-light); padding: 8px 20px; border-radius: 20px; transition: all 0.3s;"><i class="ph ph-instagram-logo" style="font-size: 1.2rem;"></i> {btn_text}</a>
        </div>
      </div>"""

new_html = pattern.sub(replace_event, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {len(pattern.findall(html))} past events.")
