## Handle two RabbitMQ clusters with ISTIO

An example how to handle two  versions of rabbitmq cluster using istio.

The idea is to manage to versions and migrate form V1 to V2, with the istio gateway, virtual-services and destination rules .

Each cluster has three nodes.


[![Schema](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")


## Install it on minikube

Requirements:
 - `kubectl label namespace default istio-injection=enabled` enables Istio Injection
 - install istio, with some profile, for example:
   ```
   istioctl manifest apply --set profile=demo
   ```
   wait until all the components are up and running.



Install the clusters, step by step:

 - `kubectl apply -k rabbitmq-service/` Install The RabbitMQ service and the RBAC
 - `kubectl apply -k istio-configuration/` Install the three istio virtual service and the gateway
 - `kubectl apply -k rabbitmq-cluster-v1` Install the RabbitMQ cluster Version 1 ( three nodes)
 - `kubectl apply -k rabbitmq-cluster-v2` Install the RabbitMQ cluster Version 2 ( three nodes)
 
or you can use directly the file: `deploy.sh` 


## Test the AMQP port

use the script: `/telnet.sh`, here should be the result:

```
$ ./telnet.sh
10.104.37.167:5672
Trying 10.104.37.167...
Connected to 10.104.37.167.
Escape character is '^]'.
test 

AMQP    Connection closed by foreign host.
```
(The ip can change)


## Hostname resolution
You need to resolve the following hostnames:
 - `rabbitmqv1.test` (for the http ui  `Version 1` http://rabbitmqv1.test:15672/#/)
 - `rabbitmqv2.test`(for the http ui `Version 2` http://rabbitmqv2.test:15672/#/)
 - `rabbitmq.test` (for the amqp connections  `amqp://rabbitmq.test/`)


I used `dnsmasq.conf` in this way:

```
domain=test
address=/test/10.99.177.215
```

Where `10.99.177.215` is the `custom-gateway` external IP given by:
```
minikube tunnel
```
## RabbitMQ Gateway

Check the RabbitMQ ingress gateway:
```
kubectl get svc  rabbitmq-ingressgateway -n istio-system -o wide
NAME                      TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                          AGE     SELECTOR
rabbitmq-ingressgateway   LoadBalancer   10.104.37.167   10.104.37.167   5672:30896/TCP,15672:32747/TCP   3m57s   app=rabbitmq-ingressgateway,custom=ingressgateway
```

## Blue Green Update

Change the `weight` parameter on the `rabbitmq-app-tcp` VirtualService (`rabbitmq-istio.yaml`)


### Enable MTLS 

To test the cluster with MTLS you have to install/update ISTIO to use the mtls mode, for ex:
```
 istioctl manifest apply --set profile=demo \
  --set values.global.mtls.auto=true \
  --set values.global.mtls.enabled=false
```

Then uncomment `- mtls.yaml` on the file `istio-configuration/kustomization.yaml`

### Without Istio

The example can work also without istio, of course you don't have the traffic management feature.

 - be sure you don't have istio label enabled, if yes remove it `kubectl label namespace default istio-injection-`
 
 then deploy the yaml(s) without istio:
 - `kubectl apply -k rabbitmq-service`
 - `kubectl apply -k rabbitmq-cluster-v1` 
 - `kubectl apply -k rabbitmq-cluster-v2`
