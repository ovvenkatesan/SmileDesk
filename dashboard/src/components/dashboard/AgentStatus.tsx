"use client";

import { useEffect, useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Activity } from "lucide-react";

export function AgentStatus() {
  const [status, setStatus] = useState<{ status: string; last_active: string } | null>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/agent-status`)
      .then((res) => res.json())
      .then((data) => setStatus(data))
      .catch((err) => console.error("Error fetching Agent Status:", err));
  }, []);

  if (!status) return <div className="p-6 text-sm text-muted-foreground animate-pulse">Loading status...</div>;

  return (
    <Card className="h-full bg-slate-50/50 border-slate-100 flex flex-row items-center p-6 gap-6">
      <div className="flex flex-col">
        <span className="text-xs font-medium text-slate-500 uppercase tracking-wider mb-1">AI Agent Status</span>
        <div className="flex items-center gap-2">
          <div className={`w-3 h-3 rounded-full ${status.status === 'online' ? 'bg-green-500 animate-pulse' : 'bg-red-500'}`}></div>
          <span className="text-2xl font-bold text-slate-900 capitalize">{status.status.replace("_", " ")}</span>
        </div>
      </div>
      
      <div className="h-10 w-[1px] bg-slate-200 hidden sm:block mx-2"></div>

      <div className="flex flex-col">
        <span className="text-xs font-medium text-slate-500 uppercase tracking-wider mb-1 text-nowrap">Health Check</span>
        <div className="flex items-center gap-2 text-emerald-600">
          <Activity className="h-4 w-4" />
          <span className="text-sm font-semibold">Systems Nominal</span>
        </div>
      </div>

      <div className="flex-1"></div>

      <div className="text-right flex flex-col justify-center">
        <span className="text-xs font-medium text-slate-400">Last Sync</span>
        <span className="text-sm font-medium text-slate-600">
          {new Date(status.last_active).toLocaleString('en-IN', { 
            timeZone: 'Asia/Kolkata',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit',
            hour12: true 
          })}
        </span>
      </div>
    </Card>
  );
}
