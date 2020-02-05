package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

type Book struct {
	Author string `json:"author"`
	Title  string `json:"title"`
}

type Books struct {
	HostName string `json:"hostname"`
	Books []*Book `json:"books"`
}

type Host struct {
	HostName string `json:"hostname"`
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("OK"))
}

func itemsHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("[store] called the books API")
	books := &Books{}
	host, _ :=   os.Hostname()
	host =  fmt.Sprintf("{hostname: %s}", host)
	books.HostName = host
	book := &Book{}

	book.Title = "Hello"
	book.Author = "John Doe"

	books.Books = append(books.Books, &Book{Title: "Golang Programming", Author: "John Doe"})
	books.Books = append(books.Books, &Book{Title: "Kubernetes Programming", Author: "Alex Kubernetes"})
	books.Books = append(books.Books, &Book{Title: "Linux Networking", Author: "Mr Linux"})

	b, _ := json.Marshal(books)

	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json")
	w.Write([]byte(string(b)))

}

func main() {
	port := "2200"
	mux := http.NewServeMux()
	mux.HandleFunc("/items", itemsHandler)
	log.Printf("[store] books is started")

	mux.HandleFunc("/healthz", healthHandler)



	http.ListenAndServe(":"+port, mux)

}
