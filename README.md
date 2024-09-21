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
  git clone https://github.com/fatimazahraelaaziz/python_service_pipeline.git
  cd python_service_pipeline

### 2. Local Development 
Develop a Python web service (see [service-count.py](https://github.com/fatimazahraelaaziz/python_service_pipeline/blob/main/service_count.py)) that:
- Increments a counter on POST requests.
- Returns the current count on GET requests.

### 3. Dockerization
- Write a `Dockerfile`(see [Dockerfile](https://github.com/fatimazahraelaaziz/python_service_pipeline/blob/main/Dockerfile)) see  to containerize the application.
- Build and test the Docker image locally:

```bash
docker build -t service-count .
docker run -p 8080:8080 service-count
```

### 4. AWS Setup
- Set up an EC2 instance and install Docker.
- Create an ECR repository to store the Docker image.

### 5. CI/CD Pipeline
Set up GitHub Actions workflows(see [blank.yaml](https://github.com/fatimazahraelaaziz/python_service_pipeline/blob/main/.github/workflows/blank.yml)):
- Build and push the Docker image to ECR on every code commit.
- Pull the image to the EC2 instance and deploy it using Docker Compose.
- Run SonarCloud and Snyk for static analysis and security checks.

## How to Run Locally

To run the **Service Count** project locally, follow these steps:

### Clone the repository:
```bash
git clone https://github.com/fatimazahraelaaziz/python_service_pipeline.git
cd python_service_pipeline
```
### Build the Docker image:
```bash
docker build -t service-count .
```

### Run the Docker container:
```bash
docker run -p 8080:8080 service-count
```

### Interact with the service:
- To retrieve the current count:
  ```bash
  curl http://localhost:8080/
  ```
- To increment the count:
  ```bash
  curl -X POST http://localhost:8080/
  ```

## CI/CD Pipeline

### Continuous Integration (CI)
The CI pipeline runs on every code commit and performs the following actions:
- Builds the Docker image.
- Pushes the Docker image to AWS ECR.
- Runs SonarCloud for static code analysis.
- Runs Snyk for vulnerability scanning.

### Continuous Deployment (CD)
After the CI process is complete, the CD pipeline:
- Pulls the Docker image from AWS ECR to the EC2 instance.
- Restarts the running Docker container using Docker Compose.



