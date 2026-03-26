# Pipeline DevSecOps Recomendado

- Git → SAST (SonarQube, Semgrep)
- Build → SCA (Dependency-Check, Trivy)
- Test → DAST (ZAP, Burp) + API Testing
- Pre-Production → Pentesting automatizado
- Production → Runtime Protection (WAF, RASP) + Logging centralizado
- Monitoring → SIEM + Alertas de anomalías
