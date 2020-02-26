## Handle two RabbitMQ clusters with ISTIO

An example how to handle two  versions of rabbitmq cluster using istio.

The idea is to manage to versions and migrate form V1 to V2, with the istio gateway, virtual-services and destination rules .

Each cluster has three nodes.


[![Schema](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")


## Install it on minikube

Requirements:
 - Consul, I followed this [guide line](https://learn.hashicorp.com/consul/kubernetes/minikube)
 - `kubectl label namespace default istio-injection=enabled` enables Istio Injection


Install the clusters:

 - `kubectl apply -k rabbitmq-service/` Install The RabbitMQ service and the RBAC
 - `kubectl apply -k istio-configuration/` Install the three istio virtual service and the gateway
 - `kubectl apply -k rabbitmq-cluster-v1` Install the RabbitMQ cluster Version 1 ( three nodes)
 - `kubectl apply -k rabbitmq-cluster-v2` Install the RabbitMQ cluster Version 2 ( three nodes)

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
## Custom Gateway

To create the `custom-gateway` I used [helm](https://istio.io/docs/setup/install/helm/):

```
gateways:
  enabled: true
  custom-gateway:
    enabled: true
    labels:
      app: custom-gateway
    replicaCount: 1
    autoscaleMin: 1
    autoscaleMax: 5
    resources: {}
      # limits:
      #  cpu: 100m
      #  memory: 128Mi
      #requests:
      #  cpu: 1800m
      #  memory: 256Mi
    cpu:
      targetAverageUtilization: 80
    loadBalancerIP: ""
    loadBalancerSourceRanges: {}
    externalIPs: []
    serviceAnnotations: {}
    podAnnotations: {}
    type: LoadBalancer #change to NodePort, ClusterIP or LoadBalancer if need be
    #externalTrafficPolicy: Local #change to Local to preserve source IP or Cluster for default behaviour or leave commented out
    ports:
      ## You can add custom gateway ports
    - port: 15672
      targetPort: 15672
      name: http 
    - port: 5672
      targetPort: 5672
      name: amqp 
```

Here is the result:
```
kubectl get svc  custom-gateway -n istio-system -o wide
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                          AGE     SELECTOR
custom-gateway   LoadBalancer   10.99.177.215   10.99.177.215   15672:30179/TCP,5672:32634/TCP   3d20h   app=custom-gateway,release=istio
```

## Blue Green Update

Change the `weight` parameter on the `rabbitmq-app-tcp` VirtualService (`rabbitmq-istio.yaml`)



