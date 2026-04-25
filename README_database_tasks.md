# Database Tasks

A collection of five relational database designs, each containing two linked tables, sample data, and a SELECT query. Created as a course assignment.

---

## Scenarios

### 1. Books and Authors
Stores books and their authors. Each book is linked to one author via a foreign key.

```mermaid
erDiagram
  AUTHORS {
    int author_id PK
    varchar name
    varchar nationality
  }
  BOOKS {
    int book_id PK
    varchar title
    varchar genre
    int published
    int author_id FK
  }
  AUTHORS ||--o{ BOOKS : "writes"
```

---

### 2. Departments and Employees
Stores employees and the department they belong to. Each employee is linked to one department.

```mermaid
erDiagram
  DEPARTMENTS {
    int dept_id PK
    varchar dept_name
    varchar location
  }
  EMPLOYEES {
    int emp_id PK
    varchar first_name
    varchar last_name
    date hire_date
    numeric salary
    int dept_id FK
  }
  DEPARTMENTS ||--o{ EMPLOYEES : "employs"
```

---

### 3. Customers and Orders
Stores customer orders. Each order is linked to one customer.

```mermaid
erDiagram
  CUSTOMERS {
    int customer_id PK
    varchar name
    varchar email
    varchar city
  }
  ORDERS {
    int order_id PK
    date order_date
    numeric total_eur
    varchar status
    int customer_id FK
  }
  CUSTOMERS ||--o{ ORDERS : "places"
```

---

### 4. Consultants and Meetings
Stores consultant meetings with clients. Each meeting is linked to one consultant.

```mermaid
erDiagram
  CONSULTANTS {
    int consultant_id PK
    varchar name
    varchar expertise
    numeric rate_per_hour
  }
  MEETINGS {
    int meeting_id PK
    date meeting_date
    int duration_min
    varchar topic
    varchar client_name
    int consultant_id FK
  }
  CONSULTANTS ||--o{ MEETINGS : "conducts"
```

---

### 5. Directors and Movies
Stores movies and their directors. Each movie is linked to one director.

```mermaid
erDiagram
  DIRECTORS {
    int director_id PK
    varchar name
    int birth_year
    varchar country
  }
  MOVIES {
    int movie_id PK
    varchar title
    int release_year
    varchar genre
    numeric imdb_score
    int director_id FK
  }
  DIRECTORS ||--o{ MOVIES : "directs"
```

---

## Files

| File | Description |
|------|-------------|
| `1_books_and_authors.sql` | Books and Authors — CREATE TABLE, INSERT, SELECT |
| `2_departments_and_employees.sql` | Departments and Employees — CREATE TABLE, INSERT, SELECT |
| `3_customers_and_orders.sql` | Customers and Orders — CREATE TABLE, INSERT, SELECT |
| `4_consultants_and_meetings.sql` | Consultants and Meetings — CREATE TABLE, INSERT, SELECT |
| `5_directors_and_movies.sql` | Directors and Movies — CREATE TABLE, INSERT, SELECT |

---

## How to Run

1. Open your SQL client (e.g. Azure Data Studio, DBeaver, or pgAdmin).
2. Connect to your database.
3. Open and run each file individually in any order — they are fully independent of each other.
