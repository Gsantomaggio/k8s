#!/bin/bash
export INGRESS_PORT=$(kubectl -n istio-system get service rabbitmq-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="amqp")].port}')
export INGRESS_HOST=$(kubectl -n istio-system get service rabbitmq-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
echo $INGRESS_HOST:$INGRESS_PORT

#telnet $INGRESS_HOST 31400
telnet $INGRESS_HOST $INGRESS_PORT

