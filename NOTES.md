# Next Steps: Frontend-Backend Integration

## Current State
- Frontend: deployed on GitHub Pages, uses `localStorage`.
- Backend: running on `localhost:5000`, works with `curl`.
- They don't talk to each other yet.

## The Problem
- GitHub Pages (HTTPS) cannot talk to localhost (HTTP) due to browser security.
- Backend is not publicly accessible.

## Plan

### Path B: Deploy the backend publicly
1. Create a free account on Render (or Railway/Fly.io).
2. Push the backend to GitHub.
3. Connect the GitHub repo to Render.
4. Render will build and deploy the Flask app, giving it a public HTTPS URL.
5. Update `script.js` in the frontend to use the new URL instead of `localStorage`.
6. Test end-to-end.

### Before deploying
- Make sure `CORS(app)` is configured correctly.
- Remove `debug=True` in production.
