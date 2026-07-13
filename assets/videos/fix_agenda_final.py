import re

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace all Instagram embeds with our images
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

# The regex searches for <div style="text-align: center;">...<blockquote...data-instgrm-permalink="(url)"...</blockquote>...<script...></script>...</div>
pattern_embed = re.compile(
    r'<div style="text-align: center;">\s*<blockquote class="instagram-media" data-instgrm-permalink="(.*?)"[^>]*>.*?</blockquote>\s*<script async src="//www\.instagram\.com/embed\.js"></script>\s*</div>',
    re.DOTALL
)

def replace_embed(match):
    original_url = match.group(1).strip()
    matched_image = mapping.get(original_url, 'constelacao-1.jpg')

    return f'''<a href="{original_url}" target="_blank" style="display: block; border-radius: 12px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.05); text-decoration: none; position: relative;">
              <img src="{{{{ "/assets/images/{matched_image}" | relative_url }}}}" alt="Ver post no Instagram" style="width: 100%; height: 350px; object-fit: cover; display: block; transition: transform 0.3s ease;" onmouseover="this.style.transform='scale(1.05)'" onmouseout="this.style.transform='scale(1)'">
              <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.2); display: flex; align-items: center; justify-content: center; opacity: 0; transition: opacity 0.3s ease;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0'">
                 <i class="ph ph-instagram-logo" style="color: white; font-size: 3rem;"></i>
              </div>
            </a>'''

html, c1 = pattern_embed.subn(replace_embed, html)


# Fix the text of Retiro de Corpo e Alma
# We just find the string starting from "Em nosso <strong>Retiro" to "perfeito para você!</strong>\s*</p>"
# Since it's a huge multiline string, we use re.sub with DOTALL.
pattern_text = re.compile(r'<p style="margin-bottom: 1rem;">\s*Em nosso <strong>Retiro de Corpo e Alma.*?este é o evento\s*perfeito para você!</strong>\s*</p>', re.DOTALL)

new_retiro_text = '''<p style="margin-bottom: 1rem;">
                Em nosso <strong>Retiro de Corpo e Alma</strong>, você terá a oportunidade de:
              </p>
              <ul style="margin-bottom: 1.5rem; padding-left: 0; list-style-type: none;">
                <li style="margin-bottom: 0.5rem;">🧘‍♀️ Explorar o Yoga e a Meditação</li>
                <li style="margin-bottom: 0.5rem;">🌱 Expandir o Autoconhecimento</li>
                <li style="margin-bottom: 0.5rem;">🌌 Descobrir as Constelações Sistêmicas Familiares</li>
                <li style="margin-bottom: 0.5rem;">💆‍♀️ Priorizar o Autocuidado</li>
                <li style="margin-bottom: 0.5rem;">🍏 Explorar a Alimentação Consciente</li>
                <li style="margin-bottom: 0.5rem;">🌅 Conectar-se com a Natureza</li>
              </ul>
              <p style="margin-bottom: 1rem;">
                Este retiro foi cuidadosamente criado pensando em uma agenda holística com atividades para ajudá-la a se reconectar consigo mesma através de técnicas de autoconhecimento como yoga e meditação, com a sua alimentação, com as relações em seu entorno através das constelações familiares e dos exercícios sistêmicos.
              </p>
              <p style="margin-bottom: 0;">
                Se você está buscando um momento de reconexão, de autoconhecimento e plenitude, <strong>este é o evento perfeito para você!</strong>
              </p>'''

html, c2 = pattern_text.subn(new_retiro_text, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Replaced {c1} embeds and {c2} text blocks.")
