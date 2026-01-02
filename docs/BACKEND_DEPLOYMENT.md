# CloudForge Portfolio — Backend Deployment

## Overview

This document describes how the CloudForge backend is deployed and operated in the production environment.
The frontend is deployed independently via static hosting and is documented in `FRONTEND_DEPLOYMENT.md`.

---

## Deployment Target

Backend deployment target:
- Amazon EC2 instance
- Amazon Linux 2023
- Free-tier eligible instance type

The EC2 instance runs a single containerized backend service.

---

## Container Runtime

The backend application is packaged as a Docker image.

Key characteristics:
- Flask-based REST API
- Containerized using Docker
- Stateless application design

Docker is installed directly on the EC2 instance and managed using
standard Docker commands.

---

## Network Configuration

The backend container:
- Listens internally on port `5000`
- Is exposed publicly via EC2 port `80`

Port mapping used:
80 -> 5000

This allows the service to be accessed through standard HTTP while keeping the application configuration unchanged.

---

## Service Exposure

Public access to the backend is provided through:
- A custom subdomain
- Cloudflare-managed DNS and HTTPS

Cloudflare terminates HTTPS at the edge and forwards traffic to the EC2 instance over HTTP.

---

## Container Lifecycle Management

The backend container is started with the following restart policy:
- `unless-stopped`

This ensures:
- Automatic container restart on EC2 reboot
- Automatic recovery after Docker daemon restarts
- Manual stops remain respected

---

## Deployment Automation

Backend deployment is fully automated via GitHub Actions.

The deployment workflow:
1. Pulls the latest approved Docker image
2. Stops the currently running container (if any)
3. Removes the old container
4. Starts a new container with the updated image

No manual SSH access is required for routine deployments.

---

## Security Notes

- SSH access is key-based only
- No password authentication enabled
- Only required ports are exposed publicly
- Application runs inside a containerized environment

---

## Summary

The CloudForge backend deployment prioritizes simplicity, reliability, and reproducibility while remaining close to real-world production practices.