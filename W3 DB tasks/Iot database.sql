-- ============================================================
-- IoT Equipment Database
-- Task 12.2 — Azure SQL Database
-- ============================================================


-- ============================================================
-- 1. EQUIPMENT AND LOCATION
-- ============================================================

CREATE TABLE location (
    location_id  INT           PRIMARY KEY,
    name         VARCHAR(100)  NOT NULL,
    building     VARCHAR(100),
    room         VARCHAR(50),
    city         VARCHAR(80)
);

CREATE TABLE equipment (
    equipment_id  INT           PRIMARY KEY,
    serial_number VARCHAR(100)  NOT NULL UNIQUE,
    model         VARCHAR(100),
    manufacturer  VARCHAR(100),
    status        VARCHAR(30)   DEFAULT 'active',
    location_id   INT           REFERENCES location(location_id)
);

INSERT INTO location VALUES
    (1, 'Main Lab',       'Building A', 'Room 101', 'Helsinki'),
    (2, 'Server Room',    'Building A', 'Room 005', 'Helsinki'),
    (3, 'Field Station',  'Outdoor',    NULL,        'Espoo');

INSERT INTO equipment VALUES
    (1, 'SN-001-TMP', 'TempSensor X1',  'SensorCorp',  'active',   1),
    (2, 'SN-002-HUM', 'HumidPro 3000',  'IoTech',      'active',   1),
    (3, 'SN-003-CO2', 'CO2 Monitor V2', 'AirSense',    'inactive', 2),
    (4, 'SN-004-GPS', 'GPS Tracker T5', 'TrackIt',     'active',   3);


-- ============================================================
-- 2. USERS AND ROLES
-- ============================================================

CREATE TABLE roles (
    role_id      INT           PRIMARY KEY,
    role_name    VARCHAR(50)   NOT NULL UNIQUE,
    description  VARCHAR(200)
);

CREATE TABLE users (
    user_id      INT           PRIMARY KEY,
    first_name   VARCHAR(50)   NOT NULL,
    last_name    VARCHAR(50)   NOT NULL,
    email        VARCHAR(150)  NOT NULL UNIQUE,
    role_id      INT           REFERENCES roles(role_id)
);

INSERT INTO roles VALUES
    (1, 'admin',      'Full access to all resources'),
    (2, 'technician', 'Can perform maintenance and record measurements'),
    (3, 'viewer',     'Read-only access to data');

INSERT INTO users VALUES
    (1, 'Mikko',  'Virtanen',  'mikko.virtanen@lab.fi',  1),
    (2, 'Aino',   'Mäkinen',   'aino.makinen@lab.fi',    2),
    (3, 'Juhani', 'Korhonen',  'juhani.korhonen@lab.fi', 2),
    (4, 'Liisa',  'Leinonen',  'liisa.leinonen@lab.fi',  3);


-- ============================================================
-- 3. MEASUREMENTS
-- ============================================================

CREATE TABLE measurements (
    measurement_id  INT             PRIMARY KEY,
    measured_at     TIMESTAMP       NOT NULL,
    metric          VARCHAR(50)     NOT NULL,
    value           NUMERIC(10, 4)  NOT NULL,
    unit            VARCHAR(20),
    equipment_id    INT             REFERENCES equipment(equipment_id),
    user_id         INT             REFERENCES users(user_id)
);

INSERT INTO measurements VALUES
    (1, '2025-04-01 08:00:00', 'temperature', 22.50,  'Celsius',  1, 2),
    (2, '2025-04-01 08:05:00', 'humidity',    58.30,  '%',        2, 2),
    (3, '2025-04-01 09:00:00', 'temperature', 23.10,  'Celsius',  1, 2),
    (4, '2025-04-02 10:00:00', 'co2',         412.00, 'ppm',      3, 3),
    (5, '2025-04-03 07:30:00', 'latitude',    60.1699,'deg',      4, 3);

-- Measurements per equipment with the recording user
SELECT
    e.model           AS equipment,
    e.serial_number,
    m.measured_at,
    m.metric,
    m.value,
    m.unit,
    u.first_name || ' ' || u.last_name AS recorded_by
FROM measurements m
JOIN equipment e ON m.equipment_id = e.equipment_id
JOIN users u     ON m.user_id      = u.user_id
ORDER BY m.measured_at;


-- ============================================================
-- 4. MAINTENANCE
-- ============================================================

CREATE TABLE maintenance (
    maintenance_id   INT          PRIMARY KEY,
    scheduled_date   DATE         NOT NULL,
    completed_date   DATE,
    type             VARCHAR(50),
    notes            TEXT,
    equipment_id     INT          REFERENCES equipment(equipment_id),
    user_id          INT          REFERENCES users(user_id)
);

INSERT INTO maintenance VALUES
    (1, '2025-03-15', '2025-03-15', 'calibration', 'Sensor recalibrated to factory specs', 1, 2),
    (2, '2025-03-20', '2025-03-21', 'repair',       'Replaced faulty humidity probe',       2, 2),
    (3, '2025-04-10', NULL,         'inspection',   'Scheduled quarterly inspection',        3, 3),
    (4, '2025-04-15', NULL,         'firmware',     'Firmware update to v3.1.4',             4, 2);

-- Open maintenance tasks with assigned technician and equipment location
SELECT
    e.model              AS equipment,
    l.name               AS location,
    mt.type,
    mt.scheduled_date,
    mt.notes,
    u.first_name || ' ' || u.last_name AS assigned_to
FROM maintenance mt
JOIN equipment e ON mt.equipment_id = e.equipment_id
JOIN location l  ON e.location_id   = l.location_id
JOIN users u     ON mt.user_id      = u.user_id
WHERE mt.completed_date IS NULL
ORDER BY mt.scheduled_date;


-- ============================================================
-- 5. RESERVATIONS
-- ============================================================

CREATE TABLE reservations (
    reservation_id  INT           PRIMARY KEY,
    start_time      TIMESTAMP     NOT NULL,
    end_time        TIMESTAMP     NOT NULL,
    purpose         VARCHAR(200),
    status          VARCHAR(30)   DEFAULT 'confirmed',
    equipment_id    INT           REFERENCES equipment(equipment_id),
    user_id         INT           REFERENCES users(user_id)
);

INSERT INTO reservations VALUES
    (1, '2025-04-20 09:00:00', '2025-04-20 11:00:00', 'Air quality experiment',     'confirmed', 1, 3),
    (2, '2025-04-21 13:00:00', '2025-04-21 15:00:00', 'Humidity calibration test',  'confirmed', 2, 2),
    (3, '2025-04-22 10:00:00', '2025-04-22 12:00:00', 'Field GPS mapping session',  'pending',   4, 3),
    (4, '2025-04-25 08:00:00', '2025-04-25 10:00:00', 'CO2 baseline measurement',   'confirmed', 3, 2);

-- Upcoming reservations with equipment and user details
SELECT
    r.reservation_id,
    e.model               AS equipment,
    l.name                AS location,
    u.first_name || ' ' || u.last_name AS reserved_by,
    r.start_time,
    r.end_time,
    r.purpose,
    r.status
FROM reservations r
JOIN equipment e ON r.equipment_id = e.equipment_id
JOIN location l  ON e.location_id  = l.location_id
JOIN users u     ON r.user_id      = u.user_id
ORDER BY r.start_time;
