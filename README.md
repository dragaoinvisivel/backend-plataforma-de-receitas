# Back-end | Plataforma de Receitas
> [!NOTE]
> Este repositório é para desenvolvedores que desejam inspecionar e/ou contribuir para o back-end da [Plataforma de Receitas](https://github.com/dragaoinvisivel/frontend-plataforma-de-receitas).
>
> Caso você seja apenas um usuário que deseja executar o projeto em seu computador, visite o [repositório correto](https://github.com/dragaoinvisivel/frontend-plataforma-de-receitas).

# Configuração e Execução
> [!NOTE]
> Ressaltamos novamente que este tutorial de execução é para **desenvolvedores**. Você não irá conseguir utilizar o projeto seguindo os tutoriais abaixo.

Comece clonando o repositório:
```bash
git clone https://github.com/dragaoinvisivel/backend-plataforma-de-receitas.git
cd backend-plataforma-de-receitas
```

Com o repositório clonado, você possui duas opções para executar o servidor:
- [Executar de forma segura com Docker - Recomendado](#1-executando-com-docker-recomendado)
- [Executar manualmente - somente para usuários avançados](#2-executando-manualmente)

## 1. Executando com Docker (recomendado)
Caso você possua Docker instalado em seu sistema, é possível executar o back-end com pouquíssimos comandos. Para instruções sobre como instalar o Docker, visite o [site oficial](https://www.docker.com/products/docker-desktop/).

Com o Docker instalado, basta executar o seguinte comando:

```docker run -it --name receitas-dev -p 9823:9823 -v "./src:/app" python:latest /bin/bash```

Feito isso, você já estará dentro do container com o ambiente de desenvolvimento configurado e pronto para uso. O próximo passo é navegar para o diretório onde se encontra o código fonte, e instalar as dependências do projeto:

```cd /app && pip install -r requirements.txt```

Com as dependências instaladas, basta executar o servidor:

```python app.py```

## 2. Executando manualmente
> [!CAUTION]
> Executar o projeto manualmente envolve o gerenciamento manual das tecnologias e dependências necessárias. Isso pode gerar conflitos, caso você já possua algum dos itens aqui listados, porém em versões diferentes.
>
> Somente prossiga com a execução manual caso saiba o que está fazendo.
### 1. Ferramentas necessárias

Antes de continuar com a instalação e configuração do projeto, é necessário ter algumas ferramentas instaladas no seu computador. Sem elas, não será possível executar o projeto.

##### FFmpeg
Ferramenta de linha de comando necessária para processamento de áudio e vídeo. Caso você ainda não tenha o FFmpeg instalado, você pode seguir o seguinte tutorial: [Instalando ffmpeg no Windows](https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows).

##### Python

Caso não tenha o Python instalado em seu computador, você pode instalá-lo seguindo o seguinte tutorial: [Instalação do Python](https://tutorial.djangogirls.org/pt/python_installation/).

### 2. Configurar o ambiente virtual (venv)

Crie um ambiente virtual usando `venv`:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- No Windows:

```bash
venv\Scripts\activate
```

- No Linux/Mac:

```bash
source venv/bin/activate
```

### 3. Instalar as dependências Python

Instale as dependências do projeto a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar o servidor Flask

```bash
python app.py
```

## Contribuindo

Se desejar contribuir com este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Créditos

Este projeto é uma variação do projeto original [platform_course](https://github.com/Alessandro-filho/platform_course) do autor [Alessandro Filho](https://github.com/Alessandro-filho). Todos os créditos pelo projeto original vão para o autor.
