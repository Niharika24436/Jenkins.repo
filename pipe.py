pipeline {
    agent any
    stages {
        stage('Run Python') {
            steps {
                echo 'Executing Python Script...'
                sh 'python3 --version'
                sh 'python3 -c "print(\'Hello from Python inside Jenkins!\')"'
            }
        }
    }
}
