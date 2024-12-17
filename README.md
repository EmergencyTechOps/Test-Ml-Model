# Iris Prediction App

This is a Flask-based application to predict iris species using a trained Random Forest model. It is containerized using Docker.

## Steps to Deploy

1. Clone the repository:
    ```bash
    git clone <repo-url>
    cd project
    ```

2. Train the model:
    ```bash
    python train_model.py
    ```

3. Build the Docker image:
    ```bash
    docker build -t iris-app .
    ```

4. Run the Docker container:
    ```bash
    docker run -d -p 5000:5000 iris-app
    ```

5. Access the app in your browser:
    ```
    http://<EC2-Public-IP>:5000
    ```
