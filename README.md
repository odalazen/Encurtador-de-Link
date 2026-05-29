# Encurtador de Link

Uma simples aplicação web desenvolvida com Flask para encurtar links URL

O sistema permite:

- Criar links encurtados
- Redirecionar automaticamente para a URL original
- Contabilizar quantidade de acessos
- Gerenciar URLs armazenadas
- Interface web simples e funcional

---

# Demonstração

## Exemplo de uso

URL original:

https://google.com

URL encurtada:

http://127.0.0.1:5000/aK91xP

---

# Tecnologias utilizadas

- Python
- Flask
- SQLAlchemy
- SQLite
- HTML5
- CSS3
- Gunicorn

---

# Estrutura do projeto

```
url_shortener/
│
├── app/
│   ├── static/
│   │   └── style.css
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   ├── routes.py
│   ├── services.py
│   └── validators.py
│
├── instance/
│   └── database.db
│
├── venv/
│
├── .gitignore
├── config.py
├── requirements.txt
├── Procfile
└── run.py
```
# Funcionalidades
## Encurtamento de URLs

O usuário envia uma URL e o sistema gera automaticamente um código curto único.

## Redirecionamento automático

Ao acessar:
```
/<short_code>
```
o sistema redireciona para a URL original.

## Contador de cliques

Cada acesso ao link encurtado incrementa automaticamente a quantidade de cliques.

## Validação de URLs

O backend realiza:

normalização de URLs
validação de formato
adição automática de https://

# Como executar localmente
1. Clonar repositório
git clone https://github.com/odalazen/Encurtador-de-Link.git
2. Entrar na pasta
cd Encurtador-de-Link
3. Criar ambiente virtual
Windows
python -m venv venv
Linux/macOS
python3 -m venv venv
4. Ativar ambiente virtual
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
5. Instalar dependências
pip install -r requirements.txt
6. Executar aplicação
python run.py
Acessar no navegador
http://127.0.0.1:5000
Deploy


Lucas Dalazen

GitHub:
https://github.com/odalazen
