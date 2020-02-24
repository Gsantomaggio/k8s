## Handle two RabbitMQ clusters with ISTIO

An example how to handle two  versions of rabbitmq cluster using istio.

The idea is to manage to versions and migrate form V1 to V2, with the istio gateway, virtual-services and destination rules .

Each cluster has three nodes.


[![Schema](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")](https://github.com/Gsantomaggio/k8s/raw/wip/rabbitmq_traffic/img/img.png "Schema")
