-- Total transactions
SELECT COUNT(*) AS total_transactions, SUM(amount) AS total_amount
FROM gold_transactions;

-- High-risk transactions
SELECT COUNT(*) AS high_risk_count
FROM gold_transactions
WHERE risk_score > 0.8;

-- Top high-risk users
SELECT user_id, SUM(risk_score) AS total_risk
FROM gold_transactions
GROUP BY user_id
ORDER BY total_risk DESC
LIMIT 10;
