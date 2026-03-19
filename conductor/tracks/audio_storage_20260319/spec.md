# Specification: Audio Recording, Transcription, and Sentiment Storage

## Overview
This track implements the functionality to store call audio, transcriptions, and sentiment analysis for the Voice AI Orchestration pipeline. Audio files will be stored in Supabase S3, while the corresponding transcriptions and sentiment analysis metadata will be stored in a Supabase PostgreSQL database. This allows clinic owners and staff to review calls asynchronously.

## Functional Requirements
- **Audio Recording:** The system must record incoming calls via LiveKit.
- **Audio Processing & Storage:**
  - The recorded audio must be converted to or saved as an MP3 format.
  - The MP3 file must be uploaded to a configured Supabase S3 storage bucket.
- **Transcription:** The system must aggregate the real-time transcription of the call.
- **Sentiment Analysis:**
  - Sentiment analysis must be performed asynchronously after the call concludes.
  - The analysis should evaluate the overall tone and sentiment of the patient's interaction.
- **Data Persistence:**
  - The full transcript, sentiment analysis results, and a reference URL to the audio file in S3 must be stored in the Supabase PostgreSQL database.
- **Data Retention:**
  - The system must enforce a 30-day retention policy. Recordings, transcripts, and sentiment data older than 30 days must be automatically purged or flagged for deletion.

## Non-Functional Requirements
- **Performance:** Post-call async processing should not block the main LiveKit agent worker or impact concurrent call capacity.
- **Security:** Audio files and database records must be securely accessed (e.g., using proper RLS policies in Supabase or authenticated backend access).

## Acceptance Criteria
- [ ] A test call is recorded, and the resulting audio is successfully saved as an MP3.
- [ ] The MP3 file is successfully uploaded to the specified Supabase S3 bucket.
- [ ] After the call, an asynchronous task successfully processes the transcript for sentiment analysis.
- [ ] A new record is created in the Supabase Postgres database containing the transcript, sentiment data, and a link to the S3 audio file.
- [ ] A mechanism (e.g., cron job or database trigger) is configured to purge records and files older than 30 days.

## Out of Scope
- Building the UI to display the transcripts/audio.
- Real-time sentiment analysis during the call.