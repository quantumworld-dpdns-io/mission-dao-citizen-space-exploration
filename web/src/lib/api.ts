const API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

export async function apiFetch<T>(path: string, options?: RequestInit): Promise<T> {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { "Content-Type": "application/json", ...options?.headers },
    ...options,
  });
  if (!res.ok) throw new Error(`API error: ${res.status}`);
  return res.json();
}

export const api = {
  missions: {
    list: () => apiFetch<any[]>("/api/missions"),
    get: (id: string) => apiFetch<any>(`/api/missions/${id}`),
  },
  proposals: {
    list: () => apiFetch<any[]>("/api/proposals"),
    submit: (data: any) => apiFetch<any>("/api/proposals", { method: "POST", body: JSON.stringify(data) }),
  },
  telemetry: {
    query: (satelliteId: string) => apiFetch<any>(`/api/telemetry/${satelliteId}`),
  },
};
