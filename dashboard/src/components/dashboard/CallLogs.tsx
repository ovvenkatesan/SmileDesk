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

export function CallLogs() {
  // Mock data for UI layout phase
  const calls = [
    { id: 1, date: "2026-03-17 14:30", number: "+123****890", duration: "2m 25s", outcome: "Booked" },
    { id: 2, date: "2026-03-17 11:15", number: "+198****321", duration: "1m 05s", outcome: "Questions" },
    { id: 3, date: "2026-03-16 19:45", number: "+155****678", duration: "3m 10s", outcome: "Rescheduled" },
  ];

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
            <TableRow key={call.id} className="cursor-pointer hover:bg-muted/50">
              <TableCell className="font-medium">{call.date}</TableCell>
              <TableCell>{call.number}</TableCell>
              <TableCell>{call.duration}</TableCell>
              <TableCell className="text-right">
                <Badge variant={call.outcome === "Booked" ? "default" : "secondary"}>
                  {call.outcome}
                </Badge>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}