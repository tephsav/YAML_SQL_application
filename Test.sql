# Task 1
CREATE TABLE IF NOT EXISTS toys(
    id INT NOT NULL AUTO_INCREMENT,
    toy_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    status ENUM('ok', 'broken', 'repair') NOT NULL,
    status_updated DATE NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(toy_id, name)
);

CREATE TABLE IF NOT EXISTS games(
    id INT NOT NULL AUTO_INCREMENT,
    game_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    date DATE NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(game_id, name)
);

CREATE TABLE IF NOT EXISTS toys_games(
    id INT NOT NULL AUTO_INCREMENT,
    game_id INT NOT NULL,
    toy_id INT NOT NULL,
    note VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (game_id) REFERENCES games(game_id),
    FOREIGN KEY (toy_id) REFERENCES toys(toy_id),
    UNIQUE(game_id, toy_id, note)
);

# Task 2
CREATE TABLE IF NOT EXISTS toys_repair(
    id INT NOT NULL AUTO_INCREMENT,
    toy_id INT NOT NULL,
    issue_description VARCHAR(255) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (toy_id) REFERENCES toys(toy_id),
    UNIQUE(toy_id, issue_description)
);

# Task 4
SELECT toys.toy_id, toys.name AS 'toys.name', toys.status, toys.status_updated,
    games.name AS 'games.name', games.date,
    toys_games.note
    FROM toys_games LEFT JOIN toys ON toys_games.toy_id = toys.toy_id
                    LEFT JOIN games ON toys_games.game_id = games.game_id
    ORDER BY toys.toy_id, games.game_id;

# Task 5
SELECT toys.name
    FROM toys
    WHERE toys.name NOT IN (
        SELECT DISTINCT(toys.name)
            FROM toys RIGHT JOIN toys_repair ON toys.toy_id = toys_repair.toy_id);