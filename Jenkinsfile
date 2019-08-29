#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.7'
        }
    }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "python example.py"
            }
        }
    }

}