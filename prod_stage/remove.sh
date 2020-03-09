#!/usr/bin/zsh
kubectl apply -k deploy/application
kubectl apply -k deploy/istio-configuration
kubectl label namespace staging istio-injection=enabled

