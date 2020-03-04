#!/usr/bin/zsh
kubectl apply -k rabbitmq-service
sleep 3
kubectl apply -k istio-configuration/
sleep 3
kubectl apply -k rabbitmq-cluster-v1
sleep 3
kubectl apply -k rabbitmq-cluster-v2
