import re

filepath = '../../agenda.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Dançar a Vida
pattern_dancar = re.compile(r'<div style="background: var\(--color-bg-sand\); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba\(0,0,0,0\.05\);">(.*?)<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin-top: 2rem;">(.*?)<div style="display: flex; flex-direction: column; justify-content: center;">\s*<p style="text-align: justify; line-height: 1\.6; color: var\(--color-text-dark\); margin-bottom: 2rem; font-size: 1\.1rem;">(.*?)</p>.*?</div>\s*</div>\s*</div>', re.DOTALL)

def replace_dancar(m):
    return f"""<div style="background: var(--color-white); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border-top: 4px solid var(--color-primary-light);">
        <h3 style="color: var(--color-primary); font-family: var(--font-heading); margin-bottom: 1rem; text-align: center;">Vivência: Dançar a Vida</h3>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin-top: 2rem;">{m.group(2)}<div style="display: flex; flex-direction: column; justify-content: center;">
            <p style="text-align: justify; line-height: 1.6; color: var(--color-text-dark); margin-bottom: 0; font-size: 1.1rem;">{m.group(3).strip()}</p>
          </div>
        </div>

        <div style="text-align: center; margin-top: 2rem; padding-top: 2rem; border-top: 1px solid var(--color-bg-sand);">
          <a href="https://wa.me/{{{{ site.phone }}}}?text=Olá,%20gostaria%20de%20saber%20sobre%20as%20próximas%20datas%20deste%20evento." target="_blank" style="color: var(--color-primary); background: var(--color-bg-sand); text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; justify-content: center; gap: 8px; font-size: 0.95rem; border: 1px solid var(--color-primary-light); padding: 10px 25px; border-radius: 20px; transition: all 0.3s;"><i class="ph ph-calendar" style="font-size: 1.2rem;"></i> Consultar agenda para datas deste evento</a>
        </div>
      </div>"""

html = pattern_dancar.sub(replace_dancar, html)


# Fix Retiro
pattern_retiro = re.compile(r'<!-- Retiro de Corpo e Alma -->\s*<div style="background: var\(--color-white\); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba\(0,0,0,0\.05\); margin-top: 3rem; border-top: 4px solid var\(--color-primary-light\);">\s*<h3 style="color: var\(--color-primary\); font-family: var\(--font-heading\); margin-bottom: 1rem; text-align: center;">Vivência: Retiro de Corpo e Alma</h3>\s*<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; margin-top: 2rem;">(.*?)<!-- Descrição -->\s*<div style="display: flex; flex-direction: column; justify-content: center;">\s*<div style="font-size: 1\.05rem; line-height: 1\.7; text-align: justify; color: var\(--color-text-dark\);">(.*?)</div>\s*</div>\s*</div>\s*<!-- Botão Menor Abaixo -->', re.DOTALL)

def replace_retiro(m):
    return f"""<!-- Retiro de Corpo e Alma -->
      <div style="background: var(--color-white); border-radius: 20px; padding: 3rem; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin-top: 3rem; border-top: 4px solid var(--color-primary-light);">
        <h3 style="color: var(--color-primary); font-family: var(--font-heading); margin-bottom: 1rem; text-align: center;">Vivência: Retiro de Corpo e Alma</h3>
        
        <div style="display: flex; flex-direction: column; align-items: center; margin-top: 2rem;">{m.group(1)}<!-- Descrição -->
          <div style="width: 100%; max-width: 800px; margin: 0 auto; text-align: center;">
            <div style="font-size: 1.05rem; line-height: 1.7; text-align: justify; color: var(--color-text-dark);">{m.group(2)}</div>
          </div>
        </div>

        <!-- Botão Menor Abaixo -->"""

html = pattern_retiro.sub(replace_retiro, html)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
