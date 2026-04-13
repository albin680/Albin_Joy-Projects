from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout, get_user_model

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from decimal import Decimal, InvalidOperation

from django.conf import settings

from django.views.decorators.csrf import csrf_exempt

from .models import Vendor, Category, Booking, Complaint, CustomerProfile, VendorPortfolio



import razorpay

from decimal import Decimal

from .models import Vendor, Category, Booking, Complaint, CustomerProfile



from django.http import HttpResponseForbidden





def role_required(role):

    def decorator(view_func):

        def wrapper(request, *args, **kwargs):

            if request.user.is_authenticated and request.user.role == role:

                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("You are not authorized to view this page")

        return wrapper

    return decorator



User = get_user_model()





# ---------------- HOME ----------------

def home_view(request):

    categories = Category.objects.all()

    vendors = Vendor.objects.filter(is_verified=True).order_by('-created_at')[:6]

    return render(request, "home.html", {"categories": categories, "vendors": vendors})





# ---------------- SEARCH ----------------

from django.db.models import Q

from django.core.paginator import Paginator







def vendor_search(request):

    query = request.GET.get("q")

    location = request.GET.get("location")

    category = request.GET.get("category")

    min_price = request.GET.get("min_price")

    max_price = request.GET.get("max_price")

    sort = request.GET.get("sort")



    # Start with queryset

    vendors = Vendor.objects.filter(is_verified=True)



    # 🔎 Search by name OR category

    if query:

        vendors = vendors.filter(

            Q(business_name__icontains=query) |

            Q(category__name__icontains=query)

        )



    # 📍 Location filter

    if location:

        vendors = vendors.filter(location__icontains=location)



    # 📂 Category filter

    if category:

        vendors = vendors.filter(category_id=category)



    # 💰 Price filter

    if min_price:

        vendors = vendors.filter(base_price__gte=min_price)



    if max_price:

        vendors = vendors.filter(base_price__lte=max_price)



    # ↕ Sorting

    if sort == "low":

        vendors = vendors.order_by("base_price")

    elif sort == "high":

        vendors = vendors.order_by("-base_price")

    else:

        vendors = vendors.order_by("-created_at")



    # ✅ PAGINATION MUST BE LAST

    paginator = Paginator(vendors, 6)

    page_number = request.GET.get("page")

    vendors = paginator.get_page(page_number)



    categories = Category.objects.all()



    return render(request, "search_results.html", {

        "vendors": vendors,

        "categories": categories

    })



# ---------------- VENDOR DETAIL ----------------

from decimal import Decimal



def vendor_detail(request, vendor_id):

    vendor = get_object_or_404(Vendor, id=vendor_id)



    advance_amount = vendor.base_price * Decimal("0.60")



    return render(request, "vendor_detail.html", {

        "vendor": vendor,

        "advance_amount": advance_amount

    })





# ---------------- CUSTOMER REGISTER ----------------

# ---------------- CUSTOMER REGISTER (Updated) ----------------

def customer_register(request):

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        confirm_password = request.POST.get("confirm_password") # Added

        phone = request.POST.get("phone")



        # ❌ Check for password mismatch

        if password != confirm_password:

            messages.error(request, "Passwords do not match")

            return redirect("customer_register")



        if User.objects.filter(Q(username=username) | Q(email=email)).exists():

            messages.error(request, "Username or Email already exists")

            return redirect("customer_register")



        user = User.objects.create_user(

            username=username,

            email=email,

            password=password,

            phone=phone,

            role="customer"

        )

        CustomerProfile.objects.create(user=user)

        messages.success(request, "Registration successful. Please login.")

        return redirect("login")

    return render(request, "customer_register.html")



# ---------------- VENDOR REGISTER ----------------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction, IntegrityError
from django.db.models import Q
from decimal import Decimal, InvalidOperation
from .models import User, Vendor, Category

def register_vendor(request):

    categories = Category.objects.all()
    if request.method == "POST":
        # 1. Pricing Cleanup (Handles empty strings from form)
        def to_decimal(value):
            try:
                val = value.strip()
                return Decimal(val) if val else None
            except (InvalidOperation, ValueError, AttributeError):
                return None

        raw_base_price = request.POST.get('base_price', '')
        raw_plate_price = request.POST.get('price_per_plate', '')
        
        clean_base_price = to_decimal(raw_base_price)
        clean_plate_price = to_decimal(raw_plate_price)

        # 2. Collect Form Data
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        phone = request.POST.get("phone", "").strip()
        business_name = request.POST.get("business_name")
        location = request.POST.get("location")
        category_id = request.POST.get("category_id")

        # 3. Validations
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "vendor_registration.html", {"categories": Category.objects.all(), "data": request.POST})

        if User.objects.filter(Q(username=email) | Q(email=email)).exists():
            messages.error(request, "Email already registered")
            return render(request, "vendor_registration.html", {"categories": Category.objects.all(), "data": request.POST})
        
        if User.objects.filter(phone=phone).exists():
            messages.error(request, "This phone number is already registered.")
            return render(request, "vendor_registration.html", {"categories": Category.objects.all(), "data": request.POST})

        # 4. Atomic Database Operation
        try:
            with transaction.atomic():
                # Create the User first
                user = User.objects.create_user(
                    username=email, 
                    email=email,
                    password=password,
                    phone=phone,
                    role="vendor"
                )

                # Get the Category
                category = get_object_or_404(Category, id=category_id)

                # Create the Vendor Profile
                Vendor.objects.create(
                    user=user,
                    business_name=business_name,
                    category=category,
                    location=location,
                    phone=phone,
                    base_price=clean_base_price,
                    price_per_plate=clean_plate_price,
                    profile_pic=request.FILES.get("profile_pic"),
                    service_image=request.FILES.get("service_image"),
                    id_proof=request.FILES.get("id_proof")
                )

            messages.success(request, "Vendor registered! Please wait for admin approval.")
            return redirect("login")

        except Exception as e:
            # If anything fails, transaction.atomic rolls back the User creation
            messages.error(request, f"Registration failed: {str(e)}")
            return render(request, "vendor_registration.html", {"categories": Category.objects.all(), "data": request.POST})

    # GET Request
    categories = Category.objects.all()
    return render(request, "vendor_registration.html", {"categories": categories})


from django.db import transaction


# ---------------- LOGIN ----------------

def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")



        user = authenticate(request, username=username, password=password)



        if user:

            login(request, user)



            if user.role == "vendor":

                return redirect("vendor_dashboard")

            elif user.role == "admin":

                return redirect("admin_dashboard")

            else:

                return redirect("customer_dashboard")

        else:

            messages.error(request, "Invalid username or password")



    return render(request, "login.html")





# ---------------- LOGOUT ----------------

def logout_view(request):

    logout(request)

    return redirect("home")





# ---------------- INITIATE BOOKING ----------------

from datetime import datetime

import razorpay
from decimal import Decimal
from datetime import datetime
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Vendor, Booking

@login_required
def initiate_booking(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    
    if request.method == "POST":
        # 1. Date & Time Validation (Combining the two HTML fields)
        date_str = request.POST.get("event_date")
        time_str = request.POST.get("event_time")
        
        if not date_str or not time_str:
            return JsonResponse({"error": "Date and Time are required."}, status=400)

        try:
            # Combine into format: 2026-03-30T14:30
            dt_str = f"{date_str}T{time_str}"
            dt_obj = datetime.strptime(dt_str, "%Y-%m-%dT%H:%M")
            
            if settings.USE_TZ:
                from django.utils import timezone
                dt_obj = timezone.make_aware(dt_obj)
        except (ValueError, TypeError):
            return JsonResponse({"error": "Invalid date or time format."}, status=400)

        # 2. Check if Vendor is already booked
        if Booking.objects.filter(vendor=vendor, event_datetime__date=dt_obj.date(), status__in=['confirmed', 'pending']).exists():
            return JsonResponse({"error": "Vendor is already booked on this date."}, status=400)

        # 3. Calculate Dynamic Pricing
        total_amount = Decimal(str(vendor.base_price))
        food_type_price = request.POST.get("food_type")
        guest_count = request.POST.get("guest_count")

        if food_type_price and guest_count:
            try:
                catering_cost = Decimal(food_type_price) * int(guest_count)
                total_amount += catering_cost
            except (ValueError, TypeError):
                pass 

        # 4. Create the Booking Object
        # Note: 'event_pincode' matches HTML name 'event_pincode'
        booking = Booking.objects.create(
            customer=request.user,
            vendor=vendor,
            event_datetime=dt_obj,
            event_address=request.POST.get("event_address"),
            event_pincode=request.POST.get("event_pincode"), 
            customer_phone=request.POST.get("customer_phone"),
            total_amount=total_amount,
            status="pending"
        )

        # 5. Handle Advance Payment (60% Logic)
        advance = total_amount * Decimal("0.60")
        booking.advance_amount = advance
        booking.balance_amount = total_amount - advance
        
        # 6. Razorpay Integration
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            amount_in_paise = int(float(advance) * 100)
            order_data = {
                "amount": amount_in_paise,
                "currency": "INR",
                "payment_capture": "1"
            }
            order = client.order.create(data=order_data)
            
            booking.advance_order_id = order["id"]
            booking.save()

            # IMPORTANT: Return JsonResponse for the JavaScript fetch()
            return JsonResponse({
                "order_id": order["id"],
                "amount": amount_in_paise,
                "key": settings.RAZORPAY_KEY_ID,
                "business_name": vendor.business_name
            })
            
        except Exception as e:
            # Delete the pending booking if order creation fails
            booking.delete()
            return JsonResponse({"error": f"Gateway error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request method."}, status=405)
# ---------------- PAYMENT VERIFY ----------------





from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect

from django.contrib import messages

from django.conf import settings

from django.db.models import Q

import razorpay



from .models import Booking





@csrf_exempt

def payment_verify(request):

    if request.method == "POST":

        razorpay_payment_id = request.POST.get("razorpay_payment_id")

        razorpay_order_id = request.POST.get("razorpay_order_id")

        razorpay_signature = request.POST.get("razorpay_signature")



        booking = Booking.objects.filter(

            Q(advance_order_id=razorpay_order_id) |

            Q(balance_order_id=razorpay_order_id)

        ).first()



        if not booking:

            messages.error(request, "Booking not found.")

            return redirect("customer_dashboard")



        client = razorpay.Client(

            auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)

        )



        try:

            client.utility.verify_payment_signature({

                "razorpay_order_id": razorpay_order_id,

                "razorpay_payment_id": razorpay_payment_id,

                "razorpay_signature": razorpay_signature

            })

        except:

            messages.error(request, "Payment verification failed!")

            return redirect("customer_dashboard")



        booking.razorpay_payment_id = razorpay_payment_id



        # =========================

        # ADVANCE PAYMENT (60%)

        # =========================

        if booking.advance_order_id == razorpay_order_id:
            booking.advance_payment_id = razorpay_payment_id
            booking.advance_paid = True
            # Only set to confirmed if balance isn't already paid (unlikely but safe)
            if not booking.balance_paid:
                booking.status = "confirmed"
            messages.success(request, "Advance payment successful!")

        # BALANCE PAYMENT
        elif booking.balance_order_id == razorpay_order_id:
            booking.balance_payment_id = razorpay_payment_id
            booking.balance_paid = True
            # If balance is paid, the event process is effectively 'completed'
            booking.status = "completed" 
            messages.success(request, "Balance payment completed!")

        booking.save()

        booking.razorpay_payment_id = razorpay_payment_id # Optional legacy field

        booking.save()

        return redirect("booking_success")



    return redirect("customer_dashboard")







# ---------------- SUCCESS ----------------

def booking_success(request):

    return render(request, "booking_success.html")





# ---------------- CUSTOMER DASHBOARD ----------------

@login_required

def customer_dashboard(request):

    bookings = Booking.objects.filter(customer=request.user)

    return render(request, "customer_dashboard.html", {"bookings": bookings})





# ---------------- VENDOR DASHBOARD ----------------

from decimal import Decimal

from django.utils import timezone



from django.db.models import F
from decimal import Decimal

@login_required
def vendor_dashboard(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    bookings = Booking.objects.filter(vendor=vendor)

    total_earned = Decimal('0.00')
    pending_escrow = Decimal('0.00')

    for b in bookings:
        # 1. Calculate Released Earnings (What they have actually been sent)
        if b.advance_released:
            total_earned += b.advance_vendor_share() # Uses the 90% logic from model
        if b.balance_released:
            total_earned += b.balance_vendor_share() # Uses the 90% logic from model

        # 2. Calculate Pending Escrow (What is in the system but NOT yet released)
        if b.advance_paid and not b.advance_released:
            pending_escrow += b.advance_vendor_share()
        if b.balance_paid and not b.balance_released:
            pending_escrow += b.balance_vendor_share()

    context = {
        'vendor': vendor,
        'bookings': bookings,
        'total_earned': total_earned,
        'pending_escrow': pending_escrow,
    }
    return render(request, 'vendor_dashboard.html', context)

# ---------------- DISPUTE ----------------
from django.contrib import messages
@login_required
def complete_booking(request, booking_id):
    if request.method == "POST":
        booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
        
        # Check 1: Is the balance paid?
        if not booking.balance_paid:
            messages.error(request, "You must pay the balance before marking the event as completed.")
            return redirect('customer_dashboard')
            
        # Check 2: Has the event date passed?
        if timezone.now() < booking.event_datetime:
            messages.error(request, "You can only mark the event as completed after the event date/time.")
            return redirect('customer_dashboard')

        if booking.status == 'confirmed':
            booking.status = 'completed'
            booking.save()
            messages.success(request, "Event marked as completed! The vendor can now request their final payout.")
        else:
            messages.error(request, "This booking is already completed or in another state.")
            
    return redirect('customer_dashboard')

@login_required
def raise_complaint(request, booking_id):
    # This can just redirect to your existing dispute view 
    # or you can create a dedicated complaint form here.
    return redirect('raise_dispute', booking_id=booking_id)

@login_required

def raise_dispute(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)



    if request.method == "POST":

        Complaint.objects.create(

            booking=booking,

            reason=request.POST.get("reason"),

            evidence=request.FILES.get("evidence")

        )



        booking.status = "disputed"

        booking.save()



        return redirect("customer_dashboard")



    return render(request, "raise_complaint.html", {"booking": booking})





# ---------------- ADMIN LOGIN (Updated) ----------------

def admin_login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")



        # 1. Check for Hardcoded/Custom Credentials (Optional/Static)

        # Replace 'superadmin' and 'admin123' with your desired custom values

        if username == "admin" and password == "2026":

            # Find the admin user in the DB to initiate a real session

            user = User.objects.filter(role="admin").first()

            if user:

                login(request, user)

                return redirect("admin_dashboard")

            else:

                messages.error(request, "Static login recognized, but no Admin role user exists in DB.")

                return redirect("admin_login")



        # 2. Standard Database Authentication

        user = authenticate(request, username=username, password=password)



        if user and user.role == "admin":

            login(request, user)

            return redirect("admin_dashboard")

       

        messages.error(request, "Invalid admin credentials or not an admin account")



    return render(request, "admin_login.html")



# ---------------- ADMIN DASHBOARD ----------------

from decimal import Decimal


@login_required
@role_required('admin')
def admin_dashboard(request):
    bookings = Booking.objects.all().order_by('-id')
    pending_vendors = Vendor.objects.filter(is_verified=False)
    approved_vendors = Vendor.objects.filter(is_verified=True)

    platform_fees = Decimal('0.00')
    total_escrow_balance = Decimal('0.00')

    for b in bookings:
        # Step A: How much cash did the user actually pay?
        amount_collected = Decimal('0.00')
        if b.advance_paid:
            amount_collected += b.advance_amount
        if b.balance_paid:
            amount_collected += b.balance_amount

        # Step B: Where does that money go?
        # If the event is over OR payout is done, 10% of total collected is REVENUE.
        if b.status in ['completed', 'released'] or b.payout_released:
            platform_fees += (amount_collected * Decimal('0.10'))
            
            # Note: For completed/released events, Escrow is 0 because 
            # the liability is now a 'Payout Due' or 'Payout Done'.
        
        # If the event is still ongoing (Pending/Confirmed/Advance Paid), 
        # 90% of total collected sits in ESCROW.
        else:
            total_escrow_balance += (amount_collected * Decimal('0.90'))

    context = {
        "pending_vendors": pending_vendors,
        "approved_vendors": approved_vendors,
        "bookings": bookings,
        "platform_fees": platform_fees.quantize(Decimal('0.01')),
        "total_escrow_balance": total_escrow_balance.quantize(Decimal('0.01')),
        "active_disputes_count": Complaint.objects.filter(status='open').count(),
        "recent_disputes": Complaint.objects.filter(status='open').order_by('-created_at')[:5],
    }

    return render(request, "admin_dashboard.html", context)

# ---------------- APPROVE VENDOR ----------------

@login_required

def approve_vendor(request, vendor_id):

    vendor = get_object_or_404(Vendor, id=vendor_id)

    vendor.is_verified = True

    vendor.save()

    return redirect("admin_dashboard")

def approved_vendors(request):

    vendors = Vendor.objects.filter(is_verified=True)

    return render(request, "approved_vendors.html", {"vendors": vendors})





from datetime import date, timedelta



@login_required
@login_required
def pay_balance(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )

    # 1. Block if advance not paid
    if not booking.advance_paid:
        messages.error(request, "Advance must be paid first.")
        return redirect("customer_dashboard")

    # 2. Block if already paid
    if booking.balance_paid:
        messages.success(request, "Balance already paid.")
        return redirect("customer_dashboard")

    # --- Time Restriction Removed ---
    # Now proceeding directly to Razorpay order creation
    client = razorpay.Client(
        auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
    )

    try:
        order = client.order.create({
            "amount": int(float(booking.balance_amount) * 100),
            "currency": "INR",
            "payment_capture": "1"
        })

        booking.balance_order_id = order["id"]
        booking.save()

        return render(request, "balance_payment.html", {
            "booking": booking,
            "razorpay_order_id": order["id"],
            "razorpay_merchant_key": settings.RAZORPAY_KEY_ID,
            "amount": int(float(booking.balance_amount) * 100),
            "display_amount": booking.balance_amount,
            "currency": "INR"
        })
    except Exception as e:
        messages.error(request, f"Payment gateway error: {str(e)}")
        return redirect("customer_dashboard")


from django.utils import timezone
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages


@login_required
@role_required('admin')
def release_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    today = timezone.now().date()
    event_date = booking.event_datetime.date()

    # --- FORCE FULL RELEASE IF STATUS IS COMPLETED ---
    # This ignores the date check if the admin has already verified completion
    if booking.status == 'completed':
        if not booking.balance_paid:
            messages.error(request, "Cannot release full payout: Customer hasn't paid balance.")
            return redirect("admin_dashboard")
            
        booking.advance_released = True
        booking.balance_released = True
        booking.payout_released = True
        booking.status = 'released'
        booking.payout_date = timezone.now()
        booking.withdraw_requested = False
        booking.save()
        messages.success(request, f"Full Payout of ₹{booking.vendor_payout()} released for Booking #{booking.id}.")
        return redirect("admin_dashboard")

    # --- SCENARIO A: RELEASE ADVANCE ONLY (Before Event) ---
    if today < event_date:
        if booking.advance_paid and not booking.advance_released:
            booking.advance_released = True
            booking.save()
            messages.success(request, f"Advance of ₹{booking.advance_vendor_share()} released to vendor.")
        else:
            messages.error(request, "Advance already released or not yet paid.")

    # --- SCENARIO B: RELEASE REMAINING (On or After Event) ---
    else:
        if not booking.balance_paid:
            messages.error(request, "Customer hasn't paid the balance yet.")
        elif booking.balance_released:
            messages.warning(request, "Balance already released.")
        else:
            booking.balance_released = True
            booking.payout_released = True
            booking.status = 'released'
            booking.payout_date = timezone.now()
            booking.save()
            messages.success(request, "Balance released. Payout complete.")

    return redirect("admin_dashboard")


from django.utils import timezone

from datetime import timedelta



def auto_release_payments():

    today = timezone.now().date()



    bookings = Booking.objects.filter(

    status='completed',

    payout_released=False

)

    for booking in bookings:

        if today >= (booking.event_datetime.date() + timedelta(days=1)):

            booking.status = 'released'

            booking.payout_released = True

            booking.payout_date = timezone.now()

            booking.save()







@login_required
@role_required('vendor')
def request_withdraw(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, vendor__user=request.user)
    today = timezone.now().date()
    event_date = booking.event_datetime.date()

    # Case A: Before the Event (Advance Only)
    if today < event_date:
        if not booking.advance_paid:
            messages.error(request, "Customer hasn't paid the advance yet.")
        elif booking.advance_released:
            messages.warning(request, "Advance has already been sent to your account.")
        else:
            booking.withdraw_requested = True # Admin sees this as an Advance request
            booking.save()
            messages.success(request, "Withdrawal request for Advance (60%) sent to Admin.")

    # Case B: On or After the Event (Balance)
    else:
        if not booking.balance_paid:
            messages.error(request, "Customer hasn't paid the balance yet.")
        elif booking.balance_released:
            messages.warning(request, "Full payout has already been completed.")
        else:
            booking.withdraw_requested = True # Admin sees this as a Balance request
            booking.save()
            messages.success(request, "Withdrawal request for Balance (40%) sent to Admin.")

    return redirect("vendor_dashboard")



from django.shortcuts import get_object_or_404, render

from django.contrib.auth.decorators import login_required

from .models import Booking



@login_required

def booking_detail(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)



    return render(request, "booking_detail.html", {

        "booking": booking

    })

from django.utils import timezone

from decimal import Decimal



@login_required

def cancel_booking(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    if booking.status not in ['confirmed', 'pending']:

        messages.error(request, "Cannot cancel this booking.")

        return redirect('customer_dashboard')

   

    delta = booking.event_datetime - timezone.now()

    if delta.total_seconds() > 7*24*3600:

        refund = booking.advance_amount * Decimal('0.80')

    elif delta.total_seconds() > 1*24*3600:

        refund = booking.advance_amount * Decimal('0.40')

    else:

        refund = Decimal('0.00')



    booking.status, booking.refund_amount = 'cancelled', refund

    booking.save()

    messages.success(request, f"Cancelled. Estimated Refund: ₹{refund}")

    return redirect('customer_dashboard')





from django.contrib.auth import update_session_auth_hash



# ---------------- PASSWORD MANAGEMENT ----------------



from django.core.mail import send_mail

from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.encoding import force_bytes, force_str

from django.template.loader import render_to_string



# 1. User enters email here

# ---------------- PASSWORD MANAGEMENT ----------------



from django.utils.crypto import get_random_string

from .models import PasswordReset  # Ensure this is in your models.py



def forgot_password(request):

    if request.method == 'POST':

        email = request.POST.get('email')

        try:

            # We use 'User' which you defined as get_user_model() at the top

            u = User.objects.get(email=email)

           

            # 1. Generate a unique token

            token = get_random_string(length=6)

           

            # 2. Save/Update token in the database

            PasswordReset.objects.filter(user=u).delete() # Remove old tokens

            PasswordReset.objects.create(user=u, token=token)



            # 3. Create the reset link

            domain = request.get_host()

            reset_link = f'http://{domain}/reset/{token}/'

           

            # 4. Send email

            try:

                send_mail(

                    'Reset Your EventHub Password',

                    f'Hello {u.username},\n\nClick the link below to reset your password:\n{reset_link}',

                    settings.DEFAULT_FROM_EMAIL,

                    [email],

                    fail_silently=False

                )

                messages.success(request, "Reset link sent! Please check your email.")

                return redirect('login')

            except Exception:

                messages.error(request, "Network connection failed. Could not send email.")

                return redirect('forgot_password')



        except User.DoesNotExist:

            messages.info(request, "Email id not registered")

            return redirect('forgot_password')



    return render(request, 'forgot_password.html')





def reset_password(request, token):

    # Verify the token exists in our database

    password_reset = get_object_or_404(PasswordReset, token=token)

   

    if request.method == 'POST':

        new_password = request.POST.get('new_password')

        confirm_password = request.POST.get('confirm_password')

       

        if new_password and new_password == confirm_password:

            user_obj = password_reset.user

           

            # ✅ SECURE: Use set_password to hash the password

            user_obj.set_password(new_password)

            user_obj.save()

           

            # Delete the used token

            password_reset.delete()

           

            messages.success(request, "Password updated successfully! Please login.")

            return redirect('login')

        else:

            messages.error(request, "Passwords do not match.")

           

    return render(request, 'reset_password.html', {'token': token})

# Add this to your imports at the top

from django.template.loader import render_to_string

from django.http import HttpResponse



@login_required

def view_bill(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    return render(request, "view_bill.html", {

        'booking': booking,

        'platform_fee': booking.commission(),

        'subtotal': booking.vendor_payout(),

        'invoice_date': timezone.now(),

    })





from django.db import transaction



@login_required

@role_required('admin')

def resolve_dispute(request, complaint_id):

    complaint = get_object_or_404(Complaint, id=complaint_id)

    booking = complaint.booking



    if request.method == "POST":

        action = request.POST.get("action")

        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

       

        try:

            with transaction.atomic(): # Ensure DB and Payment states stay synced

                if action == "refund":

                    refunds_issued = 0

                    total_refunded = Decimal('0.00')



                    # 1. Refund Advance Payment

                    if booking.advance_paid and booking.advance_payment_id:

                        client.refund.create({

                            "payment_id": booking.advance_payment_id,

                            "amount": int(booking.advance_amount * 100)

                        })

                        refunds_issued += 1

                        total_refunded += booking.advance_amount



                    # 2. Refund Balance Payment (if it exists)

                    if booking.balance_paid and booking.balance_payment_id:

                        client.refund.create({

                            "payment_id": booking.balance_payment_id,

                            "amount": int(booking.balance_amount * 100)

                        })

                        refunds_issued += 1

                        total_refunded += booking.balance_amount



                    if refunds_issued > 0:

                        booking.status = 'cancelled'

                        booking.refund_amount = total_refunded

                        messages.success(request, f"Successfully refunded {refunds_issued} transactions (Total: ₹{total_refunded}).")

                    else:

                        messages.warning(request, "No successful payments found to refund.")

                        return redirect('admin_dashboard')



                elif action == "release":

                    booking.status = 'released'

                    booking.payout_released = True

                    booking.payout_date = timezone.now()

                    messages.success(request, "Dispute resolved: Payment released to vendor.")



                # Finalize resolution

                complaint.status = 'resolved'

                complaint.save()

                booking.save()

               

        except razorpay.errors.BadRequestError as e:

            messages.error(request, f"Razorpay rejected the refund: {str(e)}")

            return redirect('admin_dashboard')

        except Exception as e:

            messages.error(request, f"An unexpected error occurred: {str(e)}")

            return redirect('admin_dashboard')



        return redirect('admin_dashboard')



    return render(request, "admin/resolve_dispute.html", {"complaint": complaint})



import csv

from django.http import HttpResponse



@login_required

@role_required('admin')

def export_bookings_csv(request):

    response = HttpResponse(content_type='text/csv')

    response['Content-Disposition'] = 'attachment; filename="bookings_report.csv"'



    writer = csv.writer(response)

    writer.writerow(['Booking ID', 'Customer', 'Vendor', 'Total Amount', 'Platform Fee', 'Vendor Payout', 'Status', 'Date'])



    bookings = Booking.objects.all()

    for b in bookings:

        writer.writerow([

            b.id, b.customer.username, b.vendor.business_name,

            b.total_amount, b.commission(), b.vendor_payout(),

            b.get_status_display(), b.event_datetime

        ])



    return response
@login_required
@role_required('vendor')
def update_portfolio(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    user = request.user
    
    if request.method == "POST":
        vendor.business_name = request.POST.get('business_name')
        vendor.location = request.POST.get('location')
        vendor.phone = request.POST.get('phone') 
        user.phone = request.POST.get('phone')
        user.save()

        if request.FILES.get('profile_pic'):
            vendor.profile_pic = request.FILES.get('profile_pic')
        if request.FILES.get('id_proof'):
            vendor.id_proof = request.FILES.get('id_proof')

        vendor.save()

        portfolio_images = request.FILES.getlist('portfolio_images')
        for img in portfolio_images:
            VendorPortfolio.objects.create(vendor=vendor, image=img)

        messages.success(request, "Profile and portfolio updated successfully!")
        return redirect('vendor_dashboard')

    portfolio = vendor.portfolio_items.all()
    return render(request, "update_portfolio.html", {"vendor": vendor, "portfolio": portfolio})


from django.contrib import messages

from django.core.mail import send_mail

from django.conf import settings

from django.utils.crypto import get_random_string

from .models import User, PasswordReset