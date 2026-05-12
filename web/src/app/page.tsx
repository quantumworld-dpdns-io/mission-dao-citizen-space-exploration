import Link from "next/link";

export default function Home() {
  return (
    <div className="max-w-6xl mx-auto px-4 py-16">
      <section className="text-center mb-20">
        <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-cosmic-400 to-blue-300 bg-clip-text text-transparent">
          Mission DAO
        </h1>
        <p className="text-xl text-gray-400 max-w-2xl mx-auto">
          A platform for communities to fund, govern, and verify CubeSat missions
          with zero-knowledge proofs and decentralized governance.
        </p>
        <div className="flex gap-4 justify-center mt-8">
          <Link href="/missions" className="px-6 py-3 bg-cosmic-600 rounded-lg font-medium hover:bg-cosmic-700 transition">
            Explore Missions
          </Link>
          <Link href="/dao" className="px-6 py-3 border border-gray-700 rounded-lg font-medium hover:bg-gray-800 transition">
            DAO Dashboard
          </Link>
        </div>
      </section>

      <div className="grid md:grid-cols-3 gap-8 mb-20">
        {features.map((f) => (
          <div key={f.title} className="p-6 rounded-xl bg-gray-900 border border-gray-800">
            <div className="text-3xl mb-4">{f.icon}</div>
            <h3 className="text-lg font-semibold mb-2">{f.title}</h3>
            <p className="text-gray-400 text-sm">{f.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

const features = [
  {
    icon: "🛰️",
    title: "CubeSat Missions",
    description: "Propose and fund satellite missions with transparent on-chain governance.",
  },
  {
    icon: "🔐",
    title: "Verifiable Data",
    description: "All mission telemetry published with zero-knowledge proofs for integrity verification.",
  },
  {
    icon: "🏛️",
    title: "DAO Governance",
    description: "Community-driven decision making through proposal voting and agent-assisted workflows.",
  },
];
