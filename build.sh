set -e

echo "🧹 Limpiando contenedores antiguos..."
docker rm -f samplerunning 2>/dev/null || true

echo "🐳 Iniciando proceso de contenerización..."

docker build -t elden-api-app .

echo "🚀 Ejecutando contenedor 'samplerunning'..."
docker run --name samplerunning \
  -e ELDEN_CATEGORIA="weapons" \
  -e ELDEN_ITEM="Uchigatana" \
  elden-api-app

echo "✅ Proceso completado con éxito."