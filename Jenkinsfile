
pipeline {

    agent any

    // Environment variables
    environment {
        APP_NAME = 'embedded_c_app'
        VERSION = '1.0'
    }

    // User inputs
    parameters {

        choice(
            name: 'BUILD_TYPE',
            choices: ['Debug', 'Release'],
            description: 'Select build configuration'
        )

        string(
            name: 'BUILD_MESSAGE',
            defaultValue: 'Hello from Jenkins',
            description: 'Enter a build message'
        )
    }

    stages {

        stage('Build Information') {
            steps {
                echo "Application: ${env.APP_NAME}"
                echo "Version: ${env.VERSION}"
                echo "Build Type: ${params.BUILD_TYPE}"
                echo "Message: ${params.BUILD_MESSAGE}"
            }
        }

        stage('Check GCC') {
            steps {
                sh 'gcc --version'
            }
        }

        stage('Compile') {
            steps {
                script {
                    if (params.BUILD_TYPE == 'Debug') {
                        env.CFLAGS = '-g -O0'
                    } else {
                        env.CFLAGS = '-O2'
                    }
                }

                sh 'gcc -Wall -Wextra -Werror $CFLAGS -o c_app main.c'
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
                    echo "$output" | grep -q "Addition: 30"
                    echo "TEST PASSED"
                '''
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'
        }

        failure {
            echo 'Build failed!'
        }
    }
}

