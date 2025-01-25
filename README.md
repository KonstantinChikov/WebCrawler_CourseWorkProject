# Webcrawler Project

## Preparation
To get started with this project, ensure you have the following:

1. **Docker**: Make sure Docker is installed and running on your system.
2. **Visual Studio Code (VS Code)**: Open the project folder in VS Code for easy navigation and terminal access.

## How to Run
Follow these steps to build and run the project:

1. Open a terminal in VS Code.
2. Navigate to the `nltk-examples` directory using the following command:
   ```bash
   cd nltk-examples
   ```
3. Build the project using Docker Compose:
   ```bash
   docker-compose up --build
   ```
4. Open Docker and locate the running container named `nltk-examples`.
5. In the container's **exec** section, run the following command to execute the script:
   ```bash
   pipenv run python vader-examples.py
   ```

