CREATE DATABASE stage_events;
USE stage_events;

CREATE TABLE stage_event (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    detail VARCHAR(255),
    organizer VARCHAR(100)
);

CREATE TABLE stage_event_show (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    stage_event_id BIGINT,
    FOREIGN KEY (stage_event_id) REFERENCES stage_event(id) ON DELETE CASCADE
);

CREATE TABLE ticket_booking (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    price DOUBLE NOT NULL,
    customer VARCHAR(100) NOT NULL,
    no_of_seats INT NOT NULL,
    stage_event_show_id BIGINT,
    FOREIGN KEY (stage_event_show_id) REFERENCES stage_event_show(id) ON DELETE CASCADE
);

INSERT INTO stage_event (name, detail, organizer) VALUES
('Jazz Night', 'A night of soulful jazz performances', 'Jazz Collective'),
('Comedy Evening', 'A fun-filled evening of stand-up comedy', 'Laughs Unlimited');

INSERT INTO stage_event_show (start_time, end_time, stage_event_id) VALUES
('2024-06-15 19:00:00', '2024-06-15 22:00:00', 1),
('2024-06-16 20:00:00', '2024-06-16 23:00:00', 2);

INSERT INTO ticket_booking (price, customer, no_of_seats, stage_event_show_id) VALUES
(45.0, 'Michael Brown', 3, 1),
(70.0, 'Emily White', 2, 1),
(55.0, 'James Green', 4, 2);
