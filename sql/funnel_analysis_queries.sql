-- ============================================
-- E-Commerce Revenue Leakage & Funnel Audit - SQL Queries
-- Dataset: Olist Brazilian E-Commerce Dataset
-- ============================================

-- Query 1: Lost order rate (canceled/unavailable orders)
SELECT
    COUNT(*) AS total_orders,
    SUM(CASE WHEN order_status IN ('canceled', 'unavailable') THEN 1 ELSE 0 END) AS lost_orders,
    ROUND(SUM(CASE WHEN order_status IN ('canceled', 'unavailable') THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS lost_order_rate_pct
FROM Orders;

-- Query 2: Total revenue lost from canceled/unavailable orders
SELECT 
    SUM(p.payment_value) AS total_lost_revenue
FROM Orders o
JOIN Payments p ON o.order_id = p.order_id
WHERE o.order_status IN ('canceled', 'unavailable');

-- Query 3: Average order value (all orders) for comparison
SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    SUM(p.payment_value) AS total_revenue,
    ROUND(SUM(p.payment_value) / COUNT(DISTINCT o.order_id), 2) AS avg_order_value
FROM Orders o
JOIN Payments p ON o.order_id = p.order_id;
-- Query 4: Review score comparison - late vs on-time deliveries
-- Business question: Does late delivery correlate with lower customer satisfaction?
SELECT
    CASE WHEN o.delivery_delay_days > 0 THEN 'Late' ELSE 'On-time or Early' END AS delivery_status,
    COUNT(*) AS num_orders,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM OrdersWithDelay o
JOIN Reviews r ON o.order_id = r.order_id
WHERE o.delivery_delay_days IS NOT NULL
GROUP BY delivery_status;