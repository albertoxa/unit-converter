# Universal Unit Converter

A beautiful, mobile-friendly unit converter with a Python (FastAPI) backend and Next.js frontend, deployed on Vercel.

## What's Fixed

- **Tailwind CSS now compiles** — proper `tailwind.config.ts`, `postcss.config.js`, and `globals.css` with `@tailwind` directives
- **Dropdowns are never empty** — fallback data is embedded in the frontend. If the Python API fails, the UI still works with local data
- **Error handling** — shows a banner if the API is offline, but conversions still work
- **13 categories** — Length, Temperature, Weight, Volume, Digital Storage, Area, Speed, Time, Pressure, Energy, Light, Power, Angle

## Project Structure

```
unit-converter/
├── api/
│   └── index.py              # FastAPI backend (Vercel serverless)
├── app/
│   ├── page.tsx              # Home page
│   ├── layout.tsx            # Root layout (imports CSS!)
│   └── globals.css           # Tailwind directives + custom styles
├── components/
│   └── Converter.tsx         # Main UI (bulletproof)
├── lib/
│   └── units-data.ts         # Fallback data (never empty dropdowns)
├── package.json
├── requirements.txt          # Python deps
├── next.config.js
├── tailwind.config.ts
├── postcss.config.js
└── tsconfig.json
```

## Deploy to Vercel

### Option 1: GitHub (Recommended)

```bash
# 1. Push this code to your GitHub repo
git init
git add .
git commit -m "fix: tailwind + fallback data + 13 categories"
git branch -M main
git remote add origin https://github.com/YOURNAME/unit-converter.git
git push -u origin main
```

Then in Vercel dashboard → your project → **Git** → reconnect the repo → deploy.

### Option 2: Vercel CLI

```bash
npm i -g vercel
vercel login
vercel --prod
```

## Adding New Units

Open `api/index.py` and add a new `registry.register(...)` block before the API endpoints. The frontend will auto-detect it on page refresh.

Example:
```python
registry.register("currency",
    units={"usd":1.0,"eur":1.08,"gbp":1.27},
    base_unit="usd",
    symbols={"usd":"$","eur":"€","gbp":"£"})
```

## Troubleshooting

**Still ugly?** Make sure `globals.css` has `@tailwind base; @tailwind components; @tailwind utilities;`

**Still empty dropdowns?** Check browser DevTools → Network → `/api/categories`. If it 404s, the Python runtime isn't loading. Make sure `requirements.txt` exists at the root.

**Build fails?** Make sure `tailwind.config.ts` (not `.js`) is present and `postcss.config.js` exists.
