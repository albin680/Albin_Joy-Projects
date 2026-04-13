from django.urls import path
from . import views

urlpatterns = [
    # --- 1. Main & Discovery ---
    path('', views.home_view, name='home'),
    path('search/', views.vendor_search, name='vendor_search'),
    path('vendor/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),

    # --- 2. Authentication ---
    path('register/customer/', views.customer_register, name='customer_register'),
    path('register/vendor/', views.register_vendor, name='register_vendor'),
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('reset-password-confirm/<uidb64>/<token>/', views.reset_password, name='reset_password_confirm'),

    # --- 3. Booking & Razorpay Flow ---
    # Unified booking initiation path
    path('booking/initiate/<int:vendor_id>/', views.initiate_booking, name='initiate_booking'),
    path('booking/pay-balance/<int:booking_id>/', views.pay_balance, name='pay_balance'),
    path('payment/verify/', views.payment_verify, name='payment_verify'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('booking/bill/<int:booking_id>/', views.view_bill, name='view_bill'),
    path('booking/cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),

    # --- 4. User Dashboards ---
    path('dashboard/', views.customer_dashboard, name='customer_dashboard'),
    path('vendor/dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('booking/<int:booking_id>/detail/', views.booking_detail, name='booking_detail'),
    path('booking/<int:booking_id>/dispute/', views.raise_dispute, name='raise_dispute'),
    path('vendor/update-profile/', views.update_portfolio, name='update_portfolio'),
    path('vendor/request-withdraw/<int:booking_id>/', views.request_withdraw, name='request_withdraw'),
    path('booking/complete/<int:booking_id>/', views.complete_booking, name='complete_booking'),
    path('booking/complaint/<int:booking_id>/', views.raise_complaint, name='raise_complaint'),

    # --- 5. Admin (HQ) ---
    path('hq/login/', views.admin_login_view, name='admin_login'),
    path('hq/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('hq/approve-vendor/<int:vendor_id>/', views.approve_vendor, name='approve_vendor'),
    path('hq/release-payment/<int:booking_id>/', views.release_payment, name='release_payment'),
    path('hq/resolve-dispute/<int:complaint_id>/', views.resolve_dispute, name='resolve_dispute'),
    path('hq/export-bookings/', views.export_bookings_csv, name='export_bookings_csv'),
    path('approved-vendors/', views.approved_vendors, name='approved_vendors'),
]