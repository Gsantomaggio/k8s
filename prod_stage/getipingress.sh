#!/usr/bin/env bash
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')

echo "If you are using minikube don't forget to execute \"minikube tunnel\" "
echo ""
echo ""
echo "Ingress Adress is:"
echo $INGRESS_HOST:$INGRESS_PORT

echo ""
echo ""

echo "To easy resolve the adress you can add the ip to the /etc/hosts file:"
echo $INGRESS_HOST  "staging.test"
echo $INGRESS_HOST  "production.test"






