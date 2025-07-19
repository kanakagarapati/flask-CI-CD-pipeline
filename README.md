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
## Prerequisites

- Jenkins server with Git, Python3, and Email configured.
- Jenkins plugins: Git, Pipeline, Email Extension
- Python app hosted on GitHub.
- SSH access to deployment server (e.g., EC2)

# ✅ Steps by step process

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
      
<img width="2386" height="1284" alt="image" src="https://github.com/user-attachments/assets/af4381b0-2e36-491e-a5bc-261754031d49" />

- opened jenkins with url `http://34.220.190.14:8080/`
- Got below screen to create password.
     
<img width="2378" height="1346" alt="image" src="https://github.com/user-attachments/assets/9cd608e6-33ce-4acc-b02b-596a61726773" />
- Ran this `sudo cat /var/lib/jenkins/secrets/initialAdminPassword` to get password
<img width="1280" height="184" alt="image" src="https://github.com/user-attachments/assets/b1882297-0b40-48be-b9e7-20efbc36dfc3" />

<img width="2900" height="1648" alt="image" src="https://github.com/user-attachments/assets/ef6e6fa5-9d94-4dad-a785-8cde4aefd8b9" />
<img width="2303" height="1618" alt="image" src="https://github.com/user-attachments/assets/6b1bfdfb-8000-45e0-80eb-4b06fc6eec4d" />

 <img width="2403" height="1619" alt="image" src="https://github.com/user-attachments/assets/dded3495-6e70-4c88-9a91-b54421760881" />
 <img width="2414" height="1623" alt="image" src="https://github.com/user-attachments/assets/a0011634-dd36-4c6d-b643-fd027ad9283d" />

 <img width="2455" height="1647" alt="image" src="https://github.com/user-attachments/assets/df58af1a-edd0-4070-804c-f44b23b07ad2" />

 <img width="2810" height="1630" alt="image" src="https://github.com/user-attachments/assets/07d1a5c4-d2b4-45b3-b893-d93a15bb6dfb" />



    

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
