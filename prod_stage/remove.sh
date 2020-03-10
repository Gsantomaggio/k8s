#!/usr/bin/zsh
kubectl delete -k deploy/application
kubectl delete -k deploy/istio-configuration
##kubectl label namespace staging istio-injection=enabled

