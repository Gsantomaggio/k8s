package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	host, _ :=   os.Hostname()
	host =  fmt.Sprintf("<h1>{hostname: %s}</h1>", host)
	w.Write([]byte(host))
	w.Write([]byte("<h1><a href=\"/api/books/items\">Books Store API</a> </h1>"))
	w.Write([]byte("<h1><a href=\"/api/food/items\">Food Store API</a> </h1>"))
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK"))
}

func main() {
	log.Printf("[store] webstatic is starting")
	port := "2000"
	mux := http.NewServeMux()
	mux.HandleFunc("/", indexHandler)
	log.Printf("[store] webstatic is started")

	mux.HandleFunc("/healthz", healthHandler)
	http.ListenAndServe(":"+port, mux)

}
