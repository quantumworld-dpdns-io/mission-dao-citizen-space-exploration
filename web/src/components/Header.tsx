import Link from "next/link";

export default function Header() {
  return (
    <header className="border-b border-gray-800 bg-gray-950/80 backdrop-blur-sm sticky top-0 z-50">
      <div className="max-w-6xl mx-auto px-4 h-16 flex items-center justify-between">
        <Link href="/" className="text-xl font-bold bg-gradient-to-r from-cosmic-400 to-blue-300 bg-clip-text text-transparent">
          MissionDAO
        </Link>
        <nav className="flex gap-6 text-sm text-gray-400">
          <Link href="/missions" className="hover:text-white transition">Missions</Link>
          <Link href="/proposals" className="hover:text-white transition">Proposals</Link>
          <Link href="/dao" className="hover:text-white transition">DAO</Link>
        </nav>
      </div>
    </header>
  );
}
