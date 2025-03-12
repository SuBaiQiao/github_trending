CREATE DATABASE IF NOT EXISTS github_trending;

USE github_trending;

CREATE TABLE IF NOT EXISTS trending_repos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    author VARCHAR(100) NOT NULL,
    language VARCHAR(50),
    stars VARCHAR(20),
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_title (title),
    INDEX idx_author (author),
    INDEX idx_language (language),
    INDEX idx_stars (stars),
    type ENUM('daily', 'weekly', 'monthly') NOT NULL,
);
