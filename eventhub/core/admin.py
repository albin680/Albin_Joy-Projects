from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User, CustomerProfile, Vendor, Booking, Category, Complaint

# --- 1. Custom User Admin ---
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff')
    # Use add_fieldsets for the creation form and fieldsets for the edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Role Information', {'fields': ('role', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Information', {'fields': ('role', 'phone')}),
    )

admin.site.register(User, CustomUserAdmin)

# --- 2. Customer & Category ---
admin.site.register(CustomerProfile)
admin.site.register(Category)

# --- 3. Vendor Admin ---
@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'user', 'category', 'location', 'is_verified_status', 'created_at')
    list_filter = ('is_verified', 'category', 'location')
    search_fields = ('business_name', 'user__email', 'location')
    actions = ['approve_vendors']

    def is_verified_status(self, obj):
        if obj.is_verified:
            return format_html('<b style="color:green;">✔ Verified</b>')
        return format_html('<b style="color:red;">✘ Pending</b>')
    is_verified_status.short_description = "Status"

    def approve_vendors(self, request, queryset):
        queryset.update(is_verified=True)
    approve_vendors.short_description = "Mark selected vendors as Verified"

# --- 4. Booking (Escrow) Admin ---
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'vendor', 'total_amount', 'get_commission', 'get_vendor_payout', 'status_tag')
    list_filter = ('status', 'event_datetime')
    readonly_fields = ('total_amount',) 
    actions = ['release_escrow_funds', 'freeze_payments']

    def get_commission(self, obj):
        return f"₹{obj.commission()}"
    get_commission.short_description = "Hub Fee (10%)"

    def get_vendor_payout(self, obj):
        return f"₹{obj.vendor_payout()}"
    get_vendor_payout.short_description = "Vendor Cut (90%)"

    def status_tag(self, obj):
        colors = {
            'pending': 'gray',
            'confirmed': 'blue',
            'completed': 'orange',
            'released': 'green',
            'disputed': 'red',
        }
        return format_html(
            '<span style="color: {}; font-weight: bold; text-transform: uppercase;">{}</span>',
            colors.get(obj.status, 'black'),
            obj.status
        )
    status_tag.short_description = "Escrow Status"

    def release_escrow_funds(self, request, queryset):
        # Logic: Only release if the event is actually marked as completed
        updated = queryset.filter(status='completed').update(status='released')
        self.message_user(request, f"Funds released for {updated} bookings.")
    release_escrow_funds.short_description = "✅ Release funds for completed events"

    def freeze_payments(self, request, queryset):
        queryset.update(status='disputed')
    freeze_payments.short_description = "⚠️ Freeze selected payments (Dispute)"

# --- 5. Complaints (Dispute Resolution) ---
@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('booking', 'status', 'created_at')
    readonly_fields = ('reason', 'evidence', 'booking')
    actions = ['refund_customer', 'pay_vendor']

    def refund_customer(self, request, queryset):
        for complaint in queryset:
            booking = complaint.booking
            booking.status = 'disputed' # Or add 'refunded' to your STATUS_CHOICES
            booking.save()
            complaint.status = 'resolved_refund'
            complaint.save()
    refund_customer.short_description = "⚠️ Refund Customer (Penalize Vendor)"

    def pay_vendor(self, request, queryset):
        for complaint in queryset:
            booking = complaint.booking
            booking.status = 'released'
            booking.save()
            complaint.status = 'resolved_paid'
            complaint.save()
    pay_vendor.short_description = "✅ Resolve Dispute: Release to Vendor"