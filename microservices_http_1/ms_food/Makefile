buildimage:
	docker build . -t food 

testlocalimage: buildimage
	docker run -d -p 2000:2000 food

build-minikube-image:
	eval $(minikube docker-env)
	docker build . -t food
