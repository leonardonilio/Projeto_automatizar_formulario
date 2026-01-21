Esse projeto é basicamente uma brincadeira séria com Python:
eu criei um formulário em Streamlit e depois fiz um script que preenche esse formulário automaticamente usando Selenium + PyAutoGUI.
Serve tanto para aprender automação quanto para treinar Python na prática.

 O que esse projeto faz?
Tem um site simples com login e uma página para cadastrar produtos.
Dá pra cadastrar código, marca, tipo, categoria, preço, custo e observações.
Mostra uma tabelinha com tudo o que foi cadastrado.

A automação:
abre o navegador,vai até o site,lê um CSV e preenche o formulário sozinho, continua até acabar — ou até você apertar uma tecla para parar.

Estrutura do projeto (resumido)

pages            -> página do formulário

login.py         -> página inicial

automacao.py     -> onde a mágica tenta acontecer (Selenium + PyAutoGUI)

pegar_posicao.py -> script para pegar posição do mouse

produtos.csv     -> uma base de dados para preencher o formulario



Tecnologias usadas
Streamlit (para o site)
Selenium
PyAutoGUI
Pandas
Python 

Use o comando "streamlit run login.py" caso queira ver o site localmente no navegador.

Observações importantes:
Ele podem demorar um pouco pra executar os comandos(vou melhorar futuramente).
O Selenium precisa do ChromeDriver compatível com sua versão do Chrome.
O PyAutoGUI depende da posição dos elementos na tela. Ajuste as coordenadas se necessário.
O CSV de produtos deve estar formatado corretamente.
