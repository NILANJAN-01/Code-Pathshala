import React from "react";

interface NavigationProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const Navigation: React.FC<NavigationProps> = ({ activeTab, setActiveTab }) => {
  const tabs = [
    { id: "curriculum", label: "📚 Course Curriculum" },
    { id: "memory", label: "💾 RAM/Memory Visualizer" },
    { id: "bytecode", label: "⚙️ CPython Bytecode Visualizer" },
    { id: "playground", label: "🎯 Coding Playground" },
  ];

  return (
    <nav
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        padding: "1rem 2rem",
        borderBottom: "1px solid var(--border-glass)",
        background: "rgba(7, 9, 19, 0.8)",
        backdropFilter: "blur(12px)",
        position: "sticky",
        top: 0,
        zIndex: 100,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
        <span style={{ fontSize: "1.8rem" }}>🐍</span>
        <span
          className="gradient-text"
          style={{
            fontFamily: "Space Grotesk",
            fontSize: "1.4rem",
            fontWeight: 700,
            letterSpacing: "-0.03em",
          }}
        >
          CODE PATHSHALA
        </span>
      </div>

      <div style={{ display: "flex", gap: "1rem" }}>
        {tabs.map((tab) => {
          const isActive = activeTab === tab.id;
          return (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              style={{
                background: isActive
                  ? "linear-gradient(135deg, rgba(0, 242, 254, 0.15), rgba(79, 172, 254, 0.15))"
                  : "transparent",
                border: "1px solid",
                borderColor: isActive ? "var(--accent-cyan)" : "transparent",
                color: isActive ? "var(--accent-cyan)" : "var(--text-secondary)",
                borderRadius: "8px",
                padding: "0.5rem 1rem",
                fontFamily: "var(--font-sans)",
                fontSize: "0.95rem",
                fontWeight: 600,
                cursor: "pointer",
                transition: "var(--transition-smooth)",
              }}
            >
              {tab.label}
            </button>
          );
        })}
      </div>
    </nav>
  );
};
