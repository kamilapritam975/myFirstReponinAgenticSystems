# Answers

## 1. What is the role of query parameters in this request?

Query parameters are used to send additional information to the API.  
In this request, they help to:

- Search for repositories related to "python" using `q`
- Sort results by stars using `sort=stars`
- Arrange them in descending order using `order=desc`
- Limit the number of results using `per_page=5`

So, query parameters control what data we get from the API.

---

## 2. Why do we use response.json() instead of response.text?

We use `response.json()` because the API returns data in JSON format.  

- `response.json()` converts the data into a Python dictionary  
- It makes it easy to access values like `name` and `stargazers_count`

On the other hand:

- `response.text` gives raw string data  
- It is harder to work with and parse manually

So, `response.json()` is easier and more useful.