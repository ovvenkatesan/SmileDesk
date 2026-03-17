import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";

export function RoiSnapshot() {
  return (
    <Card className="h-full border-none shadow-none flex flex-col justify-center">
      <CardHeader className="pb-2">
        <CardTitle className="text-4xl font-bold text-primary">$8,400</CardTitle>
        <CardDescription className="text-lg">Estimated Value Generated (Last 30 Days)</CardDescription>
      </CardHeader>
      <CardContent>
        <p className="text-sm text-muted-foreground">
          Based on <strong>42</strong> after-hours leads saved and converted by the AI concierge.
        </p>
      </CardContent>
    </Card>
  );
}