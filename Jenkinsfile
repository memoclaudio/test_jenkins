#!groovy

pipeline {

    agent {
        docker {
            image 'python:3.6'
            args '-u root --name cib-news -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    stages {
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                sh "python -m pip install numpy"
                sh "python main.py"
            }
        }

        stage('Unit test') {
            steps {
                echo "-=- Running unit test -=-"
                sh "python test.py"
            }
        }

        stage('Build Docker Image') {
            steps{
                echo "-=- Bulding Docker Image-=-"
                sh "apt-get update"
                sh "apt-get -y install apt-transport-https ca-certificates curl software-properties-common"
                sh "curl -fsSL https://download.docker.com/linux/debian/gpg > /tmp/dkey && apt-key add /tmp/dkey && add-apt-repository \"deb [arch=amd64] https://download.docker.com/linux/debian buster stable\" && apt-get update && apt-get -y install docker-ce"
                sh "docker commit cib-news builds/cib-news"
                sh "docker rmi \$(docker images -f \"dangling=true\" -q)"
            }
        }

    }

}