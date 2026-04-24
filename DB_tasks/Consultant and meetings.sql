-- ============================================================
-- 4. CONSULTANTS AND MEETINGS
-- ============================================================

CREATE TABLE consultants (
    consultant_id INT PRIMARY KEY,
    name          VARCHAR(100) NOT NULL,
    expertise     VARCHAR(100),
    rate_per_hour NUMERIC(8, 2)
);

CREATE TABLE meetings (
    meeting_id    INT PRIMARY KEY,
    meeting_date  DATE NOT NULL,
    duration_min  INT,
    topic         VARCHAR(200),
    client_name   VARCHAR(100),
    consultant_id INT REFERENCES consultants(consultant_id)
);

INSERT INTO consultants VALUES
    (1, 'Sara Hiltunen', 'Data Strategy',      195.00),
    (2, 'Petri Nurmi',   'Cloud Architecture', 220.00),
    (3, 'Anna Repo',     'Change Management',  175.00);

INSERT INTO meetings VALUES
    (1, '2025-04-02',  60, 'Data lake kickoff',      'Elisa Oyj', 1),
    (2, '2025-04-05',  90, 'AWS migration plan',     'F-Secure',  2),
    (3, '2025-04-10',  45, 'Team alignment session', 'Kesko',     3),
    (4, '2025-04-15', 120, 'Dashboard review',       'Elisa Oyj', 1);

-- List all meetings with consultant details and calculated fee, ordered by date
SELECT
    c.name            AS consultant,
    c.expertise,
    m.client_name,
    m.meeting_date,
    m.duration_min,
    ROUND(m.duration_min / 60.0 * c.rate_per_hour, 2) AS fee_eur
FROM meetings m
JOIN consultants c ON m.consultant_id = c.consultant_id
ORDER BY m.meeting_date;
