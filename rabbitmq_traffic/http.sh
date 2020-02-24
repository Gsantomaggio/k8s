#!/bin/bash
export INGRESS_PORT=$(kubectl -n istio-system get service custom-gateway -o jsonpath='{.spec.ports[?(@.name=="http")].port}')
export INGRESS_HOST=$(kubectl -n istio-system get service custom-gateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo $INGRESS_HOST:$INGRESS_PORT

#telnet $INGRESS_HOST 31400
google-chrome $INGRESS_HOST:$INGRESS_PORT

