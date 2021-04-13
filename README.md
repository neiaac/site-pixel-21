# site-pixel-21
Desenvolvimento do website da edição de 2021 do Pixel D'Ouro.
## Instalação do servidor Django:
Após ter o python3 instalado, seguir os proximos passos.
### Virtual environment (windows): 
Inicializar:
- ~$ cd "C://Users/[...]/RepoFolder/"
- ~$ python3 -m venv [venv-name]

Ativar:
- ~$ cd "C:\Users\[...]\<venv-name>"
- ~$ .\Scripts\activate.bat
### Instalar dependências:
- ~$ pip install -r requirements.txt

### Base de Dados
- Instalar pgAdmin 4
- Criar uma DB no pgAdmin 4
- Abrir o ficheiro settings.py e configurar a secção DATABASES para aceder à nova DB

### Correr servidor Django:
- ~$ cd pixel21
- ~$ python3 manage.py makemigrations
- ~$ python3 manage.py migrate
- ~$ python3 manage.py runserver
