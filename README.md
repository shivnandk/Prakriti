# Prakriti.com

Prakriti.com is an online plant store where users can buy plants, gardening tools, and accessories. The website is built using Django, Python, and Razorpay for payment integration.

## Features
- User registration and login
- Plant listings with detailed descriptions
- Shopping cart and checkout process
- Payment integration with Razorpay
- Admin panel to manage products and orders

## Requirements
- Python 3.x
- Django 5.1.3
- Pillow 11.0.0
- Razorpay 1.4.2
- Requests 2.32.3

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Prakriti.com.git
   ```

2. Navigate to the project folder:
   ```bash
   cd Prakriti.com
   ```

3. Create a virtual environment:
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

5. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

6. Run migrations:
   ```bash
   python manage.py migrate
   ```

7. Start the server:
   ```bash
   python manage.py runserver
   ```

## License
This project is licensed under the MIT License.
