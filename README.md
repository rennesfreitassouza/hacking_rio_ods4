# Plataforma educacional - 2022
### Grupo 4Stars / ODS 4 - Educação de qualidade - Desafio SEBRAE

#### Apresentação 

Motivados por um desafio do [SEBRAE RJ](https://www.youtube.com/watch?v=J61fcUDaOpM) o time pensou em uma plataforma educacional integrada com o metaverso
elaborada para conter as melhores ferramentas de aprendizado (aulas online, jogos e desafios, reuniões, arquivos de aprendizado) disponíveis no mercado.

#### O Produto

A plataforma foi pensada para se tornar um hub para outras plataformas de aprendizado. Nela será possível criar um jogo com os 17 ODS (como um Kahoot) e haverá a possibilidade de gravar aulas, de usar uma lousa interativa, assim como a possibilidade de adicionar arquivos de diferentes formatos e facilidade de manipular essa organização de dados. Para integrar a plataforma com o metaverso, imaginou-se que o spatial.io poderia ser utilizado.

#### Informações adicionais 

Para desenvolver um primeiro protótipo do projeto, as ferramentas utilizadas foram: Python, Framework Django, HTML, CSS, Imagens em 3D (Ou imagens que se integrem ao ambiente 3D do metaverso), Metaverso.


#### Como executar este projeto na máquina local

- Instalar o Python 3 na máquina local.<p>
- Criar um virtual environment com o comando:<p>
  `python -m venv hackathon`<p>
- Ativar esse virtual environment com o comando:<p>
  `hackathon\Scripts\activate.bat`<p>
- Clonar este repositório acessando:<p>
  `https://github.com/hackingrio/hackingrio-2022-ods-4-desafio-sebrae-rj-4stars/archive/refs/heads/master.zip`<p>
- Extrair os arquivos do arquivo baixado.<p>
- Acessar o diretório com o mesma ferramenta de linha de comando em que o virtual environment está ativado.<p>
- Instalar os módulos necessários com o comando:<p>
  `pip install -r requirements.txt`<p>
- Executar o comando e aceitar o que for pedido com yes:<p>
  `python manage.py collectstatic`<p>
- Executar o projeto django com o comando:<p>
  `python manage.py runserver`<p>
- Acessar o endereço:<p>
  `http://127.0.0.1:8000/`
