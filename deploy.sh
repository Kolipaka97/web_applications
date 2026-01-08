#!/bin/bash
docker-compose pull
docker-compose down
docker-compose up -d

sleep 10
curl http://localhost:5001

