"use client";

import { useAuth } from "@/lib/AuthContext";
import { Button } from "@/components/ui/button";
import { RoiSnapshot } from "@/components/dashboard/RoiSnapshot";
import { AgentStatus } from "@/components/dashboard/AgentStatus";
import { CallLogs } from "@/components/dashboard/CallLogs";
import { BookingHistory } from "@/components/dashboard/BookingHistory";

export default function DashboardPage() {
  const { user, logout } = useAuth();

  return (
    <div className="min-h-screen bg-background p-4 md:p-8">
      <header className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-primary">Smile Garden Dashboard</h1>
          <p className="text-muted-foreground">Welcome back, {user?.phoneNumber}</p>
        </div>
        <Button variant="outline" onClick={logout}>Sign Out</Button>
      </header>

      {/* Bento Box Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-[200px]">
        {/* ROI Snapshot (Span 2 cols on md) */}
        <div className="md:col-span-2 row-span-1">
          <RoiSnapshot />
        </div>

        {/* Agent Status */}
        <div className="col-span-1 row-span-1">
          <AgentStatus />
        </div>

        {/* Call Logs (Span 2 cols, Span 2 rows) */}
        <div className="md:col-span-2 row-span-2 bg-card rounded-xl border shadow-sm p-6 flex flex-col">
          <h2 className="text-lg font-semibold text-primary mb-4">Recent Calls</h2>
          <div className="flex-1 overflow-auto">
             <CallLogs />
          </div>
        </div>

        {/* Booking History */}
        <div className="col-span-1 row-span-2 bg-card rounded-xl border shadow-sm p-6 flex flex-col">
          <h2 className="text-lg font-semibold text-primary mb-4">Booking History</h2>
          <div className="flex-1 overflow-hidden">
             <BookingHistory />
          </div>
        </div>
      </div>
    </div>
  );
}