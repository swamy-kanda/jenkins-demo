
pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code fetched from GitHub'
            }
        }

        stage('Check GCC') {
            steps {
                sh 'gcc --version'
            }
        }

        stage('Compile') {
            steps {
                sh 'gcc -Wall -Wextra -Werror -o c_app main.c'
            }
        }

        stage('Run Application') {
            steps {
                sh './c_app'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    output=$(./c_app)
                    echo "$output"

                    echo "$output" | grep -q "Addition: 40"

                    echo "TEST PASSED"
                '''
            }
        }
    }

    post {
        success {
            echo 'C application CI pipeline completed successfully!'
        }

        failure {
            echo 'C application CI pipeline failed!'
        }
    }
}

