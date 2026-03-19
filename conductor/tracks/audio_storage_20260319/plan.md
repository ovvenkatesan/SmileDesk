# Implementation Plan: Audio Recording, Transcription, and Sentiment Storage

## Phase 1: Setup Supabase Database and Storage Bucket
- [x] Task: Define Database Schema 5257036
    - [x] Write tests or validation scripts for schema verification.
    - [x] Implement SQL migration to create `calls` table (fields: `id`, `transcript`, `sentiment`, `audio_url`, `created_at`).
    - [x] Implement database trigger, `pg_cron`, or background job for the 30-day data retention policy.
- [x] Task: Setup S3 Storage Bucket 9c11474
    - [x] Configure a new Supabase Storage bucket named `call_recordings`.
    - [x] Set appropriate bucket security policies (RLS).
- [x] Task: Conductor - User Manual Verification 'Phase 1: Setup Supabase Database and Storage Bucket' (Protocol in workflow.md) [checkpoint: b8b67c1]

## Phase 2: LiveKit Call Recording & Storage
- [x] Task: Implement Audio Recording Configuration 92c27ac
    - [x] Write unit tests for recording configuration logic.
    - [x] Update `server/src/agent.py` to trigger LiveKit Egress or local recording to capture the call audio.
- [x] Task: Upload Audio to Supabase S3 80ddcd8
    - [x] Write unit tests for the Supabase storage client upload wrapper.
    - [x] Implement a post-call hook to save the file as MP3 and upload it to the `call_recordings` bucket, returning the URL.
- [x] Task: Conductor - User Manual Verification 'Phase 2: LiveKit Call Recording & Storage' (Protocol in workflow.md) [checkpoint: 572fb2e]

## Phase 3: Transcription and Sentiment Analysis
- [~] Task: Implement Post-Call Sentiment Analysis
    - [ ] Write unit tests for the sentiment analysis prompt and parser.
    - [ ] Implement an asynchronous function using Gemini to analyze the final aggregated transcript for sentiment (e.g., positive, neutral, negative, and a short summary).
- [ ] Task: Persist Call Data
    - [ ] Write unit tests for the database insertion logic.
    - [ ] Implement the final step in the post-call hook to insert the transcript, sentiment data, and S3 `audio_url` into the Supabase PostgreSQL database.
- [ ] Task: Conductor - User Manual Verification 'Phase 3: Transcription and Sentiment Analysis' (Protocol in workflow.md)