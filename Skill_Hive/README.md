 <!-- users App -->
Handles everything related to user profiles, skill sharing, and points.

Features:
User registration, login, and profile management.
Points system (earning and using points).
Skills listing and booking.
Integration with Zoom and Google Calendar for free users.
Models in users App:
UserProfile: Extends the default User model for profile details.
ActionPoint: Tracks points earned by actions.
Skill: Users list skills they can offer.

 <!-- courses App -->
Handles all premium content and certifications.

Features:
Uploading and managing premium learning materials.
Tracking user progress for premium content.
Generating certifications for completed courses.
Models in courses App:
PremiumContent: Stores premium resources.
UserProgress: Tracks course completion for premium users.
Certification: Generates and stores user certifications

 <!-- membership App -->
Manages free vs. premium memberships, payments, and upgrades.

Features:
Membership subscription management.
Payment integration (e.g., M-Pesa, PayPal).
Differentiating user access levels.
Models in membership App:
Membership: Tracks subscription status (free/premium).
Payment: Records transactions for points or subscriptions.