## questions
- how a layer 7 load balancer is different from the layer 4 load balancer.
- how to distribute the client requests/network 
- how to detect the servers that are online.
- which load balancer algorithm?
  - ensure HA and reliability by sending requests to servers 
- start a web server


## step 1
-  create a basic server that can start-up, listen for incoming connections and then forward them to a single server.
   -  it will startup and listen for connections on a specified port
   -  forward the request made to the load balancer to a backend server. This involves opening a connection to a backend server, making the same request to it that we received, passing the result back to the client.
   -  how will you plan to handle the multiple concurrent requests?
-  my understanding
   -  load balancer is nothing but a simple web server that forwards requests to a single server.
## step2
- distribute the incoming requests b/w 2 servers using a basic round robin algorithm
- implement the round robin algorithm
  - how do we mark which request we have made to a specific backend server. A global data structure.


## step 3
- periodic health checks using ping-pong server within 10 seconds(configurable time interval)
- 

## todo
-[ ] how to include certain commands to automatically run through bazel.