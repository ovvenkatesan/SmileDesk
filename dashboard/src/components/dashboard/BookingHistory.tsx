"use client";

import { useEffect, useState } from "react";
import { ScrollArea } from "@/components/ui/scroll-area";

export function BookingHistory() {
  const [bookings, setBookings] = useState<any[]>([]);

  useEffect(() => {
    fetch("http://localhost:8000/api/dashboard/bookings")
      .then((res) => res.json())
      .then((data) => setBookings(data))
      .catch((err) => console.error("Error fetching Bookings:", err));
  }, []);

  if (bookings.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground">Loading bookings...</div>;
  }

  return (
    <ScrollArea className="h-full">
      <div className="space-y-4">
        {bookings.map((booking) => (
          <div key={booking.id} className="p-3 border rounded-lg bg-card hover:border-primary transition-colors">
            <div className="flex justify-between items-center mb-1">
              <span className="font-semibold text-sm">{booking.type}</span>
              <span className="text-xs text-muted-foreground">{booking.status}</span>
            </div>
            <div className="text-sm text-foreground">{new Date(booking.date).toLocaleString()}</div>
          </div>
        ))}
      </div>
    </ScrollArea>
  );
}