import React, { useState } from "react";
import { courseData, tracks, type CourseTopic } from "../data/courses";

interface CurriculumProps {
  onSelectTopic: (topicId: string, actionTab: string) => void;
}

export const Curriculum: React.FC<CurriculumProps> = ({ onSelectTopic }) => {
  const [selectedTopic, setSelectedTopic] = useState<CourseTopic>(courseData[0]);

  return (
    <div style={{ padding: "2rem", display: "grid", gridTemplateColumns: "350px 1fr", gap: "2rem", minHeight: "calc(100vh - 80px)" }}>
      {/* Sidebar List of Tracks */}
      <div className="glass-panel" style={{ padding: "1.5rem", overflowY: "auto", maxHeight: "80vh", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
        <h3 className="gradient-text" style={{ fontSize: "1.2rem", fontWeight: 700 }}>Python Curriculum</h3>

        {tracks.map((track) => {
          const trackTopics = courseData.filter((t) => t.track === track.id);
          return (
            <div key={track.id} style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
              <h4 style={{ fontSize: "0.9rem", color: "var(--text-secondary)", borderBottom: "1px solid var(--border-glass)", paddingBottom: "0.2rem" }}>
                {track.title}
              </h4>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.25rem" }}>
                {trackTopics.map((topic) => {
                  const isSelected = selectedTopic.id === topic.id;
                  return (
                    <button
                      key={topic.id}
                      onClick={() => setSelectedTopic(topic)}
                      style={{
                        textAlign: "left",
                        padding: "0.5rem 0.8rem",
                        background: isSelected ? "rgba(0, 242, 254, 0.08)" : "transparent",
                        border: "none",
                        borderRadius: "6px",
                        color: isSelected ? "var(--accent-cyan)" : "var(--text-primary)",
                        fontFamily: "var(--font-sans)",
                        fontSize: "0.9rem",
                        cursor: "pointer",
                        transition: "var(--transition-smooth)",
                      }}
                    >
                      {topic.title}
                    </button>
                  );
                })}
                {trackTopics.length === 0 && (
                  <span style={{ fontSize: "0.85rem", color: "var(--text-muted)", paddingLeft: "0.8rem" }}>Coming soon...</span>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {/* Main Details Panel */}
      <div className="glass-panel" style={{ padding: "2rem", overflowY: "auto", display: "flex", flexDirection: "column", gap: "2rem" }}>
        <div>
          <h2 style={{ fontSize: "2rem", marginBottom: "0.5rem" }} className="gradient-text">
            {selectedTopic.title}
          </h2>
          <p style={{ color: "var(--text-secondary)", lineHeight: "1.6", fontSize: "1.1rem" }}>
            {selectedTopic.description}
          </p>
        </div>

        {/* Internals Detail (Memory/CPU/RAM details) */}
        <div style={{ padding: "1.2rem", background: "rgba(178, 36, 239, 0.05)", borderLeft: "4px solid var(--accent-purple)", borderRadius: "6px" }}>
          <h3 style={{ fontSize: "1rem", color: "var(--accent-purple)", marginBottom: "0.5rem", display: "flex", alignItems: "center", gap: "0.3rem" }}>
            ⚙️ Under the Hood (Memory & CPU)
          </h3>
          <p style={{ color: "var(--text-secondary)", fontSize: "0.95rem", lineHeight: "1.5" }}>
            {selectedTopic.internals}
          </p>
        </div>

        {/* Source Code Reference */}
        <div>
          <h3 style={{ fontSize: "1.1rem", marginBottom: "0.5rem", color: "var(--accent-blue)" }}>
            🐍 Python Source File Reference
          </h3>
          <pre style={{ position: "relative" }}>
            <code className="language-python">{selectedTopic.sourceCode}</code>
            <span style={{ position: "absolute", right: "1rem", top: "0.5rem", fontSize: "0.75rem", color: "var(--text-muted)" }}>
              code_pathshala/{selectedTopic.track === "track1" ? "basics" : selectedTopic.track === "track2" ? "basics" : selectedTopic.track === "track3" ? "advanced" : "internals"}/{selectedTopic.id}.py
            </span>
          </pre>
        </div>

        {/* Interactive Action Shortcuts */}
        <div style={{ display: "flex", gap: "1rem", marginTop: "1rem" }}>
          <button className="btn" onClick={() => onSelectTopic(selectedTopic.id, "memory")}>
            💾 Visualize Memory Layout
          </button>
          <button className="btn btn-secondary" onClick={() => onSelectTopic(selectedTopic.id, "bytecode")}>
            ⚙️ Step Through Bytecode
          </button>
          <button className="btn btn-secondary" onClick={() => onSelectTopic(selectedTopic.id, "playground")} style={{ border: "1px solid var(--accent-green)", color: "var(--accent-green)" }}>
            🎯 Solve Real-Time Challenge
          </button>
        </div>
      </div>
    </div>
  );
};
