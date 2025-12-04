PACKAGE_NAME=image_classification
VERSION=0.0.1
docker build -f Docker/Dockerfile -t image_classification:${VERSION} .
