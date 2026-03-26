#!/bin/bash
echo "Ejecutando OWASP ZAP Baseline Scan..."
docker run --rm -v $(pwd):/zap/wrk -t ghcr.io/zaproxy/zaproxy:stable zap-baseline.py \
    -t $1 \
    -r $2 \
    -c /zap/wrk/zap-baseline.conf
