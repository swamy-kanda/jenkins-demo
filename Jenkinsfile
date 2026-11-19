
pipeline {

    agent any

    environment {
        APP_NAME = 'embedded_c_app'
        VERSION = '1.0'
    }

    parameters {
        choice(
            name: 'BUILD_TYPE',
            choices: ['Debug', 'Release', 'swamy'],
            description: 'Select build configuration'
        )

        string(
            name: 'BUILD_MESSAGE',
            defaultValue: 'Hello from Jenkins',
            description: 'Enter build message'
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

        stage('Compile C') {
            steps {
                script {
                    if (params.BUILD_TYPE == 'Debug') {
                        env.CFLAGS = '-g -O0'
                        env.SWA = ''
                    } else if (params.BUILD_TYPE == 'Release') {
                        env.CFLAGS = '-O2'
                        env.SWA = ''
                    } else {
                        env.CFLAGS = '-O0'
                        env.SWA = '-Wextra'
                    }
                }

                sh 'gcc -Wall $SWA -Werror $CFLAGS -o c_app main.c'
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

        // C Unit Testing

        stage('Run Unit Tests') {
            steps {
                sh './run_tests.sh'
            }
        }

        // Publish JUnit XML Report

        stage('Publish Test Report') {
            steps {
                junit 'test-reports/results.xml'
            }
        }

        // Python Application

        stage('Check Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Run Python Application') {
            steps {
                sh 'python3 avinash.py'
            }
        }
    }

    post {
        success {
            echo 'Build completed successfully!'

            archiveArtifacts(
                artifacts: 'c_app',
                fingerprint: true
            )
        }

        failure {
            echo 'Build failed!'
        }

        always {
            echo 'Jenkins pipeline execution completed.'
        }
    }
}

