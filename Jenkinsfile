#!groovy

pipeline {
    agent {
        docker {
            image 'python:3.6'
            args '-u root --name cib-news'
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
            steps {
                echo "-=- Bulding Docker Image -=-"
                // Python dependencies
                script {
                    docker.build("jenkins-build/cib-news")
                }
            }
        }

    }

    post {
        always {
            echo "-=- remove deployment -=-"
            sh "docker commit cib-news builds/cib-news"
        }
    }

}