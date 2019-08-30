#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.6'
            args '-u root'
        }
    }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "python -m pip install numpy"
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

        stage('Build Image'){
            sh "docker build -t jenkins-build/cib-news"
        }

    }

}