export default function DAOPage() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold mb-8">DAO Dashboard</h1>
      <div className="grid md:grid-cols-3 gap-6 mb-10">
        {stats.map((s) => (
          <div key={s.label} className="p-6 rounded-xl bg-gray-900 border border-gray-800 text-center">
            <div className="text-3xl font-bold text-cosmic-400">{s.value}</div>
            <div className="text-gray-400 mt-1">{s.label}</div>
          </div>
        ))}
      </div>
      <div className="p-6 rounded-xl bg-gray-900 border border-gray-800">
        <h2 className="text-xl font-semibold mb-4">Treasury</h2>
        <div className="text-4xl font-bold text-green-400">245.5 ETH</div>
        <p className="text-gray-400 text-sm mt-1">~$820,000 USD</p>
      </div>
    </div>
  );
}

const stats = [
  { label: "Total Missions", value: "12" },
  { label: "Active Proposals", value: "3" },
  { label: "Community Members", value: "1,247" },
];
