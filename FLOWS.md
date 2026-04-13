# 🌊 Fluxos da ZenIA (Versão ManyChat)

## 1. Saudação Geral e Boas-Vindas
**Gatilhos:** "Oi", "Olá", "Informações", "Menu".

- **Mensagem:** 
  > "Olá! Bem-vindo(a) ao **Espaço Zen Medicina Terapia**. Eu sou a **ZenIA**, sua assistente virtual. ✨"
- **Ação:** Enviar arquivo `Portfolio_Geral.pdf`.
- **Mensagem de Fechamento:** 
  > "Agradecemos muito o seu interesse em nossos serviços. Estou enviando nosso portfólio completo para você conhecer nossa equipe e todas as nossas práticas. Alguma terapia específica chamou sua atenção?"

---

## 2. Interesse em Terapia Específica
**Gatilhos:** "Constelação", "Reiki", "Massagem", "Acupuntura", "Psicoterapia".

- **Mensagem:** 
  > "Que escolha maravilhosa! Essa é uma das especialidades oferecidas por nossa equipe aqui no Espaço Zen."
- **Ação:** Enviar `Imagem_[NOME_DA_TERAPIA].png` (do Drive).
- **Ação Secundária:** Reforçar o link do `Portfolio_Geral.pdf`.
- **Pergunta de Engajamento:** 
  > "Você já conhecia essa técnica ou gostaria de tirar alguma dúvida específica sobre ela?"

---

## 3. Interesse em YOGA (Fluxo de Qualificação)
**Gatilhos:** "Yoga", "Aulas", "Ioga", "Hatha".

- **Mensagem 1:** 
  > "O Yoga é uma das atividades fundamentais aqui no Espaço Zen! 🧘‍♀️"
- **Ação:** Enviar arquivo `Portfolio_Yoga.pdf`.
- **Mensagem 2 (User Input):** 
  > "Para te orientarmos melhor sobre as turmas da nossa equipe: você já pratica Yoga ou seria sua primeira experiência? Além disso, qual seria sua preferência de horário: manhã, tarde ou noite?"

---

## 4. Transbordamento para Atendimento Humano
**Gatilhos:** "Falar com alguém", "Agendar", "Preço", "Valor", "Dúvida técnica".

- **Mensagem:** 
  > "Com certeza! Vou encaminhar sua solicitação para um de nossos especialistas da equipe agora mesmo. Logo mais entraremos em contato."
- **Ação:** Notificar Admin (WhatsApp/Instagram Push).
