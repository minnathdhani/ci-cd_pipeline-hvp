#!/bin/bash


REPO_URL="https://github.com/minnathdhani/ci-cd_pipeline-hvp.git"
LOCAL_REPO="/home/ec2-user/ci-cd_pipeline-hvp"
DEPLOY_DIR="/usr/share/nginx/html"

# Optional: Pull latest changes if repo already exists
if [ -d "$LOCAL_REPO" ]; then
  cd $LOCAL_REPO
  git pull
else
  git clone $REPO_URL $LOCAL_REPO
fi

# Copy index.html to Nginx root directory
sudo cp $LOCAL_REPO/index.html $DEPLOY_DIR/index.html

# Set permissions (optional but recommended)
sudo chmod 644 $DEPLOY_DIR/index.html

# Restart Nginx
sudo systemctl restart nginx

echo "Deployment complete. Visit your EC2 public IP to see the site."
