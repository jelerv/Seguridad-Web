#!/bin/bash
# ================================================
# start-lab.sh - Script de ayuda para el curso
# ================================================

echo "======================================================"
echo "   Seguridad en Aplicaciones Web y APIs - OWASP Top 10"
echo "======================================================"
echo ""

if [ -z "$1" ]; then
    echo "Uso: ./start-lab.sh [módulo]"
    echo ""
    echo "Módulos disponibles:"
    echo "  all          → Levanta todo el laboratorio"
    echo "  3,4,5,6,9,10 → Levanta Juice Shop + módulo específico"
    echo "  injection    → Levanta Juice Shop + DVWA + Injection"
    echo "  stop         → Detiene todos los contenedores"
    echo ""
    exit 1
fi

case $1 in
    "all")
        echo "Levantando todo el laboratorio..."
        docker compose up -d
        ;;
    "3"|"4"|"5"|"6"|"9"|"10")
        echo "Levantando Juice Shop + Módulo $1..."
        docker compose up -d juice-shop
        docker compose up -d vulnerable-*-$1 secure-*-$1 2>/dev/null || echo "Módulo $1 no encontrado"
        ;;
    "injection"|"7")
        echo "Levantando entorno para Injection (Módulo 7)..."
        docker compose up -d juice-shop dvwa vulnerable-injection secure-injection
        ;;
    "stop")
        echo "Deteniendo todos los contenedores..."
        docker compose down
        ;;
    *)
        echo "Opción no válida: $1"
        echo "Ejecuta './start-lab.sh' para ver las opciones"
        ;;
esac

echo ""
echo "¡Listo! Revisa el estado con: docker compose ps"
