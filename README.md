# Service Count: Python Counter Service with CI/CD Pipeline

**Service Count** is a Python-based web service that tracks the number of POST requests it receives and returns the current count on every GET request. This project demonstrates modern DevOps practices by leveraging Docker for containerization, GitHub Actions for CI/CD, and AWS services for hosting and deployment. Additionally, SonarCloud and Snyk are used for static code analysis and security testing.

![image](https://github.com/fatimazahraelaaziz/Python-Service-CI-CD-Pipeline/assets/96253973/0a1f122d-0c4d-4099-b548-2064ed0efca6)

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Project Goals](#project-goals)
- [Tools & Technologies](#tools--technologies)
- [Implementation Steps](#implementation-steps)
- [How to Run Locally](#how-to-run-locally)
- [CI/CD Pipeline](#cicd-pipeline)
- [Deployment](#deployment)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## Project Overview

The **Service Count** project demonstrates a practical approach to building, testing, and deploying a simple Python-based web service using containerization and CI/CD. The service increments a counter on every POST request and returns the current value on each GET request. This project implements industry-standard DevOps practices to automate testing and deployment using GitHub Actions and AWS.

## Features

- **Counter Service**: A web service that:
  - Increments a counter with each POST request.
  - Returns the current count on each GET request.
- **Containerization**: The application is packaged as a Docker image for portability and scalability.
- **Deployment**: Automated deployment to AWS EC2 using Docker and GitHub Actions.
- **Static Code Analysis**: SonarCloud is used for code quality checks.
- **Security Testing**: Snyk is integrated for dependency and image vulnerability scanning.

## Project Goals

1. **Service Development**: Build a Python web service that tracks and serves a request counter.
2. **Containerization**: Package the service as a Docker image and deploy it on an EC2 instance.
3. **CI/CD Pipeline**: Implement automated testing, building, and deployment using GitHub Actions.

## Tools & Technologies

- **GitHub Actions**: Automates the CI/CD pipeline.
- **Docker**: Used for containerizing the Python application.
- **AWS EC2**: Hosts the deployed service in a Docker container.
- **AWS ECR (Elastic Container Registry)**: Stores the Docker image.
- **SonarCloud**: Analyzes the code for quality and maintainability.
- **Snyk**: Scans for security vulnerabilities in the dependencies and Docker image.

## Implementation Steps

### 1. Repository Setup
- Create a GitHub repository for the project and clone it locally:
  ```bash
  git clone https://github.com/your-username/service-count.git
  cd service-count

