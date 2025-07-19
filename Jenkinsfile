pipeline {
    agent any

    environment {
        EC2_IP = "34.220.190.14"  // Update with your EC2 IP
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
                sshagent(['kanaka-ec2-ssh']) {
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_IP} '
                        mkdir -p ~/flaskapp &&
                        cd ~/flaskapp &&
                        if [ ! -d ".git" ]; then git clone https://github.com/kanakagarapati/flask-CI-CD-pipeline.git .; else git pull; fi &&
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
