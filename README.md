# Company Website - Under Construction

This is a minimal "under construction" landing page for your company domain.

## Files
- `index.html` - Main landing page
- `company_logo_light.svg` - Company logo (light version)
- `company_logo_dark.svg` - Company logo (dark version)

## Deployment to GitHub Pages

### Step 1: Create a new GitHub repository
1. Go to https://github.com/new
2. Name it something like `company-website` or your company name
3. Make it public
4. Don't initialize with README (we already have files)

### Step 2: Push this directory to the repository
```bash
cd company-website
git init
git add .
git commit -m "Initial commit: Under construction page"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
git push -u origin main
```

### Step 3: Enable GitHub Pages
1. Go to your repository on GitHub
2. Click "Settings" tab
3. Click "Pages" in the left sidebar
4. Under "Source", select "main" branch and "/" (root) folder
5. Click "Save"
6. GitHub will give you a URL like: `https://YOUR_USERNAME.github.io/REPO_NAME/`

### Step 4: Configure your IONOS domain
1. Log in to your IONOS account
2. Go to Domain & SSL
3. Click on your domain
4. Go to DNS settings
5. Add/Edit the following records:

**For apex domain (example.com):**
- Type: A
- Host: @
- Value: 185.199.108.153
- Add three more A records with values:
  - 185.199.109.153
  - 185.199.110.153
  - 185.199.111.153

**For www subdomain:**
- Type: CNAME
- Host: www
- Value: YOUR_USERNAME.github.io

### Step 5: Configure custom domain on GitHub
1. Back in your GitHub repository settings → Pages
2. Under "Custom domain", enter your domain (e.g., `example.com`)
3. Click "Save"
4. Wait for DNS check to complete (can take 24-48 hours)
5. Once verified, check "Enforce HTTPS"

## Local Testing
Simply open `index.html` in your web browser to preview the page locally.
