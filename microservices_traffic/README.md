### Istio Traffic Management HTTP test

To tun the example you need:

- [MiniKube](https://kubernetes.io/docs/setup/learning-environment/minikube/) 
- [istioctl](https://istio.io/docs/reference/commands/istioctl/)
- https://skaffold.dev/ (optional)

# Run the example

- Start Minukube
- Setup istio:
```
 istioctl manifest apply --set profile=default
```
- wait until all the services are ready
- enable minikue tunnel (separated shell):

```
minikube tunnel
```
- deploy the example:

```
cd dev_local
skaffold dev
```
- run the client:
```
 ./test_rest.sh
```

That's should be the result:
```
10.110.251.29:80
{
   "hostname" : "{hostname: books-app-v2-65c9dbfb9f-5h9dc}",
   "version" : "2.0.0.2",
   "books" : [
      {
         "title" : "Golang Programming",
         "author" : "John Doe"
      }
   ]
}

```

There are two versions running, and you can tune the traffic.


- tune the traffic by changing the `weight`:
```
http:
    - route:
        - destination:
            host: books-app
            subset: v1
          weight: 0
        - destination:
            host: books-app
            subset: v2
          weight: 100
```


