## 1) Flask CI/CD Pipeline with Jenkins on EC2

This repository demonstrates a complete CI/CD pipeline for a Flask app using Jenkins on an AWS EC2 instance. It auto-triggers deployments using GitHub Webhooks on code push.

---
```
flask-CI-CD-pipeline/
├── app.py
├── test_app.py
├── requirements.txt
└── Jenkinsfile
```
# ✅ Prerequisites

- Jenkins installed on EC2
  - As soon as launch ec2 instance run below commands.
    ```
    sudo apt update
    sudo apt install openjdk-17-jdk -y
    wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt update
    sudo apt install jenkins -y
    sudo systemctl enable jenkins
    sudo systemctl start jenkins
    ```  
- Python 3.12+ installed on EC2
- Flask app in GitHub repo
- Jenkins Git + Pipeline plugins installed
- GitHub Webhook configured to trigger Jenkins
- Required Jenkins credentials (`kanaka-ec2-ssh`)
- Enabled Ports 5000 for testing and 8080 for jenkins opened in EC2 Security Group
---



## 🚀 2) GitHub Actions CI/CD Pipeline

This repo uses GitHub Actions for CI/CD.

### ✅ Trigger Conditions:
- Push to `staging`: triggers staging deployment.
- Push to `main`: triggers test workflow.
- Release tag: triggers production deployment.

### ⚙️ Workflow Jobs:
1. **Install Dependencies**
2. **Run Tests with Pytest**
3. **Deploy to Staging** – only on `staging` branch
4. **Deploy to Production** – only on release tags

### 🔐 Required Secrets:
- `STAGING_API_KEY`
- `PRODUCTION_API_KEY`
