-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS Eventify;
CREATE USER IF NOT EXISTS 'root'@'localhost' IDENTIFIED BY 'eventifypass';
GRANT ALL PRIVILEGES ON `Eventify`.* TO 'root'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'root'@'localhost';
FLUSH PRIVILEGES;