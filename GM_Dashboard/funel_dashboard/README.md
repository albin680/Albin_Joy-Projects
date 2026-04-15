General Manager Dashboard – Conversion Funnel Analytics


 // Project Objective:  This project is a data-driven dashboard designed to help business managers monitor lead progression across various stages of a sales funnel. It provides real-time insights into stage-wise performance, conversion rates, and drop-off points using a modern NoSQL-backed architecture.//


1. Tech Stack:

    a) Backend:Django 6.0 (Python)

    b) Database: MongoDB (using PyMongo for direct high-performance aggregation)

    c) Frontend: HTML5, Tailwind CSS, JavaScript (ES6+)

    d) Visualization: D3.js (SVG-based dynamic funnel)


2. System Architecture:

a) The system follows a modular service-oriented architecture:

    Data Layer: MongoDB stores lead event documents with timestamps.

    Service Layer (services.py): Handles complex MongoDB aggregation pipelines to calculate counts and rates dynamically.

    API Layer (views.py): Exposes structured JSON data for the frontend.

    Visualization Layer (funnel_viz.js): Uses D3.js to render a proportional funnel where the width of each stage represents the volume of leads.

b) Conversion LogicStep:

    Conversion Rate: Calculated as:

        Rate=Current Stage Count/Previous Stage Count*100
        
    Overall Conversion Rate: Calculated as:

    Efficiency=Converted Stage Count/Total Initial Leads*100


    Drop-off: Calculated as the absolute numerical difference between the current stage and the preceding stage.

3. Setup & Installation:
    a) Prerequisites: Python 3.10+MongoDB installed and running locally (mongodb://localhost:27017)
    
    b) Installation: Clone the repository and navigate to the project folder:

            Install dependencies:   [pip install -r requirements.txt]

    c) Database Seeding:  To visualize the dashboard immediately, run the seed script to generate 500+ mock lead events across the last 30 days:

            Bash Command: [python seed.py]

    d) Run the Server: Bash Command: [python manage.py runserver]
    
            Access the dashboard at: http://127.0.0.1:8000/


4. API Endpoints:
    GET /api/funnel/   Returns the aggregated funnel data.

    Query Params (Optional): start: Start date (YYYY-MM-DD)end: End date (YYYY-MM-DD)

        Response Format:  JSON{
        "summary": {"leads": 500, "conversions": 64, "rate": "12.8%"},
        "funnel": [
        {"stage": "Lead", "count": 500, "conversion_rate": 100, "drop_off": 0},
        ...
        ]
        }



5. Dashboard Features:
    KPI Cards: Instant view of total volume and success rates.

    Date Filtering: Update the entire funnel visualization by selecting specific date ranges.

    Interactive Funnel: Hover over stages to see specific drop-off numbers.

    Responsive Design: Fully functional on desktop and mobile browsers via Tailwind CSS.