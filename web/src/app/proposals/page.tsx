export default function ProposalsPage() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-12">
      <h1 className="text-3xl font-bold mb-8">Governance Proposals</h1>
      <div className="space-y-4">
        {proposals.map((p) => (
          <div key={p.id} className="p-5 rounded-lg bg-gray-900 border border-gray-800">
            <div className="flex justify-between items-start">
              <div>
                <h3 className="font-semibold text-lg">{p.title}</h3>
                <p className="text-gray-400 text-sm mt-1">{p.description}</p>
              </div>
              <span className={`px-3 py-1 rounded-full text-xs font-medium ${
                p.status === "voting" ? "bg-blue-900 text-blue-300" :
                p.status === "passed" ? "bg-green-900 text-green-300" : "bg-gray-800 text-gray-400"
              }`}>{p.status}</span>
            </div>
            <div className="flex gap-4 mt-3 text-sm text-gray-500">
              <span>For: {p.votesFor}</span>
              <span>Against: {p.votesAgainst}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

const proposals = [
  { id: "1", title: "Fund Athena-1 Launch", description: "Allocate 50 ETH from treasury for Athena-1 CubeSat launch costs", status: "voting", votesFor: 120, votesAgainst: 30 },
  { id: "2", title: "Add New Sensor Package", description: "Upgrade Pioneer-1 payload with multispectral imaging sensor", status: "passed", votesFor: 200, votesAgainst: 15 },
];
