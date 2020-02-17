buildimage:
	docker build . -t books

testlocalimage: buildimage
	docker run -d -p 2200:2200 -p 2112:2112 books

build-minikube-image:
	eval $(minikube docker-env)
	docker build . -t books
