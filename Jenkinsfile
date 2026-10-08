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
                    sh 'MAVEN_OPTS="-Xms64m -Xmx192m" mvn -B -ntp clean test'
                }
            }
        }
    }

    post {
        success {
            echo 'Build and tests completed successfully!'
        }
        failure {
            echo 'Build failed. Check the console output.'
        }
    }
}

