CREATE DATABASE ai_interview_system;

USE ai_interview_system;

CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE Questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(50),
    question TEXT,
    difficulty VARCHAR(20)
);

CREATE TABLE Results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    question_id INT,
    answer TEXT,
    score INT,
    feedback TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (question_id) REFERENCES Questions(id)
);

alter table Users
rename column name to username;

describe Users;

