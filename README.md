# Servidor de Receitas Offline | Projeto Python com SQLite e Flask

Este é um projeto básico em Python que utiliza SQLite como banco de dados e Flask como framework web. Ele é uma variação do projeto original [platform_course](https://github.com/Alessandro-filho/platform_course) do autor [Alessandro Filho](https://github.com/Alessandro-filho). Todos os créditos pelo projeto original vão para o autor.

# Configuração e Execução
## 1. Executando com Docker (recomendado)
Caso você possua Docker instalado em seu sistema, é possível executar o projeto com um único comando. Para instruções sobre como instalar o Docker, visite o [site oficial](https://www.docker.com/products/docker-desktop/).

Com o Docker instalado, basta executar o seguinte comando:

```docker run --name receitas -p 5050:5050 -v "your-recipies:/data" ghcr.io/ryanrpj/backend-plataforma-de-receitas:latest```

Substitua ```your-recipies``` pelo diretório onde os seus cursos estão localizados. **Todos** os seus cursos devem estar dentro deste diretório. **Certifique-se de que este diretório contém _apenas cursos_, portanto, não inclua diretórios abrangentes como o diretório C: do Windows ou /home do Linux.**

Caso seus cursos não estejam todos dentro de um único diretório, crie um diretório e mova-os. Esta é a forma mais simples e recomendada ao executar via Docker.

Se não for viável mover seus arquivos para um único diretório, prossiga com a [execução manual](#2-executando-manualmente). Esta abordagem é mais complexa, porém lhe concede a liberdade de manter seus cursos em diretórios separados em qualquer lugar do seu PC.

## 2. Executando manualmente
### AVISO: Instalação do FFmpeg

Antes de continuar com a instalação e configuração do servidor de cursos offline, é necessário ter o FFmpeg instalado em seu sistema. O FFmpeg é uma ferramenta de linha de comando necessária para processamento de áudio e vídeo. Caso você ainda não tenha o FFmpeg instalado, você pode seguir o seguinte tutorial: [Instalando ffmpeg no windows](https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows).

### AVISO: Instalação do Python

Caso não tenha o Python instalado em seu computador você pode instalá-lo seguindo o seguinte tutorial: [Instalação do Python](https://tutorial.djangogirls.org/pt/python_installation/).

### 1. Clonar o repositório

```bash
git clone https://github.com/dragaoinvisivel/backend-plataforma-de-receitas.git
cd backend-plataforma-de-receitas
```

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

### 3. Instalar as dependências

Instale as dependências do projeto a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar o servidor Flask

```bash
python app.py
```

### 5. Acessar o aplicativo

Uma vez que o servidor Flask estiver em execução, acesse o http://localhost:5050 no seu navegador ou visite o site [Plataforma de Receitas](https://plataforma-de-receitas.vercel.app/) para acessar o aplicativo e consumir a API em seu próprio computador. Caso deseje alterar a URL da API, você pode fazê-lo nas configurações da página.

Caso deseje ter acesso ao código do front-end e modificá-lo acesse: [Front-end Plataforma de Receitas](https://github.com/dragaoinvisivel/frontend-plataforma-de-receitas) 

## Contribuindo

Se desejar contribuir com este projeto, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter detalhes.

## Créditos

Este projeto é uma variação do projeto original [platform_course](https://github.com/Alessandro-filho/platform_course) do autor [Alessandro Filho](https://github.com/Alessandro-filho). Todos os créditos pelo projeto original vão para o autor.
