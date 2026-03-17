"use client";

import { useEffect, useState } from "react";
import {
  Table,
  Body,
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

  useEffect(() => {
    fetch("http://localhost:8000/api/dashboard/calls")
      .then((res) => res.json())
      .then((data) => setCalls(data))
      .catch((err) => console.error("Error fetching Calls:", err));
  }, []);

  if (calls.length === 0) {
    return <div className="p-4 text-sm text-muted-foreground">Loading calls...</div>;
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
            <TableHead className="text-right">Outcome</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {calls.map((call) => (
            <TableRow 
                key={call.id} 
                className="cursor-pointer hover:bg-muted/50"
                onClick={() => onSelectCall && onSelectCall(call.id)}
            >
              <TableCell className="font-medium">{new Date(call.start_time).toLocaleString()}</TableCell>
              <TableCell>{call.caller_number}</TableCell>
              <TableCell>{formatDuration(call.duration_seconds)}</TableCell>
              <TableCell className="text-right">
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