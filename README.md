# pipeline-monitoramento-hardware
Pipeline de Engenharia de Dados para monitoramento de preços de hardware (GPUs e CPUs) com Python, AWS S3 e SQL.

# 🚀 Pipeline de Monitoramento de Preços: Hardware Tech

Este projeto demonstra um fluxo de *Engenharia de Dados* para monitorar a variação de preços de componentes de hardware (GPUs e CPUs). O objetivo é extrair dados via Web Scraping, tratá-los com Python e organizá-los em uma estrutura de Data Lake simplificada.

---

## 🛠 Tecnologias Utilizadas
* *Linguagem:* Python (Pandas, BeautifulSoup/Selenium)
* *Armazenamento:* AWS S3 (Camadas Raw e Trusted)
* *Banco de Dados:* MySQL para queries analíticas
* *Documentação:* Markdown e Excalidraw para arquitetura

---

## 📐 Arquitetura do Projeto
> [!TIP]
> *Fluxo de Dados:* Python Scraper ➡️ AWS S3 (Raw) ➡️ Pandas Transformation ➡️ SQL Database (Trusted).

![Arquitetura do Projeto](docs/readme.png)

---

## ⚙️ Destaques Técnicos
* *Data Cleaning:* Tratamento de valores ausentes e normalização de strings (R$ -> Float).
* *Eficiência:* Estrutura de pastas pensada para o crescimento do volume de dados.
* *Escalabilidade:* Pronto para ser migrado para serviços de nuvem (AWS Glue).

---

## 📊 Demonstração (SQL Analytics)
Exemplo de query utilizada para identificar a variação de preços:

```sql
SELECT 
    produto_nome, 
    MIN(preco) AS menor_preco, 
    MAX(preco) AS maior_preco,
    ((MAX(preco) - MIN(preco)) / MAX(preco)) * 100 AS variacao_percentual
FROM hardware_prices
GROUP BY produto_nome
ORDER BY variacao_percentual DESC;

📬 Contato
* LinkedIn: yasmim-loppes
* Email: yasmim_loppes@icloud.com
