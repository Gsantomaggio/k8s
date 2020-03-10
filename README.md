# Production staging example
To run the demo checkot the prod_stage branch:
```
git checkout prod_stage
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
Build the needed images
```
cd web_app
docker build . -t web-app
cd ..
```
Export the minikube docker-env variables
```
eval $(minikube docker-env)
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
