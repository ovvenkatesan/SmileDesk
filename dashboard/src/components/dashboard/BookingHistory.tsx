import { ScrollArea } from "@/components/ui/scroll-area";

export function BookingHistory() {
  const bookings = [
    { id: 101, date: "Mar 18, 09:00 AM", type: "Emergency", status: "Confirmed" },
    { id: 102, date: "Mar 19, 02:00 PM", type: "Checkup", status: "Rescheduled" },
    { id: 103, date: "Mar 20, 10:30 AM", type: "Consultation", status: "Confirmed" },
  ];

  return (
    <ScrollArea className="h-full">
      <div className="space-y-4">
        {bookings.map((booking) => (
          <div key={booking.id} className="p-3 border rounded-lg bg-card hover:border-primary transition-colors">
            <div className="flex justify-between items-center mb-1">
              <span className="font-semibold text-sm">{booking.type}</span>
              <span className="text-xs text-muted-foreground">{booking.status}</span>
            </div>
            <div className="text-sm text-foreground">{booking.date}</div>
          </div>
        ))}
      </div>
    </ScrollArea>
  );
}