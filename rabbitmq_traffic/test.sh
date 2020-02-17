#!/bin/bash
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="tcp")].port}')
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo $INGRESS_HOST:$INGRESS_PORT

#telnet $INGRESS_HOST 31400
telnet $INGRESS_HOST $INGRESS_PORT

