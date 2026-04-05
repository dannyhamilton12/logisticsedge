# Netlify Deployment Setup for LogisticsEdge

## Overview
This guide provides step-by-step instructions to deploy the LogisticsEdge site to Netlify with continuous deployment from GitHub.

## Prerequisites
- GitHub repository: https://github.com/dannyhamilton12/logisticsedge (already exists)
- Netlify account (free plan sufficient)
- Domain: logisticsedge.co.uk (needs to be registered/configured)

## Step 1: Create Netlify Account
1. Go to https://netlify.com
2. Sign up with GitHub account (recommended for easier repo integration)
3. Complete account verification

## Step 2: Create New Site from Git
1. Click "Add new site" → "Import an existing project"
2. Choose "GitHub" as the Git provider
3. Authorize Netlify to access your GitHub account
4. Select the repository: `dannyhamilton12/logisticsedge`

## Step 3: Configure Build Settings
The `netlify.toml` file in the repo root will automatically configure:
- **Build command:** `npm run build`
- **Publish directory:** `dist`
- **Node version:** 22.12.0

Manual verification:
- Build command: `npm run build`
- Publish directory: `dist`
- Environment variables: None required

## Step 4: Deploy Initial Build
1. Click "Deploy site"
2. Wait for build to complete (2-3 minutes)
3. Check deploy log for errors
4. Visit the temporary Netlify URL (e.g., `https://amazing-name-123456.netlify.app`)

## Step 5: Configure Custom Domain

### Option A: Register logisticsedge.co.uk (Recommended)
1. Register domain through your preferred registrar
2. In Netlify: Site settings → Domain management → Add custom domain
3. Add `logisticsedge.co.uk`
4. Configure DNS records:
   ```
   Type: A
   Name: @
   Value: 75.2.60.5

   Type: CNAME
   Name: www
   Value: your-site-name.netlify.app
   ```
5. Enable HTTPS (automatic via Let's Encrypt)

### Option B: Use Alternative Domain
If logisticsedge.co.uk is unavailable:
1. Consider: logisticsedge.net, logistics-edge.co.uk, or similar
2. Update `astro.config.mjs` site URL to match chosen domain
3. Follow same DNS configuration steps

## Step 6: Verify Deployment
1. Check site loads at custom domain
2. Test key pages:
   - Homepage: `/`
   - Articles: `/articles/`
   - Products: `/products/`
3. Verify SEO elements:
   - Sitemap: `/sitemap-index.xml`
   - Meta tags and structure
4. Check mobile responsiveness

## Step 7: Enable Continuous Deployment
Continuous deployment is enabled by default:
- Push to `main` branch triggers automatic rebuild
- Build status visible in GitHub commits
- Failed builds prevent deployment

## Troubleshooting

### Build Fails
- Check Node.js version (requires ≥22.12.0)
- Verify dependencies with `npm install`
- Test build locally with `npm run build`

### Domain Issues
- DNS propagation can take 24-48 hours
- Use DNS checker tools to verify records
- Ensure registrar nameservers point to correct DNS provider

### Content Not Updating
- Clear browser cache
- Check if build succeeded in Netlify dashboard
- Force refresh with Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)

## Post-Deployment
- Monitor build notifications in Netlify dashboard
- Set up branch deploys for preview environments if needed
- Configure analytics and performance monitoring
- Consider Netlify CMS for content management

## Files Created
- `netlify.toml` - Build and deployment configuration
- `DEPLOYMENT.md` - This setup guide

## Support
- Netlify docs: https://docs.netlify.com
- Astro deployment guide: https://docs.astro.build/en/guides/deploy/netlify/