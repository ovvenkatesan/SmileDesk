"use client";

import { useAuth } from "@/lib/AuthContext";
import { Button } from "@/components/ui/button";

export default function DashboardPage() {
  const { user, logout } = useAuth();

  return (
    <div className="p-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold text-primary">Smile Garden Dashboard</h1>
        <Button variant="outline" onClick={logout}>Sign Out</Button>
      </div>
      <p>Welcome, {user?.phoneNumber}. The Bento Box layout will be built here in Phase 4.</p>
    </div>
  );
}