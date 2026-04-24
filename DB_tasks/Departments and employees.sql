-- ============================================================
-- 2. DEPARTMENTS AND EMPLOYEES
-- ============================================================

CREATE TABLE departments (
    dept_id   INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location  VARCHAR(100)
);

CREATE TABLE employees (
    emp_id     INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50) NOT NULL,
    hire_date  DATE,
    salary     NUMERIC(10, 2),
    dept_id    INT REFERENCES departments(dept_id)
);

INSERT INTO departments VALUES
    (1, 'Engineering', 'Helsinki'),
    (2, 'Marketing',   'Espoo'),
    (3, 'Finance',     'Tampere');

INSERT INTO employees VALUES
    (1, 'Mikko',  'Virtanen', '2020-03-15', 62000.00, 1),
    (2, 'Aino',   'Mäkinen',  '2019-07-01', 58000.00, 1),
    (3, 'Juhani', 'Korhonen', '2021-11-20', 54000.00, 2),
    (4, 'Liisa',  'Leinonen', '2018-01-08', 67000.00, 3);

-- List all employees with their department and location, ordered alphabetically
SELECT
    d.dept_name,
    d.location,
    e.first_name || ' ' || e.last_name AS employee,
    e.hire_date,
    e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.last_name;
