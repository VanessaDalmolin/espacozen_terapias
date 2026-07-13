import re

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

mapping = {
    'https://www.instagram.com/p/C__iWAuPdav/': 'dancar_vida.png',
    'https://www.instagram.com/p/C8DauDEvGvX/': 'vegnique_yoga.png',
    'https://www.instagram.com/reel/CzD-DEZOgQV/': 'retiro_fogueira.png',
    'https://www.instagram.com/p/CqEHHwiPVip/': 'casal_hero_cropped.jpg',
    'https://www.instagram.com/p/CoNiBs1P27u/': 'evento_prosperidade.png',
    'https://www.instagram.com/p/CviW4KYvaLJ/': 'evento_crianca_interior.png',
    'https://www.instagram.com/p/Cv0XPdHgHpw/': 'constelacao-1.jpg',
    'https://www.instagram.com/p/DKxBFJCv02p/': 'areia_zen_pedra.png'
}

def replace_embed(match):
    original_url = match.group(1)
    matched_image = mapping.get(original_url, 'constelacao-1.jpg')

    return f'''<a href="{original_url}" target="_blank" style="display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.05); text-decoration: none; position: relative;">
              <img src="{{{{ "/assets/images/{matched_image}" | relative_url }}}}" alt="Ver post no Instagram" style="width: 100%; height: 350px; object-fit: cover; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0'">
                 <i class="ph ph-instagram-logo" style="color: white; font-size: 3rem;"></i>
              </div>
            </a>'''

pattern = re.compile(
    r'<div style="text-align: center;">\s*'
    r'<blockquote class="instagram-media" data-instgrm-permalink="(.*?)" .*?</blockquote>\s*'
    r'<script async src="//www\.instagram\.com/embed\.js"></script>\s*'
    r'</div>',
    re.DOTALL
)

new_html, count = pattern.subn(replace_embed, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"Replaced {count} embeds.")
