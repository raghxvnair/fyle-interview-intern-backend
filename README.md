## Prerequisites

Before you begin, ensure you have the following installed on your system:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. *Clone the Repository*: 
    bash
    git clone https://github.com/raghxvnair/fyle-interview-intern-backend.git
   
    cd fyle-interview-intern-backend
    

3. *Build the Docker Image*:
    bash
    docker-compose build
    

4. *Run the Docker Container*:
    bash
    docker-compose up -d
    docker exec -it imageid sh
    

5. *Access the Application*:
    Once the container is up and running, you can access the application at http://localhost:7755.
