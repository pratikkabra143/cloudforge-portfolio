# CloudForge Portfolio

A cloud-native portfolio platform featuring a globally distributed static frontend
(AWS S3 + Cloudflare CDN), a containerized Python backend, and modern DevOps workflows
with automated CI/CD pipelines powered by GitHub Actions.

The project is structured to reflect a real deployment setup rather than a mock or demo.

---

## 🚀 Project Status

- Infrastructure: Complete
- CI/CD Pipelines: Complete
- Backend API: Live (public, read-only)
- Frontend Delivery: Live (static hosting)

---

## 🌐 Live URL : https://pratikkabra.dev

Available Backend API endpoints:
- `/health` Health: https://api.pratikkabra.dev/health
- `/projects` Projects: https://api.pratikkabra.dev/projects

---

## 🧠 System Overview

- Static frontend hosting using AWS S3
- Global delivery and HTTPS via Cloudflare
- Containerized Python backend deployed on EC2
- Public, read-only API endpoints
- Automated CI pipelines for frontend and backend
- Gated CD pipelines for production deployments
- Secure handling of secrets and deployment artifacts
- Architecture and deployment documentation

---

## 🧱 Repository Structure

- `backend/` — Python Flask backend code
- `frontend/` — Static HTML/CSS/JS frontend code
- `docs/` — Documentation on architecture, CI/CD, and deployment
- `.github/workflows/` — GitHub Actions CI/CD pipeline definitions
- `README.md` — Project overview
- `docker-compose.yml` — Local development setup

---

## 🎯 CI/CD

- Frontend and backend pipelines handled via GitHub Actions
- Backend uses separate CI and CD workflows
- Docker images are built via CI and deployed automatically

Details are documented in `docs/CI_CD.md`.

---

## 📘 Documentation

- `docs/ARCHITECTURE.md` — System architecture and design
- `docs/CI_CD.md` — CI/CD pipelines and deployment strategy
- `docs/backend_deployment.md` — Backend deployment details
- `docs/FRONTEND_DEPLOYMENT.md` — Frontend hosting and delivery

---

## 🧠 Design Principles

- Infrastructure-first approach
- Clear separation of concerns
- Verifiable automation over hidden complexity
- Production-aligned patterns

---

See `NOTICE.md` for attribution and authenticity terms.