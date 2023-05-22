## This is shell basics project repo on ALX-SE Programme

CHANGE MASTER TO MASTER_HOST='18.209.225.63', MASTER_USER='replica_user', MASTER_PASSWORD='haywon', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=154;
START SLAVE;

CREATE TABLE example1 (
example_column varchar(30)
);
INSERT INTO example1 VALUES
('This is the first row'),
('This is the second row'),
('This is the third row');
