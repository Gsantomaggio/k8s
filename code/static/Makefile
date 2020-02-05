buildimage:
	docker build . -t static

testlocalimage: buildimage
	docker run -d -p 1000:1000 static

build-minikube-image:
	eval $(minikube docker-env)
	docker build . -t static
