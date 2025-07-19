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

<img width="2477" height="1503" alt="image" src="https://github.com/user-attachments/assets/04926a2e-fea3-48f3-adc9-172b24f38218" />

<img width="2471" height="453" alt="image" src="https://github.com/user-attachments/assets/2a665652-2c69-43fb-8712-605dd6495878" />

<img width="2636" height="1643" alt="image" src="https://github.com/user-attachments/assets/e08eabab-aefc-4ca3-963e-6054a077aec4" />

<img width="2708" height="1629" alt="image" src="https://github.com/user-attachments/assets/e725545e-d68f-4b7c-9d6b-8f949741e028" />

<img width="2618" height="1642" alt="image" src="https://github.com/user-attachments/assets/d39c084c-529c-44b5-a0e5-640cfd6f8951" />
    
<img width="2863" height="1650" alt="image" src="https://github.com/user-attachments/assets/0bf2dbbc-229f-4247-b690-fd4b5c2a2c6e" />
<img width="2765" height="1566" alt="image" src="https://github.com/user-attachments/assets/f55cd01c-3bc5-4f41-a5e9-8c321424efa7" />

<img width="2869" height="1386" alt="image" src="https://github.com/user-attachments/assets/b11370d1-0b45-44ab-ace0-f27591b81bce" />
<img width="2871" height="672" alt="image" src="https://github.com/user-attachments/assets/b179a009-abbd-4e40-a8f5-8a46629825c1" />
<img width="2895" height="1613" alt="image" src="https://github.com/user-attachments/assets/ee8fc3da-706a-4208-a13a-ab59e85a795d" />
<img width="2839" height="1636" alt="image" src="https://github.com/user-attachments/assets/17c54892-d3af-4d82-98b6-237c25a5c771" />

<img width="2874" height="1642" alt="image" src="https://github.com/user-attachments/assets/1a1161a3-3bab-44e4-ab71-db53019e0b5f" />

### 🔐 Required Open Ports in EC2 Security Group

To ensure your Jenkins pipeline and Flask app run properly, the following inbound ports must be open in your EC2 security group:

| Type            | Protocol | Port Range | Source     | Purpose                                  |
|-----------------|----------|------------|------------|------------------------------------------|
| SSH             | TCP      | 22         | 0.0.0.0/0  | For SSH access to the EC2 instance       |
| HTTP            | TCP      | 80         | 0.0.0.0/0  | Optional: For serving HTTP content       |
| Custom TCP Rule | TCP      | 8080       | 0.0.0.0/0  | For GitHub webhook communication to Jenkins |
| Custom TCP Rule | TCP      | 5000       | 0.0.0.0/0  | For accessing the Flask application      |



----------------------


## 🚀 2) GitHub Actions CI/CD Pipeline

This repo uses GitHub Actions for CI/CD.

### ✅ Trigger Conditions:
- Push to `staging`: triggers staging deployment.
- <img width="2284" height="960" alt="image" src="https://github.com/user-attachments/assets/99a9f67b-5aa0-4e93-8cbc-ae38af0f295e" />
<img width="2782" height="1739" alt="image" src="https://github.com/user-attachments/assets/65a388c0-8e0c-4c7c-ac69-09db7fab1d2d" />
<img width="1804" height="1246" alt="image" src="https://github.com/user-attachments/assets/7e45695b-3085-4718-950c-373cf86853fb" />
<img width="2876" height="1051" alt="image" src="https://github.com/user-attachments/assets/452f3ad8-45fa-431b-a498-db86ddeac12b" />
<img width="2854" height="1335" alt="image" src="https://github.com/user-attachments/assets/2d39613a-97fd-49ca-9394-d3e6aa0eada6" />

- Push to `main`: triggers test workflow.
- <img width="2787" height="1546" alt="image" src="https://github.com/user-attachments/assets/867d9fbb-4f7a-48da-a161-4b5323df9e6c" />

- Release tag: triggers production deployment.
<img width="2805" height="1611" alt="image" src="https://github.com/user-attachments/assets/53c3f7e3-1112-4a16-afb5-cf8f88dad85f" />
<img width="2740" height="1596" alt="image" src="https://github.com/user-attachments/assets/e35c0fb0-e5a0-4359-b0e5-6fd870e6696a" />
<img width="2710" height="1621" alt="image" src="https://github.com/user-attachments/assets/148ab06e-29df-4a06-82fc-e9c273d93587" />
<img width="2879" height="875" alt="image" src="https://github.com/user-attachments/assets/9e120a90-3ab0-40c5-82aa-444939070f76" />
<img width="2888" height="1306" alt="image" src="https://github.com/user-attachments/assets/400c3613-e48b-43a0-9c5d-9f5104e4198d" />

### ⚙️ Workflow Jobs:
1. **Install Dependencies**
2. **Run Tests with Pytest**
3. **Deploy to Staging** – only on `staging` branch
4. **Deploy to Production** – only on release tags

### 🔐 Required Secrets:
- `STAGING_API_KEY`
- `PRODUCTION_API_KEY`
