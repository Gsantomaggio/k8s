#!/usr/bin/zsh
kubectl delete -k rabbitmq-service
sleep 1
kubectl delete -k istio-configuration/
sleep 1
kubectl delete -k rabbitmq-cluster-v1
sleep 1
kubectl delete -k rabbitmq-cluster-v2
