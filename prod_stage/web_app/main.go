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
	env := fmt.Sprintf("<h1>{Test page for: %s}</h1>", getEnv() )
	w.Write([]byte(host))
	w.Write([]byte(env))
}


func getEnv() string {
	return os.Getenv("ENVIRONMENT")
}


func main() {
	log.Printf("[webapp]  is starting...")
	port := "2000"
	mux := http.NewServeMux()
	mux.HandleFunc("/", indexHandler)
	log.Printf("[webapp] is started")
	http.ListenAndServe(":"+port, mux)
}