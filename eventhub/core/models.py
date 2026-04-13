from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from decimal import Decimal
from django.core.validators import RegexValidator

# ---------------- USER MODEL ----------------
class User(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('vendor', 'Vendor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=15, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

# ---------------- CATEGORY MODEL ----------------
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name

# ---------------- TRANSPORTATION SUPPORT MODELS ----------------
# Moved up so Booking model can reference VendorVehicle
class VehicleType(models.Model):
    """Stores types like Car, Bus, Traveler"""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# ---------------- VENDOR MODEL ----------------
class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendor_profile')
    business_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    
    # Pricing & Services
    base_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        help_text="General starting price"
    )
    price_per_plate = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        null=True, 
        blank=True, 
        help_text="For Caterers: Price per person"
    )
    is_caterer = models.BooleanField(default=False)
    
    # Status & Verification
    is_available = models.BooleanField(default=True, help_text="Is the vendor currently accepting new bookings?")
    is_verified = models.BooleanField(default=False)
    
    # Media & Docs
    profile_pic = models.ImageField(upload_to='profiles/')
    service_image = models.ImageField(upload_to='services/')
    id_proof = models.FileField(upload_to='docs/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Phone Validation
    phone_regex = RegexValidator(
        regex=r'^\+?\d{9,15}$',
        message="Enter a valid phone number (e.g. +919876543210). Up to 15 digits allowed."
    )
    phone = models.CharField(
        validators=[phone_regex], 
        max_length=17, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.business_name

class VendorVehicle(models.Model):
    """Links a Vendor to specific vehicles and their KM rates"""
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    base_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Starting price for this vehicle from this vendor"
    )

    class Meta:
        unique_together = ('vendor', 'vehicle_type')

    def __str__(self):
        return f"{self.vendor.business_name} - {self.vehicle_type.name}"

class VendorPortfolio(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='portfolio_items')
    image = models.ImageField(upload_to='portfolio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Portfolio Item for {self.vendor.business_name}"

# ---------------- CUSTOMER MODEL ----------------
class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# ---------------- BOOKING MODEL ----------------
class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Advance Paid'),
        ('completed', 'Event Completed'),
        ('released', 'Paid to Vendor'),
        ('disputed', 'Disputed'),
        ('cancelled', 'Cancelled'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    
    # Event Logistics
    event_datetime = models.DateTimeField()
    event_venue_name = models.CharField(max_length=255)
    event_address = models.TextField()
    event_city = models.CharField(max_length=100)
    event_pincode = models.CharField(max_length=10)

    pickup_location = models.CharField(max_length=255, null=True, blank=True)
    drop_location = models.CharField(max_length=255, null=True, blank=True)
    # Transportation & Catering Specifics
    selected_vehicle = models.ForeignKey(VendorVehicle, on_delete=models.SET_NULL, null=True, blank=True)
    estimated_kilometers = models.PositiveIntegerField(null=True, blank=True)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)
    guest_count = models.PositiveIntegerField(null=True, blank=True)
    food_type_selected = models.CharField(max_length=100, null=True, blank=True)

    # Financials
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    # Razorpay Specifics
    advance_order_id = models.CharField(max_length=200, null=True, blank=True)
    balance_order_id = models.CharField(max_length=200, null=True, blank=True)
    advance_payment_id = models.CharField(max_length=255, blank=True, null=True)
    balance_payment_id = models.CharField(max_length=255, blank=True, null=True)
    advance_paid = models.BooleanField(default=False)
    balance_paid = models.BooleanField(default=False)
    
    # Status & Payouts
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    withdraw_requested = models.BooleanField(default=False)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    advance_released = models.BooleanField(default=False)
    balance_released = models.BooleanField(default=False)
    payout_released = models.BooleanField(default=False) 
    payout_date = models.DateTimeField(null=True, blank=True)

    def calculate_totals(self):
        vendor = self.vendor
        # 1. Transportation Logic
        if self.selected_vehicle and self.estimated_kilometers:
            vehicle = self.selected_vehicle
            km_cost = Decimal(self.estimated_kilometers) * vehicle.price_per_km
            self.total_amount = vehicle.base_price + km_cost
        # 2. Catering Logic
        elif vendor.is_caterer and self.guest_count and vendor.price_per_plate:
            self.total_amount = Decimal(self.guest_count) * vendor.price_per_plate
        # 3. Default
        else:
            self.total_amount = vendor.base_price or Decimal('0.00')

        if self.total_amount > 0:
            # Setting advance to 60% as per your HTML template logic
            self.advance_amount = (self.total_amount * Decimal('0.60')).quantize(Decimal('0.01'))
            self.balance_amount = self.total_amount - self.advance_amount

    def save(self, *args, **kwargs):
        if not self.total_amount or self.total_amount == 0:
            self.calculate_totals()
        super().save(*args, **kwargs)

    # Calculation Methods (90/10 Split Logic)
    def advance_vendor_share(self):
        return (self.advance_amount * Decimal('0.90')).quantize(Decimal('0.01'))

    def balance_vendor_share(self):
        return (self.balance_amount * Decimal('0.90')).quantize(Decimal('0.01'))

    def commission(self):
        return (self.total_amount * Decimal('0.10')).quantize(Decimal('0.01'))

    def vendor_payout(self):
        return (self.total_amount * Decimal('0.90')).quantize(Decimal('0.01'))

    def __str__(self):
        return f"Booking #{self.id} - {self.vendor.business_name}"

# ---------------- COMPLAINT & AUTH ----------------
class Complaint(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name='complaint')
    reason = models.TextField()
    evidence = models.ImageField(upload_to='disputes/', blank=True, null=True)
    status = models.CharField(max_length=20, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username}"