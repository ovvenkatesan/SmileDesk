"use client";

import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Activity, CalendarCheck, PhoneCall, TrendingUp } from "lucide-react";

export function RoiSnapshot() {
  const [data, setData] = useState<{ leads_saved: number; estimated_value: number; period: string; total_calls: number; conversion_rate: number } | null>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/roi`)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Error fetching ROI:", err));
  }, []);

  if (!data) return <div className="p-6 text-sm text-muted-foreground animate-pulse">Loading KPIs...</div>;

  return (
    <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 h-full">
      <Card className="flex flex-col justify-center bg-blue-50/50 border-blue-100">
        <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
          <CardTitle className="text-sm font-medium text-blue-800">Total Calls</CardTitle>
          <PhoneCall className="h-4 w-4 text-blue-600" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-blue-900">{data.total_calls}</div>
          <p className="text-xs text-blue-600/80 mt-1">Handled by AI</p>
        </CardContent>
      </Card>

      <Card className="flex flex-col justify-center bg-emerald-50/50 border-emerald-100">
        <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
          <CardTitle className="text-sm font-medium text-emerald-800">Appointments Booked</CardTitle>
          <button onClick={() => fetch(process.env.NEXT_PUBLIC_API_URL + "/api/dashboard/sync", {method: "POST"}).then(() => window.location.reload())} className="text-[10px] bg-emerald-100 hover:bg-emerald-200 text-emerald-700 px-2 py-0.5 rounded border border-emerald-300">Sync</button><CalendarCheck className="h-4 w-4 text-emerald-600" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-emerald-900">{data.leads_saved}</div>
          <p className="text-xs text-emerald-600/80 mt-1">Total Bookings</p>
        </CardContent>
      </Card>

      <Card className="flex flex-col justify-center bg-violet-50/50 border-violet-100">
        <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
          <CardTitle className="text-sm font-medium text-violet-800">Conversion Rate</CardTitle>
          <TrendingUp className="h-4 w-4 text-violet-600" />
        </CardHeader>
        <CardContent>
          <div className="text-3xl font-bold text-violet-900">{data.conversion_rate}%</div>
          <p className="text-xs text-violet-600/80 mt-1">Booking success rate</p>
        </CardContent>
      </Card>
    </div>
  );
}

