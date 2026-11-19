
pipeline {

    agent any

    // Environment Variables
    environment {
        APP_NAME = 'embedded_c_app'
        VERSION = '1.0'
    }

    // Build Parameters
    parameters {

        choice(
            name: 'BUILD_TYPE',
            choices: ['Debug', 'Release','swamy'],
            description: 'Select build configuration'
        )

        string(
            name: 'BUILD_MESSAGE',
            defaultValue: 'Hello from Jenkins',
            description: 'Enter build message'
        )
    }

    stages {

        // Display Build Information
        stage('Build Information') {
            steps {
                echo "Application: ${env.APP_NAME}"
                echo "Version: ${env.VERSION}"
                echo "Build Type: ${params.BUILD_TYPE}"
                echo "Message: ${params.BUILD_MESSAGE}"
            }
        }

        // C Application Pipeline

        stage('Check GCC') {
            steps {
                sh 'gcc --version'
            }
        }

        stage('Compile C') {
            steps {
                script {
                    if (params.BUILD_TYPE == 'Debug') {
                        env.CFLAGS = '-g -O0'
                    } else if(params.BUILD_TYPE == 'Release') {
                        env.CFLAGS = '-O2'
                    }
                    else{
                        env.CFLAGS = '-OO'
                    }
                }

                sh 'gcc -Wall -Wextra -Werror $CFLAGS -o c_app main.c'
            }
        }

        stage('Run C Application') {
            steps {
                sh './c_app'
            }
        }

        stage('Test C Application') {
            steps {
                sh '''
                    output=$(./c_app)
                    echo "$output"

                    echo "$output" | grep -q "Addition: 30"

                    echo "C TEST PASSED"
                '''
            }
        }

        // Python Application Pipeline

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Python Application') {
            steps {
                sh '''
                    echo "$BUILD_MESSAGE"
                    python3 avinash.py
                '''
            }
        }
    }

    // Post Build Actions

    post {

        success {
            echo 'C and Python applications completed successfully!'
        }

        failure {
            echo 'C or Python application pipeline failed!'
        }

        always {
            echo 'Jenkins pipeline execution completed.'
        }
    }
}

