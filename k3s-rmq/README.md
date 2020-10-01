# Description
---
Install a lightweight Kubernetes stack for with a RabbitMQ Cluster.
Compontents:
 - [K3s](https://k3s.io/)
 - [RabbitMQ](www.rabbitmq.com)
 - [RabbitMQ Operator](https://www.rabbitmq.com/kubernetes/operator/operator-overview.html)
 


# How to install 
---

```bash
curl -sfL https://raw.githubusercontent.com/Gsantomaggio/k8s/wip/k3s-rmq/install |  bash -
```
The setup may require a few minutes...

Check the credentials and the url to access to the cluster.
As result you should have something like:
```
[INFO]  Management UI: http://192.168.1.75:15672
[INFO]  AMQP: 192.168.1.75:5672
[INFO]  Credentials:
username: 1ZZZWMCttegIIZSUKzdsyk39bhf4yyqP
password: aIMOJafZEngc_94ePchT778nU9zvutOI
```

Demo:

![](gif/rmqs.gif)


# Vagrant 
---

For non Linux users or just to deploy it in Vagrant:

WIP