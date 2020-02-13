#!/usr/bin/env bash
eval $(minikube docker-env)
kubectl apply  -f <(istioctl kube-inject -f deploy/book.yaml)
#kubectl apply  -f <(istioctl kube-inject -f deploy/books_v2.yaml)
kubectl apply  -f deploy/gateway.yaml
kubectl apply  -f deploy/route.yaml
