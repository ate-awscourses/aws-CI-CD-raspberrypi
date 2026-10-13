# Self-Hosted Edge Computing Portfolio & CI/CD Pipeline

An automated, self-hosted professional portfolio and backend API running entirely on a Raspberry Pi 5 at the edge. This project demonstrates full-stack infrastructure management, secure cloud integrations, and zero-touch CI/CD deployments using a $0.00 infrastructure stack.

## 🏗️ Architecture & Tech Stack
*   **Hardware:** Raspberry Pi 5
*   **OS/Environment:** Raspberry Pi OS, Python, virtual environments (`venv`)
*   **Web/API:** Flask, HTML/CSS/JavaScript
*   **Networking:** Cloudflare Quick Tunnels (secure public exposure bypassing NAT/port-forwarding)
*   **Database:** MariaDB (Local relational data storage)
*   **CI/CD:** Git, GitHub Webhooks (automated git pull on push events)
*   **Cloud Backup:** AWS S3, `boto3` SDK, Linux `crontab`

## 📊 System Diagram

```mermaid
graph TD
    subgraph "Edge Infrastructure (Raspberry Pi 5)"
        Flask[Flask API & Web Server]
        DB[(MariaDB)]
        Cron[Linux Cron Job]
        Script[Python: backup.py]

        Cron -->|Nightly at 00:00| Script
        Script -->|mysqldump| DB
    end

    subgraph "Cloud Services"
        CF[Cloudflare Tunnel]
        GH[GitHub Repository]
        S3[(AWS S3 Storage)]
    end

    User((Web Visitor)) -->|HTTPS| CF
    CF -->|Secure Reverse Proxy| Flask

    Dev((Developer)) -->|git push SSH| GH
    GH -->|Webhook Payload| CF
    
    Script -->|boto3 API| S3
