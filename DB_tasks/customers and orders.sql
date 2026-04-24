-- ============================================================
-- 3. CUSTOMERS AND ORDERS
-- ============================================================

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) UNIQUE,
    city        VARCHAR(80)
);

CREATE TABLE orders (
    order_id    INT PRIMARY KEY,
    order_date  DATE NOT NULL,
    total_eur   NUMERIC(10, 2),
    status      VARCHAR(20),
    customer_id INT REFERENCES customers(customer_id)
);

INSERT INTO customers VALUES
    (1, 'Oy Ranta Ltd',  'ranta@example.fi', 'Helsinki'),
    (2, 'Metsä Corp',    'info@metsa.fi',    'Tampere'),
    (3, 'Aalto Imports', 'aalto@imports.fi', 'Turku');

INSERT INTO orders VALUES
    (1, '2025-01-10', 1250.00, 'delivered', 1),
    (2, '2025-02-14',  340.50, 'shipped',   1),
    (3, '2025-03-01', 4800.00, 'delivered', 2),
    (4, '2025-03-22',  980.75, 'pending',   3);

-- List all completed or shipped orders with customer details, newest first
SELECT
    c.name       AS customer,
    c.city,
    o.order_id,
    o.order_date,
    o.total_eur,
    o.status
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE o.status IN ('delivered', 'shipped')
ORDER BY o.order_date DESC;
