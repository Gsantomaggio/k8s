buildimage:
	docker build . -t books

testlocalimage: buildimage
	docker run -d -p 3000:3000 books

build-minikube-image:
	eval $(minikube docker-env)
	docker build . -t books
