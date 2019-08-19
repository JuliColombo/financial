# Usage
Run in console to start the application:
`./dist/financial_exe/financial_exe runserver`

# API
### Get balance
**GET**
**http://localhost:8000/balance/**

Response:

``{"amount": 50}``

### Get all transactions
**GET**
**http://localhost:8000/transactions/**

Response:

``[{"amount": 5, "type": "credit", "id": "4374812792", "effectiveDate": "2019-08-19T21:00:46.575Z"}, {"amount": 5, "type": "credit", "id": "4374812288", "effectiveDate": "2019-08-19T21:00:47.663Z"}, {"amount": 5, "type": "debit", "id": "4374856192", "effectiveDate": "2019-08-19T21:00:51.288Z"}]``


### Get transaction by ID
**GET**
**http://localhost:8000/transactions/4327612640/**

Response:

``{"amount": 50, "type": "credit", "id": "4327612640", "effectiveDate": "2019-08-19T21:11:30.342Z"}``


### Create transaction
**POST**
**http://localhost:8000/transactions/**

Data:

``{
  "type": "credit",
  "amount": 25
}``

Response:

``{"amount": 25, "type": "credit", "id": "4327615664", "effectiveDate": "2019-08-19T21:15:40.733Z"}``

# Transactions List
See all credits (green) and debits (red) from account.

**GET**
**http://localhost:8000/history/**

![Screenshot](history.png)