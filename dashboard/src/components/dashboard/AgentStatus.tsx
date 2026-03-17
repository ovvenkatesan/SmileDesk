import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export function AgentStatus() {
  return (
    <Card className="h-full border-none shadow-none flex flex-col justify-center">
      <CardHeader className="pb-2">
        <CardTitle className="text-xl">Status</CardTitle>
      </CardHeader>
      <CardContent>
        <div className="flex items-center gap-3">
          <div className="w-4 h-4 rounded-full bg-green-500 animate-pulse"></div>
          <span className="text-lg font-medium text-foreground">Online & Ready</span>
        </div>
        <p className="text-xs text-muted-foreground mt-4">Last active: Just now</p>
      </CardContent>
    </Card>
  );
}