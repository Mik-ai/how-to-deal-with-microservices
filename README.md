# How to deal with microservices

What is going on?

- There is a common problem: many microservices use the same database, and when we make changes to the database, we need to fix each microservice.
- Here is a different approach, we store the structure of orm models in one place and give it away when necessary.
- Model names and fields remain unchanged, only the values change.
