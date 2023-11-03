# Sistema de Monitoramento de Windows com Flask

Este é um projeto de exemplo que demonstra como criar um aplicativo da web usando Flask para coletar informações do sistema Windows, incluindo dados de CPU, memória e disco, e exibir essas informações em uma interface web.

## Pré-requisitos

Antes de executar o aplicativo, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- Flask
- psutil

## Você pode instalar as dependências usando o pip:

pip install Flask psutil


## Como executar o aplicativo
Clone este repositório para o seu computador.

Navegue até o diretório raiz do projeto.

## Execute o aplicativo Flask:

python app.py

O aplicativo estará disponível em http://127.0.0.1:5000/ no seu navegador.

## Rotas
/: Exibe informações gerais do sistema, incluindo uso de CPU, memória e disco.

/usuarios_info: Exibe informações sobre o uso de CPU e memória de cada usuário.

## Arquivo JSON
As informações coletadas do sistema são armazenadas em um arquivo JSON chamado system_info.json. Esse arquivo é atualizado sempre que o aplicativo é executado e contém informações de CPU, memória e disco.

## Contribuindo
Sinta-se à vontade para contribuir com melhorias ou correções para este projeto. Basta fazer um fork do repositório, criar um branch com suas alterações e enviar um pull request.

## Licença
Este projeto está licenciado sob a MIT License - consulte o arquivo LICENSE para obter mais detalhes.

## Créditos
Todos os créditos a Josue Soares Bruno