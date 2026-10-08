pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Verify Java') {
            steps {
                sh 'java -version'
            }
        }

        stage('Verify Maven') {
            steps {
                sh 'mvn -version'
            }
        }

        stage('Build Maven Project') {
            steps {
                dir('Assignment-Maven-Java/maven-java-project') {
                    sh 'mvn clean test'
                }
            }
        }
    }
}
