package main

import (
	"encoding/json"
	"fmt"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promauto"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"github.com/streadway/amqp"
	"log"
	"net/http"
	"os"
	"time"
)

type Book struct {
	Author string `json:"author"`
	Title  string `json:"title"`
}

type Books struct {
	HostName string  `json:"hostname"`
	Books    []*Book `json:"books"`
	Version  string  `json:"version"`
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK"))
}

func itemsHandler(w http.ResponseWriter, r *http.Request) {
	recordMetrics()
//	log.Printf("[store] called the books API")
	switch r.Method {
	case "GET":
		getBooks(w)
	case "POST":
		go writeMessageToRabbitMQ()
	}

}

func failOnError(err error, msg string) {
	if err != nil {
		log.Fatalf("%s: %s", msg, err)
	}
}
func writeMessageToRabbitMQ() {
	conn, err := amqp.Dial("amqp://test:test@rabbitmq-app.default:5672/")
	if err != nil {
		log.Fatalf("%s: %s", "FAIL RABBITMQ", err)
	} else {
		time.Sleep(2 * time.Second)
		defer conn.Close()
	}
}

func getBooks(w http.ResponseWriter) {
	books := &Books{}
	host, _ := os.Hostname()
	host = fmt.Sprintf("{hostname: %s}", host)
	books.HostName = host
	books.Version = getVersion()

	books.Books = append(books.Books, &Book{Title: "Golang Programming", Author: "John Doe"})
	//books.Books = append(books.Books, &Book{Title: "Kubernetes Programming", Author: "Alex Kubernetes"})
//	books.Books = append(books.Books, &Book{Title: "Linux Networking", Author: "Mr Linux"})
//	books.Books = append(books.Books, &Book{Title: "Distributed Application", Author: "Mr CAP"})

	b, _ := json.Marshal(books)

	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(string(b)))
}

func getVersion() string {
	return os.Getenv("BOOKS_VERSION")
}

func main() {
	log.Printf("[store] books is starting...")
	port := "2200"
	mux := http.NewServeMux()
	mux.HandleFunc("/", itemsHandler)
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
