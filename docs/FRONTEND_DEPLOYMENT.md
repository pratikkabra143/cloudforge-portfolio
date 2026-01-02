# CloudForge Portfolio — Frontend Deployment

## Overview

The CloudForge frontend is a static website deployed independently from the backend using cloud-native static hosting. The deployment prioritizes simplicity, global availability, and zero server maintenance.

---

## Hosting Platform

The frontend is hosted on:
- Amazon S3 (static website hosting)

S3 is used purely as an object store for static assets:
- HTML
- CSS
- JavaScript

No server-side runtime is required.

---

## CDN and HTTPS

Traffic to the frontend is served through:
- Cloudflare DNS
- Cloudflare CDN
- Cloudflare-managed HTTPS

Cloudflare provides:
- Global caching
- TLS termination
- Custom domain support

---

## Deployment Automation

Frontend deployment is automated using GitHub Actions.

Workflow file:
- `.github/workflows/frontend-ci.yml`

Deployment process:
1. GitHub Actions triggers on changes to the `frontend/` directory
2. Static files are synced to the S3 bucket
3. Updated content becomes globally available via Cloudflare

The deployment is idempotent and requires no downtime.

---

## Cache Behavior

The frontend relies on CDN caching provided by Cloudflare.

Cache invalidation is handled implicitly through:
- Content updates
- Browser refresh
- CDN revalidation

Explicit cache-busting strategies can be added if required.

---

## Security Notes

- No backend credentials exist in the frontend
- S3 bucket access is restricted
- HTTPS is enforced at the CDN level

---

## Summary

The CloudForge frontend deployment demonstrates a serverless, low-maintenance approach to delivering static web content at global scale.