# Next Steps: Deploy the Backend to Render

## Current State
- ✅ Flask backend is working locally.
- ✅ Code is pushed to GitHub: `unfinished-business-api`
- ✅ `Procfile`, `gunicorn`, and `requirements.txt` are ready.
- 🚧 Not yet deployed to a public URL.

## Plan for Next Session

1. Go to render.com and sign up with GitHub.
2. Create a new "Web Service" and select the `unfinished-business-api` repo.
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: Free
4. Wait for the build, then copy the public URL.
5. Test: `https://<your-url>.onrender.com/projects`

## After Deployment
- [ ] Update the frontend `script.js` to use the Render URL instead of `localStorage`.
- [ ] Test end-to-end: add, finish, and delete projects from the live web app.
- [ ] Mark Version 3.0 complete in the frontend README.
