# Deployment Guide for Vecho Ai

## 🚀 Recommended Deployment Platforms

### 1. **Render.com** (Recommended - Easiest)
- ✅ Free tier available
- ✅ Automatic deployments from GitHub
- ✅ Easy Flask setup
- ✅ Environment variables support
- ✅ Persistent storage for SQLite

**Steps:**
1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Create new "Web Service"
4. Connect GitHub repo
5. Settings:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `cd backend && python app.py` or use gunicorn
   - Environment: Python 3
6. Add environment variable: `GEMINI_API_KEY`

---

### 2. **Railway.app** (Great for Full-Stack)
- ✅ Free tier with $5 credit
- ✅ Automatic deployments
- ✅ Simple setup
- ✅ Good for Flask apps

**Steps:**
1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → Deploy from GitHub
4. Add environment variable: `GEMINI_API_KEY`
5. Deploy!

---

### 3. **PythonAnywhere** (Simple & Beginner-Friendly)
- ✅ Free tier available
- ✅ Easy Python hosting
- ✅ Good for learning

**Steps:**
1. Sign up at [pythonanywhere.com](https://www.pythonanywhere.com)
2. Upload files via web interface
3. Configure web app
4. Set environment variables

---

### 4. **Fly.io** (Modern & Fast)
- ✅ Free tier
- ✅ Global deployment
- ✅ Docker-based

---

### 5. **Vercel** (For Frontend + Serverless)
- ⚠️ Requires converting Flask to serverless functions
- ✅ Great for frontend
- ✅ Free tier

---

## 📋 Pre-Deployment Checklist

### 1. Move API Key to Environment Variable
- ✅ Don't hardcode API keys
- ✅ Use environment variables
- ✅ Add to `.env` file (local) and platform settings (production)

### 2. Update Database Path
- ✅ SQLite works for small apps
- ⚠️ For production, consider PostgreSQL (Render/Railway support it)

### 3. Use Production Server
- ✅ Replace Flask dev server with Gunicorn
- ✅ Add proper error handling

### 4. Update CORS Settings
- ✅ Configure allowed origins
- ✅ Remove `debug=True` in production

### 5. Static Files
- ✅ Ensure frontend files are served correctly
- ✅ Check image paths

---

## 🔧 Quick Setup Files Needed

1. **Procfile** (for Render/Railway)
2. **runtime.txt** (Python version)
3. **.env.example** (template for env vars)
4. **gunicorn** in requirements.txt

---

## 🎯 My Recommendation: **Render.com**

**Why Render?**
- Easiest setup
- Free tier is generous
- Automatic HTTPS
- Great documentation
- Perfect for Flask apps

**Estimated Setup Time:** 10-15 minutes

---

## 📝 Next Steps

1. Move API key to environment variable
2. Add production server (Gunicorn)
3. Create deployment configuration files
4. Push to GitHub
5. Deploy on chosen platform

