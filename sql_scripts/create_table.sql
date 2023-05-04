use `trip_planner_database`;

CREATE TABLE `User` (
    `Fname`    VARCHAR(30)    NOT NULL,
    `Lname`    VARCHAR(30)    NOT NULL,
    `Email`    VARCHAR(50)    NOT NULL,
    PRIMARY KEY (`Email`)
);

CREATE TABLE `Attraction` (
    `Id`                 VARCHAR(20)     NOT NULL,
    `Name`               VARCHAR(255)    NOT NULL,
    `Description`        TEXT,
    `Zipcode`            VARCHAR(5),
    `Add`                TEXT,
    `Region`             VARCHAR(20),
    `Town`               VARCHAR(20),
    `Tel`                VARCHAR(60),
    `Website`            TEXT,
    `Map`                TEXT,
    `Px`                 FLOAT           NOT NULL,
    `Py`                 FLOAT           NOT NULL,
    `Parkinginfo`        TEXT,
    `Attraction_type`    VARCHAR(11)     NOT NULL,
    PRIMARY KEY (`Id`)
);

CREATE TABLE `Scenic_spot` (
    `Attraction_id`     VARCHAR(20)    NOT NULL,
    `Toldescribe`       TEXT,
    `Travellinginfo`    TEXT,
    `Opentime`          TEXT,
    `Ticketinfo`        TEXT,
    `Remarks`           TEXT,
    `Keyword`           TEXT,
    PRIMARY KEY (`Attraction_id`),
    FOREIGN KEY (`Attraction_id`) REFERENCES `Attraction`(`Id`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);

CREATE TABLE `Restaurant` (
    `Attraction_id`    VARCHAR(20)    NOT NULL,
    `Opentime`         TEXT,
    PRIMARY KEY (`Attraction_id`),
    FOREIGN KEY (`Attraction_id`) REFERENCES `Attraction`(`Id`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);

CREATE TABLE `Hotel` (
    `Attraction_id`          VARCHAR(20)    NOT NULL,
    `Fax`                    VARCHAR(60),
    `Serviceinfo`            TEXT,
    `LowestPrice`            INTEGER,
    `CeilingPrice`           INTEGER,
    `TotalNumberofRooms`     INTEGER,
    `TotalNumberofPeople`    INTEGER,
    PRIMARY KEY (`Attraction_id`),
    FOREIGN KEY (`Attraction_id`) REFERENCES `Attraction`(`Id`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);

CREATE TABLE `Activity` (
    `Attraction_id`     VARCHAR(20)     NOT NULL,
    `Org`               VARCHAR(255)    NOT NULL,
    `Cycle`             TEXT,
    `Travellinginfo`    TEXT,
    `Charge`            INTEGER,
    `Remarks`           TEXT,
    PRIMARY KEY (`Attraction_id`),
    FOREIGN KEY (`Attraction_id`) REFERENCES `Attraction`(`Id`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);

CREATE TABLE `Picture` (
    `Attraction_id`    VARCHAR(20)     NOT NULL,
    `Url`              TEXT            NOT NULL,
    `Description`      TEXT,
    PRIMARY KEY (`Attraction_id`),
    FOREIGN KEY (`Attraction_id`) REFERENCES `Attraction`(`Id`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);

CREATE TABLE `Itinerary` (
    `Id`                  VARCHAR(20)     NOT NULL,
    `User_email`          VARCHAR(50)     NOT NULL,
    `Local_url`           TEXT            NOT NULL,
    PRIMARY KEY (`Id`),
    FOREIGN KEY (`User_email`) REFERENCES `User`(`Email`)
    ON DELETE CASCADE  ON UPDATE CASCADE
);