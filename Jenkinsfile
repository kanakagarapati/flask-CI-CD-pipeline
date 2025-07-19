pipeline {
    agent any

    environment {
        EC2_IP = "34.220.190.14"
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                git 'https://github.com/kanakagarapati/flask-CI-CD-pipeline.git'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
                sh './venv/bin/pytest test_app.py'
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['ec2-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} '
                        cd ~/flaskapp || mkdir ~/flaskapp &&
                        git clone https://github.com/kanakagarapati/flask-CI-CD-pipeline.git ~/flaskapp || cd ~/flaskapp &&
                        git pull &&
                        /usr/bin/python3 -m venv venv &&
                        ./venv/bin/pip install -r requirements.txt &&
                        sudo systemctl restart flaskapp
                    '
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful!'
        }
        failure {
            echo '❌ Deployment Failed.'
        }
    }
}
