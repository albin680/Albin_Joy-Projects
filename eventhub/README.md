EventHub: Comprehensive Event Service & Vendor Management System
EventHub is a sophisticated, full-stack digital marketplace designed to bridge the gap between event organizers and service providers. This platform streamlines the entire event planning process, from discovering specialized vendors to managing secure financial transactions through an integrated escrow system.

🌟 Project Overview
Planning an event involves coordinating multiple moving parts. EventHub simplifies this by providing a centralized hub where users can find everything from photographers and decorators to catering services. The core mission of this project is to provide a transparent, secure, and efficient ecosystem for both professional vendors and personal clients.

✨ Core Features & Functionalities
🏦 Secure Escrow Payment System
Razorpay Integration: Utilizes the Razorpay API for seamless and secure payment processing.

Escrow Logic: Implements a safety mechanism where payments are held securely and only released to vendors upon successful completion of the service, protecting both parties.

🏢 Vendor Ecosystem
Service Portfolio: Vendors can create rich profiles, list multiple services, upload price lists, and showcase their previous work.

Lead Management: A dedicated dashboard for vendors to track new inquiries, pending bookings, and payment history.

👤 User Experience
Smart Search & Filtering: Users can filter vendors by service type, location, and budget.

Booking Lifecycle: A transparent workflow allowing users to track their event status from "Pending" to "Confirmed" and "Completed."

🛡️ Administrative Control
Role-Based Access Control (RBAC): Strict security protocols ensure that Users, Vendors, and Administrators only see data relevant to their specific roles.

Dispute Resolution: Admin tools to oversee transactions and ensure the platform remains fair for all users.

🛠️ Technical Architecture & Stack
Layer  Technology
Backend :Python (Django / Flask Frameworks)
Frontend:"HTML5, CSS3, JavaScript (Bootstrap & Jinja2 Templates)"
Database:SQLite (Development) / MySQL or PostgreSQL (Production)
API Integration:Razorpay Payment Gateway API
Version Control:Git & GitHub

🚀 Installation & Local Setup
1. System Requirements
Python 3.8+
Virtual Environment (Recommended)

2. Cloning the Project

git clone https://github.com/albin680/Albin_Joy-Projects.git
cd EventHub

3. Setting Up the Environment

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
# Install required dependencies
pip install -r requirements.txt

4. Database Initialization

# Apply migrations (for Django)
python manage.py migrate
# Or run the setup script (for Flask)
python seed.py

5. Launch the Server

 python manage.py runserver



📈 Future Roadmap

AI Recommendations: Implementing machine learning to suggest vendors based on user preferences.

Chat System: Real-time communication between users and vendors.

Mobile App: Developing a dedicated Android/iOS version for on-the-go management.

Developed with ❤️ by Albin Joy