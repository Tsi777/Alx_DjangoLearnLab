from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from relationship_app.models import UserProfile

class Command(BaseCommand):
    help = 'Assign roles to existing users'
    
    def handle(self, *args, **options):
        # Create test users with different roles
        users_data = [
            {'username': 'admin', 'password': 'admin123', 'role': 'Admin'},
            {'username': 'librarian', 'password': 'librarian123', 'role': 'Librarian'},
            {'username': 'member', 'password': 'member123', 'role': 'Member'},
        ]
        
        for user_data in users_data:
            user, created = User.objects.get_or_create(username=user_data['username'])
            if created:
                user.set_password(user_data['password'])
                user.save()
                self.stdout.write(f"Created user: {user_data['username']}")
            
            # Get or create UserProfile and assign role
            profile, profile_created = UserProfile.objects.get_or_create(user=user)
            profile.role = user_data['role']
            profile.save()
            self.stdout.write(f"Assigned {user_data['role']} role to {user_data['username']}")
        
        self.stdout.write(
            self.style.SUCCESS('Successfully assigned roles to test users')
        )