pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/kanakagarapati/flask-CI-CD-pipeline.git'
        EC2_USER = 'ubuntu'
        EC2_IP = '34.220.190.14'
        PROJECT_DIR = 'flaskapp'
    }

    stages {

        stage('Clone Repo') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[url: "${REPO_URL}"]]
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
                    ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_IP} '
                        cd ~ &&
                        if [ -d "${PROJECT_DIR}/.git" ]; then
                            echo "[INFO] Git repo exists. Pulling latest changes..." &&
                            cd ${PROJECT_DIR} && git pull
                        else
                            echo "[INFO] Git repo not found. Cloning fresh..." &&
                            rm -rf ${PROJECT_DIR} &&
                            git clone ${REPO_URL} ${PROJECT_DIR} &&
                            cd ${PROJECT_DIR}
                        fi &&
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
        failure {
            echo "❌ Deployment Failed."
        }
        success {
            echo "✅ Deployment Successful."
        }
    }
}
