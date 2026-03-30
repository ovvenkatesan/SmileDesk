"use client";

import { useEffect, useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { PieChart, Pie, Cell, ResponsiveContainer, Tooltip, Legend } from "recharts";
import { Moon, Users, XCircle, Clock } from "lucide-react";

export function AdvancedStats() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/api/dashboard/advanced-stats`)
      .then((res) => res.json())
      .then((data) => setData(data))
      .catch((err) => console.error("Error fetching Advanced Stats:", err));
  }, []);

  if (!data) return <div className="p-6 text-sm text-muted-foreground animate-pulse">Loading Advanced Analytics...</div>;

  const chartData = Object.entries(data.language_breakdown).map(([name, value]) => ({
    name,
    value,
  }));

  const COLORS = ["#0088FE", "#00C49F", "#FFBB28", "#FF8042", "#8884d8"];

  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-4 w-full">
      {/* KPI Cards */}
      <div className="md:col-span-1 space-y-4">
        <Card className="bg-orange-50/50 border-orange-100">
          <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-xs font-medium text-orange-800">After Hours</CardTitle>
            <Moon className="h-3 w-3 text-orange-600" />
          </CardHeader>
          <CardContent>
            <div className="text-xl font-bold text-orange-900">{data.after_hours_calls}</div>
            <p className="text-[10px] text-orange-600/80 mt-0.5">Calls outside 9-6</p>
          </CardContent>
        </Card>

        <Card className="bg-blue-50/50 border-blue-100">
          <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-xs font-medium text-blue-800">New Patients</CardTitle>
            <Users className="h-3 w-3 text-blue-600" />
          </CardHeader>
          <CardContent>
            <div className="text-xl font-bold text-blue-900">{data.new_patients}</div>
            <p className="text-[10px] text-blue-600/80 mt-0.5">This month</p>
          </CardContent>
        </Card>
      </div>

      <div className="md:col-span-1 space-y-4">
        <Card className="bg-red-50/50 border-red-100">
          <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-xs font-medium text-red-800">No-Shows</CardTitle>
            <XCircle className="h-3 w-3 text-red-600" />
          </CardHeader>
          <CardContent>
            <div className="text-xl font-bold text-red-900">{data.no_shows}</div>
            <p className="text-[10px] text-red-600/80 mt-0.5">Total missed</p>
          </CardContent>
        </Card>

        <Card className="bg-indigo-50/50 border-indigo-100">
          <CardHeader className="pb-2 flex flex-row items-center justify-between space-y-0">
            <CardTitle className="text-xs font-medium text-indigo-800">Efficiency</CardTitle>
            <Clock className="h-3 w-3 text-indigo-600" />
          </CardHeader>
          <CardContent>
            <div className="text-xl font-bold text-indigo-900">{data.scheduling_efficiency}%</div>
            <p className="text-[10px] text-indigo-600/80 mt-0.5">Time utilization</p>
          </CardContent>
        </Card>
      </div>

      {/* Language Chart */}
      <Card className="md:col-span-2 flex flex-col h-full bg-slate-50/50 border-slate-100">
        <CardHeader className="pb-2">
          <CardTitle className="text-xs font-medium text-slate-800">Language Distribution</CardTitle>
        </CardHeader>
        <CardContent className="flex-1 pb-0">
          <div className="h-[120px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={chartData}
                  cx="50%"
                  cy="50%"
                  innerRadius={30}
                  outerRadius={50}
                  paddingAngle={5}
                  dataKey="value"
                >
                  {chartData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend layout="vertical" align="right" verticalAlign="middle" iconSize={8} wrapperStyle={{fontSize: '10px'}} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
