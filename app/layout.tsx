import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Universal Converter — American to Metric & Universal",
  description: "Convert between American, Imperial, and Universal units. Length, temperature, weight, volume, data, area, speed, time, pressure, energy, light, power, and angle.",
};
export const viewport = {
  width: "device-width",
  initialScale: 1,
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  );
}
