build-image:
	docker build . -t books

run-local-image: build-image
	docker run -d -p 2200:2200 books

build-minikube-image:
	eval $(minikube docker-env)
	docker build . -t books
