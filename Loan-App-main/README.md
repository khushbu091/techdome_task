# Loan-App

Loan Application Task given by **Tech-Dome**

The Loan Management System is a Django web application designed to facilitate the management of loans. It allows customers to submit loan requests, admins to approve or reject loan requests, and customers to view and manage their loans.

## Features

- **Loan Creation**: Customers can submit loan requests specifying the loan amount and term.
- **Loan Approval**: Admins can approve or reject pending loan requests.
- **Loan Viewing**: Customers can view details of their loans.
- **Repayments**: Customers can make repayments on their loans, updating the loan status.
- **HTML Templates**: The application includes HTML templates for various pages, including a landing page, loan list, loan detail, repayment add, and success message.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Pr1s0ner627/Loan-App.git
    
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Apply database migrations:

    ```
    python manage.py migrate
    ```

4. Create a superuser (admin) account:

    ```
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```
    python manage.py runserver
    ```

6. Access the application at [http://localhost:8000/](http://localhost:8000/)

## Usage

1. Log in as an admin using the superuser account created during installation.
2. Approve or reject pending loan requests in the Django admin interface.
3. Customers can access the loan management features via the provided HTML templates.
4. Customers can submit loan requests, view their loans, and make repayments.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request to the main repository's `develop` branch.

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

This project was created by Khushbu Patel.
