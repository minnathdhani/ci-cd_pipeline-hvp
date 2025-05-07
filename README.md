# 🚀 Lightweight CI/CD Pipeline with Bash, Python & Cron (Ubuntu + Nginx)

This project demonstrates a lightweight CI/CD (Continuous Integration and Continuous Deployment) pipeline using Bash, Python, and cron jobs on an Ubuntu server. It is designed to automatically detect new commits to a GitHub repository and deploy them using Nginx to serve a simple HTML site.

---

## 📌 Key Features

- ✅ Automates deployment of a GitHub-hosted HTML project
- 🐍 Python script to monitor GitHub for new commits via API
- 🖥️ Bash script to clone and deploy latest changes
- ⏱️ Cron job for scheduled, hands-free deployment
- 🌐 Nginx for lightweight web hosting on EC2 Linux

---

## 📁 Folder Structure

check_commit.py          # Python script to check for new commits
deploy.sh                # Bash script to deploy latest code
last_commit.txt          # Stores last deployed commit SHA
simple-html-site/        # HTML project cloned from GitHub

git clone 


## Configure Nginx 

sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo rm -rf /var/www/html/*

## Python Script - check_commit.py




✅ How It Works:

Every 5 minutes, the cron job runs the Python script.
The script checks GitHub for new commits.
If a new commit is found, it triggers the Bash script.
The Bash script clones the latest code and reloads Nginx.
Your deployed website is updated automatically.

🧪 Testing

Modify your HTML on GitHub (e.g., change <h1> text). <br>
Wait for cron to execute (up to 5 mins). <br>
Visit your server's public IP to view updated content. <br>

🔐 Security Notes

Never expose your GitHub token publicly.
Use environment variables or .env files for secure token management in production.
Ensure your Ubuntu server has firewall and SSH hardening in place.

📌 Requirements:

Python 3.x
Nginx
EC2 Linux

