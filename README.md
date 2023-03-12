# Group 7: 'GeekText'

## Sprint 3: Implement half of the HTTP routes
### Feature Checklist 
*Book Rating and Commenting*
- [x] Must be able to create a rating for a book by a user on a 5 star scale with a date-stamp
- Logic: Create a rating for a book given by a user. 
- HTTP Request Type: POST 
- Parameters Sent: Rating, User Id, Book Id
- Response Data: None
- [x] Must be able to create a comment for a book by a user with a date-stamp 
- Logic: Create a comment for a book given by a user. 
- HTTP Request Type: POST 
- Parameters Sent: Comment, User Id, Book Id 
- Response Data: None
- [ ] Must be able to retrieve a list of all comments for a particular book.
- Logic: Retrieve a list of comments for the book
- HTTP Request Type: GET 
- Parameters Sent: Book Id 
- Response Data: JSON list of comments
- [ ] Must be able to retrieve the average rating for a book 
- Logic: Given a book Id, calculate the average rating as a decimal.
- HTTP Request Type: GET 
- Parameters Sent: Book Id
- Response Data: Computed Average rating (decimal)
