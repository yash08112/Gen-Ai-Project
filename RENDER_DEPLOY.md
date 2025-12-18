# 🚀 Deploy Vecho Ai to Render.com (Step-by-Step)

## Prerequisites
- GitHub account
- Render.com account (free)
- Your Gemini API key

---

## Step 1: Push Code to GitHub

1. Initialize git (if not already):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. Create a new repository on GitHub

3. Push your code:
   ```bash
   git remote add origin https://github.com/yourusername/vecho-ai.git
   git branch -M main
   git push -u origin main
   ```

---

## Step 2: Deploy on Render

1. **Go to [render.com](https://render.com)** and sign up/login

2. **Click "New +" → "Web Service"**

3. **Connect your GitHub repository:**
   - Click "Connect account" if needed
   - Select your `vecho-ai` repository

4. **Configure the service:**
   - **Name:** `vecho-ai` (or any name you like)
   - **Region:** Choose closest to you
   - **Branch:** `main`
   - **Root Directory:** Leave empty (or `backend` if you want)
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`

5. **Add Environment Variables:**
   - Click "Advanced" → "Add Environment Variable"
   - Key: `GEMINI_API_KEY`
   - Value: Your actual Gemini API key
   - Click "Add"

6. **Click "Create Web Service"**

7. **Wait for deployment** (takes 2-5 minutes)

---

## Step 3: Update Your App URL

Once deployed, Render will give you a URL like:
`https://vecho-ai.onrender.com`

The frontend will automatically use `/api` when not on localhost, so it should work!

---

## Step 4: Test Your Deployment

1. Visit your Render URL
2. Try sending a message
3. Check if everything works!

---

## 🎉 Done!

Your Vecho Ai chatbot is now live on the internet!

---

## Troubleshooting

**Issue: App crashes on startup**
- Check logs in Render dashboard
- Make sure `GEMINI_API_KEY` is set correctly
- Verify `requirements.txt` has all dependencies

**Issue: API calls fail**
- Check browser console for CORS errors
- Verify API URL is correct (should be `/api` in production)

**Issue: Database errors**
- SQLite should work, but data resets on each deploy
- For persistent data, consider upgrading to PostgreSQL

---

## Next Steps (Optional)

1. **Custom Domain:** Add your own domain in Render settings
2. **Auto-Deploy:** Already enabled - every push to main deploys automatically
3. **Environment Variables:** Add more as needed
4. **Monitoring:** Check Render dashboard for logs and metrics

