# flask-CI-CD-pipeline
flask-CI-CD-pipeline
## 🚀 GitHub Actions CI/CD Pipeline

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
