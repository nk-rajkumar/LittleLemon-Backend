
# Restaurant webapp (Django) 

This Django-based web application provides a user-friendly platform for customers to make reservations at the Little Lemon restaurant. Users can view the menu, select a date and time for their reservation, and provide their contact information.

## Features

- User-friendly booking form
- Allows users to input their first name, last name, guest count, date, time, and comments.
- Displays the restaurant's menu items with descriptions and prices.
## Technologies Used
- Python
- Django 
- HTML/CSS/JavaScript
- SQLite (default database)

## Run Locally

Clone the project and the run the python file

```bash
  git clone https://github.com/nk-rajkumar/LittleLemon-Backend
```
Navigate to the project directory:
```bash
cd Littlelemon/Restaurant
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```
Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```
Run migrations:
```bash
python manage.py migrate
```
Start the development server:
```bash
python manage.py runserver
```
- ctrl + c to stop the server

## Usage:

1. Access the application in your web browser at http://127.0.0.1:8000/.   
2. Navigate to the "Book a Reservation" page.
3. Fill out the reservation form and click "Submit Reservation".
4. The reservation will be saved to the database.

## Admin creation
```bash
python manage.py createsuperuser
```
Fill the credentials


## Admin Interface:

1. Access the admin panel at http://127.0.0.1:8000/admin/.
2. Log in using the admin credentials you created during installation.
3. View and manage bookings under the "Bookings" section.
## Screenshots 

![Screenshot (238)](https://github.com/user-attachments/assets/3c217057-ef53-41cc-92b9-337f21ad073b)

![Screenshot (240)](https://github.com/user-attachments/assets/65b8c84b-b9d2-4759-99c6-ae35603db11b)

![Screenshot (239)](https://github.com/user-attachments/assets/a94a30d2-9029-45e6-a6c1-234ae16a46cd)

![Screenshot (241)](https://github.com/user-attachments/assets/59a5f58b-ae7b-4e9b-965c-86e7549e1f34)

![Screenshot (242)](https://github.com/user-attachments/assets/c5b41190-c73d-4d12-a1ea-09314a5b3eec)

![Screenshot (243)](https://github.com/user-attachments/assets/99667845-38f5-48d9-af42-a2302875fb65)

![Screenshot (244)](https://github.com/user-attachments/assets/2e3a83a2-f22c-4885-b6ee-cb2ec97e1f01)

![Screenshot (245)](https://github.com/user-attachments/assets/c4397bcc-46d4-42b1-96a5-1d4cbe08ee9d)

![Screenshot (246)](https://github.com/user-attachments/assets/21fe7ddb-a0e7-4ad3-a3e7-50ca3674159d)

## Future Improvements

- Add a cart functionality for users to order from the menu.
- Improve the overall design for a better user experience.

## License

[MIT](https://choosealicense.com/licenses/mit/)

This project is licensed under the MIT License. Feel free to contribute or modify!

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to report bugs, please create an issue or submit a pull request.
