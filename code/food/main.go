package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
)

type Food struct {
	Type   string `json:"type"`
	Source string `json:"source"`
}

type Foods struct {
	HostName string  `json:"hostname"`
	Foods    []*Food `json:"foods"`
}

type Host struct {
	HostName string `json:"hostname"`
}


func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("OK"))
}

func itemsHandler(w http.ResponseWriter, r *http.Request) {
	log.Printf("[store] food the books API")

	foods := &Foods{}
	host, _ := os.Hostname()
	host = fmt.Sprintf("{hostname: %s}", host)
	foods.HostName = host

	foods.Foods = append(foods.Foods, &Food{Type: "Pasta", Source: "Italy"})
	foods.Foods = append(foods.Foods, &Food{Type: "Sushi", Source: "Japan"})
	foods.Foods = append(foods.Foods, &Food{Type: "Baguette", Source: "France"})

	b, _ := json.Marshal(foods)

	w.WriteHeader(http.StatusOK)
	w.Header().Set("Content-Type", "application/json")

	w.Write([]byte(string(b)))

}

func main() {
	port := "2100"
	mux := http.NewServeMux()

	mux.HandleFunc("/items", itemsHandler)
	log.Printf("[store] food is started")

	mux.HandleFunc("/healthz", healthHandler)


	http.ListenAndServe(":"+port, mux)
}
