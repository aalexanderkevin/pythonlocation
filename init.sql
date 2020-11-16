CREATE TABLE
    location (
        latitude FLOAT NOT NULL,
        longitude FLOAT NOT NULL,
        name VARCHAR(50) NOT NULL,
        colour VARCHAR(10) NOT NULL,
        PRIMARY KEY(latitude, longitude)
    );

INSERT INTO 
	location(latitude, longitude, name, colour)
VALUES
	(-6.175307, 106.82734, 'monas', 'green'),
	(-6.218568, 106.802535, 'ancol', 'green'),
	(-6.902969, 107.619086, 'bandung', 'red')
    ;
