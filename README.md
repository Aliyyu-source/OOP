# IoT Equipment Database

A relational database schema designed for managing IoT equipment, users, measurements, maintenance, and reservations. Built for Azure SQL Database as part of a team project.

---

## Database Structure

The schema consists of 7 linked tables. `equipment` is the central table — measurements, maintenance records, and reservations all connect to it. `location` describes where each device is deployed, and `users` are linked to `roles` for access control.

```mermaid
erDiagram
  LOCATION {
    int location_id PK
    varchar name
    varchar building
    varchar room
    varchar city
  }
  EQUIPMENT {
    int equipment_id PK
    varchar serial_number
    varchar model
    varchar manufacturer
    varchar status
    int location_id FK
  }
  ROLES {
    int role_id PK
    varchar role_name
    varchar description
  }
  USERS {
    int user_id PK
    varchar first_name
    varchar last_name
    varchar email
    int role_id FK
  }
  MEASUREMENTS {
    int measurement_id PK
    timestamp measured_at
    varchar metric
    numeric value
    varchar unit
    int equipment_id FK
    int user_id FK
  }
  MAINTENANCE {
    int maintenance_id PK
    date scheduled_date
    date completed_date
    varchar type
    text notes
    int equipment_id FK
    int user_id FK
  }
  RESERVATIONS {
    int reservation_id PK
    timestamp start_time
    timestamp end_time
    varchar purpose
    varchar status
    int equipment_id FK
    int user_id FK
  }

  LOCATION ||--o{ EQUIPMENT : "located at"
  ROLES ||--o{ USERS : "assigned to"
  EQUIPMENT ||--o{ MEASUREMENTS : "produces"
  USERS ||--o{ MEASUREMENTS : "records"
  EQUIPMENT ||--o{ MAINTENANCE : "requires"
  USERS ||--o{ MAINTENANCE : "performs"
  EQUIPMENT ||--o{ RESERVATIONS : "booked via"
  USERS ||--o{ RESERVATIONS : "makes"
```

---

## Tables

**1. location** — Physical location of each device (building, room, city).

**2. equipment** — Individual IoT devices, each linked to a location.

**3. roles** — User roles defining access levels (admin, technician, viewer).

**4. users** — Team members using the system, each assigned a role.

**5. measurements** — Sensor readings recorded by a user from a specific device.

**6. maintenance** — Scheduled and completed maintenance tasks per device.

**7. reservations** — Equipment booking records made by users.

---

## Files

| File | Description |
|------|-------------|
| `iot_database.sql` | Full schema with CREATE TABLE, INSERT, and SELECT statements |

---

## How to Run

1. Create a new database on Azure SQL.
2. Open a query editor (Azure Portal or Azure Data Studio).
3. Copy and run the contents of `iot_database.sql`.

---

## Team

1. Aliyyu Zen-Abdeen
2. Madhusan Regmi
3. Pratibha Gyawali
4. Md Nihon Mostari Siam
5. Prabhunath Kalwar.
