"use client";

import { useEffect, useState } from "react";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Button } from "@/components/ui/button";
import { UserX } from "lucide-react";

export function BookingHistory() {
  const [bookings, setBookings] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchBookings = () => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/bookings`)
      .then((res) => res.json())
      .then((data) => {
        setBookings(data);
        setIsLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching Bookings:", err);
        setIsLoading(false);
      });
  };

  const markNoShow = (bookingId: string) => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/bookings/${bookingId}/no-show`, {
      method: "POST"
    })
    .then(() => fetchBookings())
    .catch((err) => console.error("Error marking no-show:", err));
  };

  useEffect(() => {
    fetchBookings();
    const interval = setInterval(fetchBookings, 10000);
    return () => clearInterval(interval);
  }, []);

  if (isLoading && bookings.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground animate-pulse">Loading bookings...</div>;
  }

  if (bookings.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground">No recent bookings found.</div>;
  }

  return (
    <ScrollArea className="h-full">
      <div className="space-y-4 pr-4">
        {bookings.map((booking) => (
          <div key={booking.id} className="p-3 border rounded-lg bg-card hover:border-primary transition-colors">
            <div className="flex justify-between items-start mb-2">
              <div>
                <span className="font-semibold text-sm block">{booking.patient_number}</span>
                <span className="text-xs text-muted-foreground">{booking.type}</span>
              </div>
              <div className="flex flex-col items-end gap-1">
                <span className={`text-[10px] px-2 py-0.5 rounded-full ${booking.status === 'Cancelled' || booking.is_no_show ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`}>
                  {booking.is_no_show ? 'No-Show' : booking.status}
                </span>
                {!booking.is_no_show && booking.status !== 'Cancelled' && (
                  <button 
                    onClick={(e) => { e.stopPropagation(); markNoShow(booking.id); }}
                    className="text-[10px] flex items-center gap-1 text-muted-foreground hover:text-red-600 transition-colors"
                  >
                    <UserX className="h-3 w-3" /> Mark No-Show
                  </button>
                )}
              </div>
            </div>
            <div className="text-sm text-foreground font-medium">
              {new Date(booking.date).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', dateStyle: 'medium', timeStyle: 'short' })}
            </div>
          </div>
        ))}
      </div>
    </ScrollArea>
  );
}
