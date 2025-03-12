# GitHub Trending Data Scraper

This project aims to develop a system that automatically scrapes daily and weekly trending projects from GitHub Trending pages and stores them in a MySQL database. It provides a FastAPI backend API service for querying and managing the data, and a Vue 3 frontend interface for users to view and filter trending projects.

## Features
- **Data Scraping**: Python script to scrape trending projects from GitHub Trending pages.
- **Backend API**: FastAPI backend to provide RESTful APIs for data query and management.
- **Frontend UI**: Vue 3 and TypeScript frontend with Ant Design for a user-friendly interface.

## Technology Stack
- **Backend**: Python, FastAPI, MySQL
- **Frontend**: Vue 3, TypeScript, Ant Design

## Development Process
1. **Environment Setup**: Install Python, Node.js, MySQL, and create virtual environments.
2. **Data Scraping Module**: Develop Python script to scrape and store data in MySQL.
3. **Backend API**: Build FastAPI backend with SQLAlchemy for database interaction.
4. **Frontend UI**: Create Vue 3 frontend with Ant Design components.
5. **Testing & Deployment**: Perform unit and integration tests, deploy to production.

## Risk Management
- **Data Scraping Failure**: Regularly update scraping script and use proxy IPs.
- **Backend Performance**: Optimize database queries and use caching.
- **Frontend Compatibility**: Test across browsers and devices, use CSS prefixes and Polyfills.