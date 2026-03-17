-- Query para extrair indicadores de qualidade e produtividade
-- Objetivo: Identificar produtos fora do limite de especificação (LSE/LIE)

SELECT 
    CAST(data_producao AS DATE) AS data,
    id_lote,
    valor_medido,
    limite_superior,
    limite_inferior,
    CASE 
        WHEN valor_medido > limite_superior THEN 'Acima do Limite'
        WHEN valor_medido < limite_inferior THEN 'Abaixo do Limite'
        ELSE 'Conforme'
    END AS status_conformidade
FROM tb_producao_qualidade
WHERE data_producao >= '2026-01-01'
ORDER BY data_producao DESC;
