-- Paste this into your Supabase SQL Editor to create the tables

CREATE TABLE IF NOT EXISTS calls (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    caller_number TEXT NOT NULL,
    start_time TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    duration_seconds INTEGER,
    status TEXT,
    outcome TEXT,
    transcript TEXT,
    sentiment TEXT,
    summary TEXT,
    audio_url TEXT
);

CREATE TABLE IF NOT EXISTS bookings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    patient_number TEXT,
    date TIMESTAMP WITH TIME ZONE,
    type TEXT,
    status TEXT
);

-- Insert some dummy data so your dashboard isn't empty
INSERT INTO calls (caller_number, start_time, duration_seconds, status, outcome, transcript, sentiment, summary, audio_url)
VALUES
('+1234567890', NOW() - INTERVAL '2 hours', 145, 'completed', 'booked_appointment', 'Agent: Hello, Smile Garden Dental. How can I help you today?\nCaller: Hi, I am in a lot of pain and need to see a dentist as soon as possible.\nAgent: I am so sorry to hear that. I can help you schedule an emergency appointment.', 'Anxious', 'Patient called with dental pain and scheduled an emergency appointment.', 'https://oxwpcoqdggvhrbeazcwb.supabase.co/storage/v1/object/public/call_recordings/test1.mp3'),
('+1987654321', NOW() - INTERVAL '5 hours', 65, 'completed', 'questions_answered', 'Agent: Welcome to Smile Garden Dental. How may I assist you?\nCaller: Hi, I just wanted to ask what time you open tomorrow?\nAgent: We open at 8:00 AM tomorrow.', 'Neutral', 'Patient inquired about opening hours.', 'https://oxwpcoqdggvhrbeazcwb.supabase.co/storage/v1/object/public/call_recordings/test2.mp3');

INSERT INTO bookings (patient_number, date, type, status)
VALUES
('+1234567890', NOW() + INTERVAL '1 day', 'Emergency', 'Confirmed'),
('+1987654321', NOW() + INTERVAL '2 days', 'Checkup', 'Rescheduled'),
('+1122334455', NOW() + INTERVAL '3 days', 'Consultation', 'Confirmed');

-- If you get Row Level Security (RLS) errors from your dashboard/API later, run this to allow anonymous reads:
ALTER TABLE calls ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public read access to calls" ON calls FOR SELECT USING (true);
CREATE POLICY "Allow public read access to bookings" ON bookings FOR SELECT USING (true);
-- To allow the backend to insert new calls without a service key (for now):
CREATE POLICY "Allow public insert to calls" ON calls FOR INSERT WITH CHECK (true);
CREATE POLICY "Allow public insert to bookings" ON bookings FOR INSERT WITH CHECK (true);

-- 30-day Data Retention Policy
-- Make sure pg_cron extension is enabled in your Supabase Database -> Extensions
CREATE EXTENSION IF NOT EXISTS pg_cron;

-- Schedule a job to delete calls older than 30 days every day at midnight
SELECT cron.schedule('delete-old-calls', '0 0 * * *', $$
  DELETE FROM calls WHERE start_time < NOW() - INTERVAL '30 days';
$$);
