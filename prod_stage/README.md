# Production staging example
To run the demo go to the directory:
```
cd prod_stage
```
Make sure you have minikube up and running:
```
minikube status
```
Open a new terminal window and start minikube tunnel (it's a blocking operation)
```
minukube tunnel
```
Export the minikube docker-env variables
```
eval $(minikube docker-env)
```
Build the needed images
```
cd web_app
docker build . -t web-app
cd ..
```
Deploy the example
```
./deploy.sh
```
Find the IP of the ingress
```
./getipingress.sh
```
Set the entries in /etc/hosts for production and staging as the output of the script suggests.

Test it with a browser:
```
http://production.test1
```
and
```
http://stage.test1
```
