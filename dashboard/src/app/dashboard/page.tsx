"use client";

import { useState, useEffect } from "react";
import { useAuth } from "@/lib/AuthContext";
import { Button } from "@/components/ui/button";
import { RoiSnapshot } from "@/components/dashboard/RoiSnapshot";
import { AgentStatus } from "@/components/dashboard/AgentStatus";
import { CallLogs } from "@/components/dashboard/CallLogs";
import { BookingHistory } from "@/components/dashboard/BookingHistory";
import { AdvancedStats } from "@/components/dashboard/AdvancedStats";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";

export default function DashboardPage() {
  const user = { phoneNumber: "Admin" }; const logout = () => { console.log("Logout clicked"); };
  const [selectedCallId, setSelectedCallId] = useState<string | null>(null);
  const [callDetails, setCallDetails] = useState<any | null>(null);
  const [loadingDetails, setLoadingDetails] = useState(false);

  useEffect(() => {
    if (selectedCallId) {
      setLoadingDetails(true);
      fetch(`http://localhost:8000/api/dashboard/calls/${selectedCallId}`)
        .then((res) => res.json())
        .then((data) => setCallDetails(data))
        .catch((err) => console.error("Error fetching call details:", err))
        .finally(() => setLoadingDetails(false));
    } else {
      setCallDetails(null);
    }
  }, [selectedCallId]);

  return (
    <div className="min-h-screen bg-background p-4 md:p-8">
      <header className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-primary">Smile Garden Dashboard</h1>
          <p className="text-muted-foreground">Welcome back, {user?.phoneNumber || "Admin"}</p>
        </div>
        <Button variant="outline" onClick={logout}>Sign Out</Button>
      </header>

      {/* Bento Box Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-auto">
        {/* ROI Snapshot (Span 3 cols) */}
        <div className="md:col-span-3">
          <RoiSnapshot />
        </div>

        {/* Advanced Analytics (Span 3 cols) */}
        <div className="md:col-span-3 bg-card rounded-xl border shadow-sm p-6">
          <h2 className="text-lg font-semibold text-primary mb-4">Advanced Analytics</h2>
          <AdvancedStats />
        </div>

        {/* Agent Status (Span 3 cols) */}
        <div className="md:col-span-3 h-32">
          <AgentStatus />
        </div>

        {/* Call Logs (Span 2 cols) */}
        <div className="md:col-span-2 min-h-[400px] bg-card rounded-xl border shadow-sm p-6 flex flex-col">
          <h2 className="text-lg font-semibold text-primary mb-4">Recent Calls</h2>
          <div className="flex-1 overflow-auto">
             <CallLogs onSelectCall={setSelectedCallId} />
          </div>
        </div>

        {/* Booking History (Span 1 col) */}
        <div className="md:col-span-1 min-h-[400px] bg-card rounded-xl border shadow-sm p-6 flex flex-col">
          <h2 className="text-lg font-semibold text-primary mb-4">Booking History</h2>
          <div className="flex-1 overflow-hidden">
             <BookingHistory />
          </div>
        </div>
      </div>

      <Dialog open={!!selectedCallId} onOpenChange={(open) => !open && setSelectedCallId(null)}>
        <DialogContent className="max-w-2xl max-h-[80vh] flex flex-col">
          <DialogHeader>
            <DialogTitle>Call Details</DialogTitle>
            <DialogDescription>
              Transcript and AI Sentiment Analysis
            </DialogDescription>
          </DialogHeader>

          <div className="flex-1 overflow-hidden flex flex-col gap-4 mt-4">
            {loadingDetails ? (
              <div className="flex-1 flex items-center justify-center text-muted-foreground">Loading...</div>
            ) : callDetails ? (
              <>
                <div className="flex items-center gap-2">
                  <span className="font-semibold">Sentiment:</span>
                  <Badge variant={callDetails.sentiment === 'Anxious' ? 'destructive' : 'secondary'}>
                    {callDetails.sentiment}
                  </Badge>
                </div>
                <div>
                    <h4 className="font-semibold text-sm mb-1">Summary</h4>
                    <p className="text-sm text-muted-foreground bg-muted p-3 rounded-md">{callDetails.summary}</p>
                </div>
                <div className="flex-1 overflow-hidden flex flex-col min-h-0">
                    <h4 className="font-semibold text-sm mb-1">Transcript</h4>
                    <ScrollArea className="flex-1 border rounded-md p-4 bg-background">
                        <pre className="text-sm whitespace-pre-wrap font-sans">{callDetails.transcript}</pre>
                    </ScrollArea>
                </div>
              </>
            ) : (
                <div className="text-center text-muted-foreground">No details found.</div>
            )}
          </div>
        </DialogContent>
      </Dialog>
    </div>
  );
}
