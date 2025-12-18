# 🚨 URGENT: Fix Render Deployment

## Problem
Render is still running `gunicorn app:app` instead of `gunicorn wsgi:app`

## Solution: Manual Update Required

Render is not picking up the Procfile. You need to **manually update the start command** in Render dashboard.

### Steps:

1. **Go to Render Dashboard**
   - Open your service
   - Click on **"Settings"** tab

2. **Update Start Command**
   - Find **"Start Command"** field
   - **Delete** the current command: `gunicorn app:app`
   - **Enter** this new command:
     ```
     gunicorn --bind 0.0.0.0:$PORT wsgi:app
     ```
   - Click **"Save Changes"**

3. **Redeploy**
   - Go to **"Events"** or **"Manual Deploy"** tab
   - Click **"Deploy latest commit"** or **"Clear build cache & deploy"**

## Alternative: If Start Command Field is Missing

If you don't see a "Start Command" field:

1. Go to **Settings** → **Environment**
2. Look for **"Build Command"** and **"Start Command"**
3. Make sure **Start Command** is: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`

## Verify Procfile is in Root

Make sure `Procfile` (no extension) is in your project root:
```
vecho-ai/
├── Procfile          ← Should be here
├── wsgi.py          ← Should be here
├── requirements.txt
├── backend/
└── frontend/
```

## After Update

Once you update the start command, Render should:
- ✅ Build successfully
- ✅ Start with: `gunicorn --bind 0.0.0.0:$PORT wsgi:app`
- ✅ Show "Listening at: http://0.0.0.0:XXXX" in logs
- ✅ Your app goes live!

## Still Not Working?

If it still fails, try this start command instead:
```
cd /opt/render/project/src && gunicorn --bind 0.0.0.0:$PORT wsgi:app
```

Or check the logs to see what directory Render is running from.

