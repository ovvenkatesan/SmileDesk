"use client";

import { useEffect, useState } from "react";
import {
  Table,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
  TableBody
} from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";

interface CallLogsProps {
  onSelectCall?: (callId: string) => void;
}

export function CallLogs({ onSelectCall }: CallLogsProps) {
  const [calls, setCalls] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);

  const fetchCalls = () => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/calls`)
      .then((res) => res.json())
      .then((data) => {
        setCalls(Array.isArray(data) ? data : []);
        setIsLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching Calls:", err);
        setIsLoading(false);
      });
  };

  useEffect(() => {
    fetchCalls();
    
    // Auto-refresh every 10 seconds to catch new calls
    const interval = setInterval(fetchCalls, 10000);
    return () => clearInterval(interval);
  }, []);

  if (isLoading && calls.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground animate-pulse">Loading calls...</div>;
  }

  if (calls.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground">No recent calls found.</div>;
  }

  const formatDuration = (seconds: number) => {
      const m = Math.floor(seconds / 60);
      const s = seconds % 60;
      return `${m}m ${s}s`;
  };

  return (
    <div className="h-full flex flex-col">
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Date & Time</TableHead>
            <TableHead>Caller</TableHead>
            <TableHead>Duration</TableHead>
            <TableHead>Recording</TableHead><TableHead className="text-right">Outcome</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {calls.map((call) => (
            <TableRow 
                key={call.id} 
                className="cursor-pointer hover:bg-muted/50"
                onClick={() => onSelectCall && onSelectCall(call.id)}
            >
              <TableCell className="font-medium">{new Date(call.start_time).toLocaleString('en-IN', { timeZone: 'Asia/Kolkata', dateStyle: 'medium', timeStyle: 'short' })}</TableCell>
              <TableCell>{call.caller_number}</TableCell>
              <TableCell>{formatDuration(call.duration_seconds)}</TableCell>
              <TableCell>{call.audio_url ? <audio src={call.audio_url} controls className="h-8 w-48" onClick={(e) => e.stopPropagation()} /> : <span className="text-xs text-muted-foreground">No audio</span>}</TableCell><TableCell className="text-right">
                <Badge variant={call.outcome === "booked_appointment" ? "default" : "secondary"}>
                  {call.outcome.replace("_", " ")}
                </Badge>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}

