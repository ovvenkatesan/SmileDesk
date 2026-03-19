import os
import re
import pytest

def test_schema_sql_contains_audio_url():
    """Verify that schema.sql has the audio_url column defined in calls table."""
    schema_path = os.path.join(os.path.dirname(__file__), '../../schema.sql')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_content = f.read()

    # Check for audio_url column in calls table
    # Looking for a match similar to: audio_url TEXT
    assert re.search(r'audio_url\s+TEXT', schema_content, re.IGNORECASE), "audio_url column not found in schema.sql"

def test_schema_sql_contains_retention_policy():
    """Verify that schema.sql includes the pg_cron schedule for 30-day retention."""
    schema_path = os.path.join(os.path.dirname(__file__), '../../schema.sql')
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_content = f.read()

    assert "CREATE EXTENSION IF NOT EXISTS pg_cron" in schema_content, "pg_cron extension not created"
    assert "cron.schedule" in schema_content, "cron.schedule not found"
    assert "30 days" in schema_content or "30_days" in schema_content, "30-day retention interval not found"
