#!groovy

pipeline {
    agent {
        docker {
            image 'python3.6'
        }
    }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "pip install numpy"
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