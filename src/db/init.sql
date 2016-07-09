DROP Table IF EXISTS Users, Friends, Flags, UserFlags;

CREATE TABLE Users (
	uid INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(80) NOT NULL,
	password CHAR(41) NOT NULL, 
	name TEXT,
	location_lat DECIMAL(10, 8) NOT NULL,
	location_log DECIMAL(11, 8) NOT NULL,	
	PRIMARY KEY (uid)
);

CREATE TABLE Friends (
	email VARCHAR(80) NOT NULL,
	friend_email VARCHAR(80) NOT NULL,
	PRIMARY KEY (email, friend_email)
);

CREATE TABLE Flags (
	fid INT NOT NULL AUTO_INCREMENT,
	name TEXT NOT NULL,
	location_lat DECIMAL(10, 8) NOT NULL,
	location_log DECIMAL(11, 8) NOT NULL,	
	rating INT NOT NULL,
	photo_url TEXT,
	PRIMARY KEY (fid)
);

CREATE TABLE UserFlags (
	email VARCHAR(80) NOT NULL,
	fid INT NOT NULL,
	timestamp LONG NOT NULL,
	rating INT,
	review TEXT,
	PRIMARY KEY (email, fid)
);
