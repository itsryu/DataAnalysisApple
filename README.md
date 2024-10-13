<!DOCTYPE html>
<html lang="en">

<body>
    <div id="container">
        <div align="center" style="display: inline_block">
            <h1>Análise de Dados de Inscritos</h1>
            <p>
            Este projeto tem como objetivo realizar uma análise de dados de inscritos para a prova
            da Apple Academy que ocorrera entre os dias 16 a 18 de outubro de 2024, extraindo 
            informações de um arquivo PDF e gerando gráficos para visualização dos dados. Os dados 
            extraídos incluem matrícula, categoria (desenvolvedor ou designer), laboratório, data, 
            dia da semana e horário da prova.
            </p>
        </div>
        <div>
            <h2>Bibliotecas Utilizadas</h2>
            <ul>
                <li>pandas</li>
                <li>matplotlib</li>
                <li>pdfplumber</li>
            </ul>
            <h2>Instalação</h2>
            <p>Para rodar este projeto, você precisa ter Python instalado na sua máquina. Você pode instalar as
                dependências necessárias usando <code>pip</code>. Execute o seguinte comando no terminal:</p>
            <blockquote>
                <strong>⚠ Atenção:</strong> Para executar os próximos comandos (<code>py</code>), é necessário que o
                Python esteja instalado em sua máquina.
                Recomendo a versão <strong>3.11</strong>, que pode ser encontrada no site oficial:
                <a href="https://www.python.org/downloads/" target="_blank">python.org</a>
            </blockquote>
            <br>
            <pre><code>py -m venv .venv</code></pre>
            <pre><code>.\.venv\Scripts\activate</code></pre>
            <pre><code>py -m pip install -r requirements.txt</code></pre>
            <h2>Uso</h2>
            <ol>
                <li>
                    <strong>Extração de Dados:</strong>
                    <ul>
                        <li>Certifique-se de que o arquivo PDF com os dados está no diretório apropriado.</li>
                        <li>O script vai ler o PDF e extrair as informações em um formato estruturado.</li>
                    </ul>
                </li>
                <li>
                    <strong>Análise e Visualização:</strong>
                    <ul>
                        <li>Execute o script Python dentro do venv (virtual enviroment) para gerar um arquivo .csv 
                        com os dados necessários para a análise.</li>
                        <br>
                        <pre><code>.\.venv\Scripts\activate</code></pre>
                        <pre><code>py .\src\main.py</code></pre>
                        <li>Execute os scripts da pasta ./scripts para gerar os outputs (gráficos) na pasta ./outputs</li>
                        <pre><code>py .\src\scripts\histogram.py</code></pre>
                        <pre><code>py .\src\scripts\per_category.py</code></pre>
                        <pre><code>py .\src\scripts\per_laboratory.py</code></pre>
                        <pre><code>py .\src\scripts\per_data.py</code></pre>
                        <pre><code>py .\src\scripts\vacancies_by_category.py</code></pre>
                    </ul>
                </li>
            </ol>
            <h2>Gráficos Gerados</h2>
            <p>Os gráficos abaixo são exemplos de como os dados podem ser visualizados.</p>
            <h3>Inscritos por Categoria</h3>
            <p>Este gráfico mostra a distribuição dos candidatos por categorias e o total de candidatos</p>
             <div align="center" style="display: inline_block">
                <img src="./outputs/candidatos_por_categoria.png" alt="Gráficos" width="600" />
            </div>
            <h3>Vagas por Categoria</h3>
            <p>Este gráfico mostra a relação entre a quantidade de candidatos e as vagas disponíveis para cada categoria, assim
            elucidando a proporcionalidade entre candidatos-vaga para cada categoria</p>
             <div align="center" style="display: inline_block">
                <img src="./outputs/vagas_por_categoria.png" alt="Gráficos" width="600" />
            </div>
        </div>
    </div>
</body>

</html>
