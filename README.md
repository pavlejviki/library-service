###
Implement Borrowing List & Detail endpoint
Initialize borrowings app
Add borrowing model with constraints for borrow_date, expected_return_date, and actual_return_date.
Implement a read serializer with detailed book info
Implement list & detail endpoints
Implement Create Borrowing endpoint
Implement create a serializer
Validate book inventory is not 0
Decrease inventory by 1 for book
Attach the current user to the borrowing
Implement and create an endpoint
Add filtering for the Borrowings List endpoint
Make sure all non-admins can see only their borrowings
Make sure borrowings are available only for authenticated users
Add the `is_active` parameter for filtering by active borrowings (still not returned)
Add the `user_id` parameter for admin users, so admin can see all users’ borrowings, if not specified, but if specified - only for concrete user
Implement return Borrowing functionality
Make sure you cannot return borrowing twice
Add 1 to book inventory on returning
Add an endpoint for it
### 

