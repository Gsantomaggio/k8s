### Istio Traffic Management HTTP test

To tun the example you need:

- [MiniKube][1] 
- [istioctl][2] 
- https://skaffold.dev/ (optional)

# Run the example

- Start Minukube
- Setup istio:
  ```
 istioctl manifest apply --set profile=default
```
- wait until all the serives are ready
- enable minikue tunnel:
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


