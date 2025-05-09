# 🚀 Lightweight CI/CD Pipeline with Bash, Python & Cron (EC2 Linux + Nginx)

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

## Task 1:
### Create index.html:

<img width="290" alt="image" src="https://github.com/user-attachments/assets/0720bda1-bf6e-4f1d-afb6-3f003b0322b3" />


### Initialize Git and push to GitHub:

git init  <br>
git add .   <br>
git commit -m "Initial commit"   <br>
git remote add origin git@github.com:minnathdhani/ci-cd_pipeline-hvp.git  <br>
git push -u origin main  <br>


## Task 2: Configure Nginx 

sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl enable nginx
sudo rm -rf /var/www/html/*

##  Task 3: Write a Python Script to Check for New Commits:
check_updates.py

-![Screenshot 2025-05-08 010720](https://github.com/user-attachments/assets/06384970-99a3-42c3-a46a-b904a680a1bc)

-![Screenshot 2025-05-08 010801](https://github.com/user-attachments/assets/0b8c8868-38fc-4f9a-9011-465ba30c588d)


## Task 4: Write a Bash Script to Deploy the Code:

-![Screenshot 2025-05-08 011522](https://github.com/user-attachments/assets/3f61aca3-cb15-452f-aa69-3bf1d4d6049f)

-![Screenshot 2025-05-08 011535](https://github.com/user-attachments/assets/39c8c052-bd8b-48a0-89fd-a6c925d4545e)

## Give it execute permissions:

chmod +x /home/ec2-user/deploy.sh

## Task 5: Set Up a Cron Job to Run the Python Script:

corntab -e 
*/5 * * * * /usr/bin/python3 /home/ec2-user/check_commit.py >> /home/ec2-user/ci_cd_log.txt 2>&1


-![Screenshot 2025-05-08 011907](https://github.com/user-attachments/assets/5a4b7fa3-7316-4d2b-b579-2d49cd16d572)


## Task 6: Test the Setup

Modify your HTML on GitHub (e.g., change text or add more ). <br>
Wait for cron to execute (up to 5 mins). <br>
Visit your server's public IP to view updated content. <br>


✅ How It Works:

Every 5 minutes, the cron job runs the Python script. <br>
The script checks GitHub for new commits. <br>
If a new commit is found, it triggers the Bash script. <br>
The Bash script clones the latest code and reloads Nginx. <br>
Your deployed website is updated automatically. <br>

## Output:

-![Screenshot 2025-05-08 014046](https://github.com/user-attachments/assets/ed3f089d-2c4a-4427-a400-64933a6d91bd)



