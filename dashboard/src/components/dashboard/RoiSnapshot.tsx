"use client";

import { useEffect, useState } from "react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export function RoiSnapshot() {
  const [data, setData] = useState<{ leads_saved: number; estimated_value: number; period: string } | null>(null);

  useEffect(() => {
    fetch("http://localhost:8000/api/dashboard/roi")
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Error fetching ROI:", err));
  }, []);

  if (!data) return <div className="p-6 text-sm text-muted-foreground animate-pulse">Loading ROI...</div>;

  return (
    <Card className="h-full border-none shadow-none flex flex-col justify-center">
      <CardHeader className="pb-2">
        <CardTitle className="text-4xl font-bold text-primary">${data.estimated_value.toLocaleString()}</CardTitle>
        <CardDescription className="text-lg">Estimated Value Generated ({data.period})</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground">
          Based on <strong>{data.leads_saved}</strong> after-hours leads saved and converted by the AI concierge.
        </p>
      </CardContent>
    </Card>
  );
}