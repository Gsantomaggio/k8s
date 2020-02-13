package main

import (
	"encoding/json"
	"fmt"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"log"
	"net/http"
	"os"
)

type Book struct {
	Author string `json:"author"`
	Title  string `json:"title"`
}

type Books struct {
	HostName string  `json:"hostname"`
	Books    []*Book `json:"books"`
	Version string  `json:"version"`

}

type Host struct {
	HostName string `json:"hostname"`
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK"))
}

func itemsHandler(w http.ResponseWriter, r *http.Request) {
	recordMetrics()
	log.Printf("[store] called the books API")
	getBooks(w)

}

func getVersion() string {
	return os.Getenv("BOOKS_VERSION")
}


func getBooks(w http.ResponseWriter) {
	books := &Books{}
	host, _ := os.Hostname()
	host = fmt.Sprintf("{hostname: %s}", host)
	books.HostName = host
	books.version = getVersion()
	
	books.Books = append(books.Books, &Book{Title: "Golang Programming", Author: "John Doe"})
	books.Books = append(books.Books, &Book{Title: "Kubernetes Programming", Author: "Alex Kubernetes"})
	books.Books = append(books.Books, &Book{Title: "Linux Networking", Author: "Mr Linux"})

	b, _ := json.Marshal(books)

	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(string(b)))
}

func main() {
	log.Printf("[store] books is starting...")
	port := "2200"
	mux := http.NewServeMux()
	mux.HandleFunc("/items", itemsHandler)
	log.Printf("[store] books is started")

	mux.HandleFunc("/healthz", healthHandler)
	go startProm()
	http.ListenAndServe(":"+port, mux)

}

func startProm() {
	log.Printf("[store] books- prom is starting...")
	http.Handle("/metrics", promhttp.Handler())
	http.ListenAndServe(":2112", nil)

}

func recordMetrics() {
	go func() {
		opsProcessed.Inc()
	}()
}

var (
	opsProcessed = promauto.NewCounter(prometheus.CounterOpts{
		Name: "books_number_of_get_items",
		Help: "The total number HTTP get books items",
	})
)
