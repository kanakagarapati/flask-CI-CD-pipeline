pipeline {
    agent any

    environment {
        EC2_IP = "34.220.190.14" // 🔁 Replace with your actual EC2 public IP
    }

    stages {
        stage('Clone Repo') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: 'https://github.com/kanakagarapati/flask-CI-CD-pipeline.git']]
                ])
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
                sshagent(credentials: ['kanaka-ec2-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} '
                        if [ ! -d ~/flaskapp ]; then
                            git clone https://github.com/kanakagarapati/flask-CI-CD-pipeline.git ~/flaskapp;
                        else
                            cd ~/flaskapp && git pull;
                        fi &&
                        cd ~/flaskapp &&
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
