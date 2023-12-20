Step 1
In this step your goal is to create a REST API that will allow a client to add a URL to the list of URLs that are currently shortened.

You will need to consider where you are going to store the shortened URLs and the full URL they expand to. I’d suggest using some form of database for persistence. Either SQL or NoSQL will work for this. I used an in memory store for my version, but if I was going to deploy it, I’d probably use Redis. Why? Because I could use the version we built in the build your own Redis Server challenge for testing locally and when you come to deploying, Redis is also available on most cloud platforms.

You will also need to decide how you’re going to generate a short key for each URL. I’d suggest you read up about hash functions. Think carefully about how short you make it and the danger of shorter hashes colliding.

You should return a suitable HTTP status code when the request succeeds, along with the shortened URL, I decided to return it as JSON using the structure:

{
    "key":"wsf5f",
    "long_url":"https://www.google.com",
    "short_url":"http://localhost/wsf5f"
}


## questions
- which database to choose from?
- decide how you're going to generate a short key for each URL.  


## Input and Output
- given an input url the target is to get a shortened url along with the suitable httpstatus code.
- Create a idempotent API
  - when the URL already exists you have to return the shortened version of the URL
  - how to build your own UUID generator?


Step 2: 
  - redirect the request for the shortened URL. To do that return the relevant HTTP status code.
    - 302 and the location header.

Step 3:
- extend your REST API to accept a delete request, which should delete the shortened URL if it exists and take no action if it does not.



## Solution Approach
  - deciding for the backend framework?
    - flask and postgresql should be easier to use and understand.

  - how to generate a short key for each URL?
    - relying on the Base62 conversion? but why? 
      - since we can have a max of 1000 billion URLs, if we can use 62 characters, for the short url having length n we can have total 62^n URLs.
      - let us say that our length, n=7 and we can serve 62^7 ~= 3500 billion URLs.
      - because read it somewhere it is much better but how?
      - for base 62 how will you generate the sequential id or the UUID?s
      - how to build a UUID generator?