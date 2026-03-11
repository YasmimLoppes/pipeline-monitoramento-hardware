-- Criando o esquema para armazenar os dados processados (Camada Silver/Gold)
-- Este script define a estrutura para análise de preços de hardware

CREATE TABLE IF NOT EXISTS tb_monitoramento_precos (
    id_produto INT PRIMARY KEY,
    nome_item VARCHAR(255) NOT NULL,
    categoria VARCHAR(50), -- GPU ou CPU (definido no pipeline Python)
    preco_atual DECIMAL(10, 2),
    loja VARCHAR(100),
    data_extracao DATETIME,
    status_item VARCHAR(20) DEFAULT 'Active'
);

-- Exemplo de query analítica para o recrutador ver que você sabe consultar
-- Busca a média de preço por categoria
SELECT 
    categoria, 
    AVG(preco_atual) as media_preco,
    COUNT(*) as total_itens
FROM tb_monitoramento_precos
GROUP BY categoria;
