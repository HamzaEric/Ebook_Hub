from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # --- CORRECTED PATHS ---
                  # Books stay at /library/ (e.g., /library/books/)
                  path('library/', include('books.urls')),

                  # Authors get their own path (e.g., /authors/add/)
                  path('authors/', include('authors.urls')),

                  # Genres get their own path (e.g., /genres/list/)
                  path('genres/', include('genres.urls')),

                  # Accounts get their own path (e.g., /accounts/login/)
                  path('accounts/', include('accounts.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)