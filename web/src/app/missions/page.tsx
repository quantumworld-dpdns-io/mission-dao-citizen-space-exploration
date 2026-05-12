export default function MissionsPage() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold mb-8">Missions</h1>
      <div className="grid gap-6 md:grid-cols-2">
        {missions.map((m) => (
          <div key={m.id} className="p-6 rounded-xl bg-gray-900 border border-gray-800">
            <div className="flex justify-between items-start mb-3">
              <h2 className="text-xl font-semibold">{m.name}</h2>
              <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                m.status === "active" ? "bg-green-900 text-green-300" : "bg-yellow-900 text-yellow-300"
              }`}>{m.status}</span>
            </div>
            <p className="text-gray-400 text-sm mb-4">{m.description}</p>
            <div className="flex justify-between text-sm text-gray-500">
              <span>Orbit: {m.orbit}</span>
              <span>{m.funding}% funded</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

const missions = [
  { id: "1", name: "Athena-1", status: "active", description: "Earth observation CubeSat for atmospheric monitoring", orbit: "LEO 550km", funding: 85 },
  { id: "2", name: "Pioneer-1", status: "funding", description: "Technology demonstrator for new propulsion system", orbit: "LEO 400km", funding: 45 },
];
