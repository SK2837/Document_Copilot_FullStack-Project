from __future__ import annotations

from functools import lru_cache

from supabase import Client, create_client

from app.config import settings


@lru_cache(maxsize=1)
def get_service_client() -> Client:
    """Supabase client using the service-role key.

    Use for privileged backend writes (e.g. ingestion, admin queries).
    Never expose this client or its key to the frontend.
    """
    return create_client(str(settings.supabase_url), settings.supabase_service_role_key)


def get_user_client(jwt: str) -> Client:
    """Supabase client scoped to an authenticated user's JWT.

    PostgREST requests made through this client run as that user,
    so RLS policies are enforced automatically.
    """
    client = create_client(str(settings.supabase_url), settings.supabase_anon_key)
    client.postgrest.auth(jwt)
    return client
