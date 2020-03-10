#!/usr/bin/env bash
kubectl apply -k deploy/application
kubectl apply -k deploy/istio-configuration
kubectl label namespace staging istio-injection=enabled
kubectl label namespace production istio-injection=enabled

