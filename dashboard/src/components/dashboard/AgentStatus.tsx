"use client";

import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export function AgentStatus() {
  const [status, setStatus] = useState<{ status: string; last_active: string } | null>(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/dashboard/agent-status")
      .then((res) => res.json())
      .then((data) => setStatus(data))
      .catch((err) => console.error("Error fetching Agent Status:", err));
  }, []);

  if (!status) return <div className="p-6 text-sm text-muted-foreground animate-pulse">Loading status...</div>;

  return (
    <Card className="h-full border-none shadow-none flex flex-col justify-center">
      <CardHeader className="pb-2">
        <CardTitle className="text-xl">Status</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex items-center gap-3">
          <div className={`w-4 h-4 rounded-full ${status.status === 'online' ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`}></div>
          <span className="text-lg font-medium text-foreground capitalize">{status.status.replace("_", " ")}</span>
        </div>
        <p className="text-xs text-muted-foreground mt-4">Last active: {new Date(status.last_active).toLocaleString()}</p>
      </CardContent>
    </Card>
  );
}