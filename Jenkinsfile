#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.6'
        }
    }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "virtualenv .venv"
                sh "source .venv/bin/activate"
                sh "pip install numpy --user"
                sh "python main.py"
            }
        }

        stage('Unit test') {
            steps {
                echo "-=- Running unit test -=-"
                // Python dependencies
                sh "python test.py"
            }
        }

    }

}