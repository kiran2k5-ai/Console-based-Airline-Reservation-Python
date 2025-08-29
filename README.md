# ✈️ Airline Reservation System

A comprehensive console-based airline reservation system built with Python, featuring user management, flight booking, and administrative controls.

[![PyPI version](https://badge.fury.io/py/airline-reservation-system.svg)](https://badge.fury.io/py/airline-reservation-system)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Quick Start

### Install from PyPI (Recommended)
```bash
pip install airline-reservation-system
python -m airline_reservation_system
```

### Install from Source
```bash
git clone https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python.git
cd Console-based-Airline-Reservation-Python
poetry install
poetry run python -m airline_reservation_system
```

## 📋 Features

### 👤 User Management
- **User Registration**: Create new user accounts with email and password
- **User Login**: Secure authentication system
- **Profile Management**: Update user information
- **Account Deletion**: Remove user accounts

### ✈️ Flight Operations
- **Flight Search**: Search flights by destination, date, or flight number
- **Flight Details**: View comprehensive flight information
- **Flight Listings**: Browse all available flights
- **Real-time Data**: Live flight information from database

### 🎫 Booking System
- **Ticket Booking**: Reserve seats on available flights
- **Booking History**: View past and current bookings
- **Booking Modification**: Change booking details
- **Cancellation**: Cancel existing bookings with refund processing

### 🛠️ Admin Panel
- **Flight Management**: Add, update, and delete flights
- **User Oversight**: View and manage all registered users
- **Booking Analytics**: Monitor all system bookings
- **System Administration**: Complete control over the reservation system

## 🏗️ System Architecture

```
Console-based-Airline-Reservation-Python/
├── src/
│   └── airline_reservation_system/
│       ├── __init__.py
│       ├── __main__.py
│       ├── main.py          # Main application entry point
│       ├── user.py          # User management module
│       ├── admin.py         # Admin operations module
│       ├── flight.py        # Flight operations module
│       ├── booking.py       # Booking management module
│       └── db.py           # Database configuration
├── pyproject.toml          # Poetry configuration
└── README.md
```

## 🗄️ Database Schema

The system uses **Supabase** as the backend database with the following tables:

### Users Table
- `user_id` (Primary Key)
- `name`
- `email` (Unique)
- `password`
- `phone`

### Flights Table
- `flight_id` (Primary Key)
- `airline`
- `source`
- `destination`
- `departure_time`
- `arrival_time`
- `price`
- `available_seats`

### Bookings Table
- `booking_id` (Primary Key)
- `user_id` (Foreign Key)
- `flight_id` (Foreign Key)
- `booking_date`
- `passenger_count`
- `total_amount`
- `status`

## 🔧 Technology Stack

- **Language**: Python 3.8+
- **Database**: Supabase (PostgreSQL)
- **Package Management**: Poetry
- **Dependencies**: 
  - `supabase` - Database client
  - `python-dotenv` - Environment management

## 📖 Usage Examples

### Running the Application
```bash
# Install and run
pip install airline-reservation-system
python -m airline_reservation_system

# You'll see the main menu:
=== AIRLINE RESERVATION SYSTEM ===
1. Register User
2. Login User
3. Delete User
4. Update User
5. Admin
6. Quit
```

### User Registration
```
Enter the Number of the choice : 1
Enter User ID : USR001
Enter Name : John Doe
Enter E-Mail : john@example.com
Enter Password : ********
Enter Phone Number : +1234567890
```

### Flight Booking Process
```
Enter the Number of the choice : 2
Enter E-Mail : john@example.com
Enter Password : ********

=== USER MENU ===
1. Flights Details
2. Booking Tickets of Flights
3. Payments
4. Quit
```

## 🚀 Development

### Prerequisites
- Python 3.8 or higher
- Poetry package manager
- Supabase account (for database)

### Local Development Setup
```bash
# Clone the repository
git clone https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python.git
cd Console-based-Airline-Reservation-Python

# Install dependencies
poetry install

# Run the application
poetry run python -m airline_reservation_system
```

### Running Tests
```bash
# Run with Poetry
poetry run python -m airline_reservation_system

# Or install locally and test
pip install -e .
python -m airline_reservation_system
```

## 📦 Package Information

- **Package Name**: `airline-reservation-system`
- **PyPI**: https://pypi.org/project/airline-reservation-system/
- **Version**: 0.1.0
- **Author**: karthik-53
- **License**: MIT

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to functions and classes
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/airline-reservation-system/
- **GitHub Repository**: https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python
- **Issues**: https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python/issues
- **Releases**: https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python/releases

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/kiran2k5-ai/Console-based-Airline-Reservation-Python/issues) page
2. Create a new issue with detailed information
3. Contact via GitHub

## 🙏 Acknowledgments

- **Supabase** for providing excellent database services
- **Poetry** for modern Python package management
- **PyPI** for hosting the package distribution

---

**Built with ❤️ by [kiran2k5-ai](https://github.com/kiran2k5-ai)**

*Last Updated: August 29, 2025*
