import React, { useState } from "react";

interface MemoryStep {
  codeLine: string;
  explanation: string;
  stack: { name: string; target: string }[];
  heap: { address: string; type: string; value: string; refCount: number; highlight?: boolean }[];
}

interface Scenario {
  title: string;
  code: string[];
  steps: MemoryStep[];
}

const scenarios: Scenario[] = [
  {
    title: "1. Variable Aliasing & Reference Assignment",
    code: [
      "original = [1, 2, 3]",
      "alias = original",
      "alias.append(4)",
    ],
    steps: [
      {
        codeLine: "original = [1, 2, 3]",
        explanation: "Python allocates a list object '[1, 2, 3]' in the heap. The stack variable 'original' points to its address (0x7fa1) with refcount = 1.",
        stack: [{ name: "original", target: "0x7fa1" }],
        heap: [{ address: "0x7fa1", type: "list", value: "[1, 2, 3]", refCount: 1, highlight: true }],
      },
      {
        codeLine: "alias = original",
        explanation: "Python copies the reference pointer, not the data. The new variable 'alias' now points to the exact same heap address (0x7fa1). Refcount increases to 2.",
        stack: [
          { name: "original", target: "0x7fa1" },
          { name: "alias", target: "0x7fa1" },
        ],
        heap: [{ address: "0x7fa1", type: "list", value: "[1, 2, 3]", refCount: 2 }],
      },
      {
        codeLine: "alias.append(4)",
        explanation: "Modifying the list via 'alias' changes the underlying list object. Because 'original' points to the same object, it also reflects the update.",
        stack: [
          { name: "original", target: "0x7fa1" },
          { name: "alias", target: "0x7fa1" },
        ],
        heap: [{ address: "0x7fa1", type: "list", value: "[1, 2, 3, 4]", refCount: 2, highlight: true }],
      },
    ],
  },
  {
    title: "2. Reference Counting & Scope Deallocation",
    code: [
      "a = ['data']",
      "b = a",
      "del a",
      "del b",
    ],
    steps: [
      {
        codeLine: "a = ['data']",
        explanation: "A list object is created at 0x810c. Variable 'a' on the stack holds the reference. Refcount is 1.",
        stack: [{ name: "a", target: "0x810c" }],
        heap: [{ address: "0x810c", type: "list", value: "['data']", refCount: 1, highlight: true }],
      },
      {
        codeLine: "b = a",
        explanation: "Variable 'b' is assigned reference pointer of 'a'. Both variables point to 0x810c. Refcount is 2.",
        stack: [
          { name: "a", target: "0x810c" },
          { name: "b", target: "0x810c" },
        ],
        heap: [{ address: "0x810c", type: "list", value: "['data']", refCount: 2 }],
      },
      {
        codeLine: "del a",
        explanation: "'del a' removes the local variable 'a' from the stack. The reference count of 0x810c decreases to 1. The object remains alive.",
        stack: [{ name: "b", target: "0x810c" }],
        heap: [{ address: "0x810c", type: "list", value: "['data']", refCount: 1, highlight: true }],
      },
      {
        codeLine: "del b",
        explanation: "'del b' removes the final pointer. Reference count reaches 0. Python immediately garbage collects the object, freeing heap RAM.",
        stack: [],
        heap: [],
      },
    ],
  },
  {
    title: "3. Shallow Copy vs Deep Copy in Memory",
    code: [
      "x = [[1]]",
      "y = x.copy() # Shallow",
      "y[0].append(2)",
    ],
    steps: [
      {
        codeLine: "x = [[1]]",
        explanation: "Creates an outer list at 0x90a1 containing a reference to an inner list object at 0x90a2.",
        stack: [{ name: "x", target: "0x90a1" }],
        heap: [
          { address: "0x90a1", type: "list (outer)", value: "[0x90a2]", refCount: 1 },
          { address: "0x90a2", type: "list (inner)", value: "[1]", refCount: 1 },
        ],
      },
      {
        codeLine: "y = x.copy() # Shallow",
        explanation: "Shallow copy creates a NEW outer list (0x90b1) pointing to 'y', but copies the inner address (0x90a2) directly. Refcount of inner list rises to 2.",
        stack: [
          { name: "x", target: "0x90a1" },
          { name: "y", target: "0x90b1" },
        ],
        heap: [
          { address: "0x90a1", type: "list (outer)", value: "[0x90a2]", refCount: 1 },
          { address: "0x90b1", type: "list (outer)", value: "[0x90a2]", refCount: 1, highlight: true },
          { address: "0x90a2", type: "list (inner)", value: "[1]", refCount: 2 },
        ],
      },
      {
        codeLine: "y[0].append(2)",
        explanation: "Appending 2 to 'y[0]' targets the shared inner list at 0x90a2. Both 'x' and 'y' reflect the modification because they share the inner reference pointer.",
        stack: [
          { name: "x", target: "0x90a1" },
          { name: "y", target: "0x90b1" },
        ],
        heap: [
          { address: "0x90a1", type: "list (outer)", value: "[0x90a2]", refCount: 1 },
          { address: "0x90b1", type: "list (outer)", value: "[0x90a2]", refCount: 1 },
          { address: "0x90a2", type: "list (inner)", value: "[1, 2]", refCount: 2, highlight: true },
        ],
      },
    ],
  },
];

export const MemoryVisualizer: React.FC = () => {
  const [selectedScenarioIndex, setSelectedScenarioIndex] = useState(0);
  const [stepIndex, setStepIndex] = useState(0);

  const scenario = scenarios[selectedScenarioIndex];
  const step = scenario.steps[stepIndex];

  const handleNext = () => {
    if (stepIndex < scenario.steps.length - 1) {
      setStepIndex(stepIndex + 1);
    }
  };

  const handlePrev = () => {
    if (stepIndex > 0) {
      setStepIndex(stepIndex - 1);
    }
  };

  const handleScenarioChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setSelectedScenarioIndex(Number(e.target.value));
    setStepIndex(0);
  };

  return (
    <div style={{ padding: "2rem", display: "flex", flexDirection: "column", gap: "2rem", minHeight: "calc(100vh - 80px)" }}>
      {/* Header and Selectors */}
      <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <h2 className="gradient-text" style={{ fontSize: "1.8rem" }}>Interactive Memory Visualizer</h2>
          <p style={{ color: "var(--text-secondary)", fontSize: "0.95rem" }}>Step through execution to see stack pointers and heap references in real-time.</p>
        </div>
        <select
          value={selectedScenarioIndex}
          onChange={handleScenarioChange}
          style={{
            background: "var(--bg-dark)",
            color: "var(--accent-cyan)",
            border: "1px solid var(--border-glass)",
            padding: "0.5rem 1rem",
            borderRadius: "8px",
            fontSize: "0.95rem",
            outline: "none",
            cursor: "pointer",
          }}
        >
          {scenarios.map((s, idx) => (
            <option key={idx} value={idx}>
              {s.title}
            </option>
          ))}
        </select>
      </div>

      {/* Main Simulation Area */}
      <div style={{ display: "grid", gridTemplateColumns: "400px 1fr", gap: "2rem" }}>
        {/* Left Column: Code Stepper */}
        <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
          <h3 style={{ fontSize: "1.1rem", color: "var(--accent-blue)" }}>Python Code Trace</h3>
          <div style={{ background: "rgba(0,0,0,0.3)", borderRadius: "8px", padding: "1rem", display: "flex", flexDirection: "column", gap: "0.5rem" }}>
            {scenario.code.map((line, idx) => {
              const isCurrent = step.codeLine === line;
              return (
                <div
                  key={idx}
                  style={{
                    fontFamily: "var(--font-mono)",
                    fontSize: "0.95rem",
                    padding: "0.3rem 0.5rem",
                    borderRadius: "4px",
                    background: isCurrent ? "rgba(0, 242, 254, 0.15)" : "transparent",
                    borderLeft: isCurrent ? "3px solid var(--accent-cyan)" : "3px solid transparent",
                    color: isCurrent ? "var(--text-primary)" : "var(--text-muted)",
                    fontWeight: isCurrent ? "600" : "400",
                  }}
                >
                  {line}
                </div>
              );
            })}
          </div>

          <div style={{ padding: "1rem", background: "rgba(255,255,255,0.03)", borderRadius: "8px", borderLeft: "2px solid var(--accent-cyan)" }}>
            <h4 style={{ fontSize: "0.9rem", color: "var(--accent-cyan)", marginBottom: "0.25rem" }}>Explanation</h4>
            <p style={{ color: "var(--text-secondary)", fontSize: "0.88rem", lineHeight: "1.5" }}>{step.explanation}</p>
          </div>

          {/* Stepper controls */}
          <div style={{ display: "flex", gap: "1rem" }}>
            <button className="btn btn-secondary" onClick={handlePrev} disabled={stepIndex === 0} style={{ flex: 1, opacity: stepIndex === 0 ? 0.4 : 1 }}>
              ◀ Previous
            </button>
            <button className="btn" onClick={handleNext} disabled={stepIndex === scenario.steps.length - 1} style={{ flex: 1, opacity: stepIndex === scenario.steps.length - 1 ? 0.4 : 1 }}>
              Next ▶
            </button>
          </div>
        </div>

        {/* Right Column: Stack & Heap Rendering */}
        <div className="glass-panel" style={{ padding: "2rem", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "3rem", position: "relative" }}>
          {/* Stack Panel */}
          <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            <h3 style={{ fontSize: "1.2rem", borderBottom: "1px solid var(--border-glass)", paddingBottom: "0.5rem", color: "var(--accent-blue)" }}>
              Call Stack (Variables)
            </h3>
            {step.stack.length === 0 ? (
              <div style={{ color: "var(--text-muted)", fontSize: "0.95rem", fontStyle: "italic", padding: "1rem" }}>Namespace is empty.</div>
            ) : (
              <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
                {step.stack.map((v) => (
                  <div
                    key={v.name}
                    style={{
                      display: "flex",
                      justifyContent: "space-between",
                      alignItems: "center",
                      padding: "1rem",
                      background: "rgba(79, 172, 254, 0.08)",
                      border: "1px solid var(--border-glass)",
                      borderRadius: "8px",
                    }}
                  >
                    <div>
                      <span style={{ fontFamily: "var(--font-mono)", fontWeight: 600, color: "var(--text-primary)" }}>{v.name}</span>
                      <span style={{ fontSize: "0.8rem", display: "block", color: "var(--text-muted)" }}>pointer reference</span>
                    </div>
                    <span style={{ fontFamily: "var(--font-mono)", fontSize: "0.9rem", color: "var(--accent-cyan)", background: "rgba(0, 242, 254, 0.15)", padding: "0.2rem 0.6rem", borderRadius: "4px" }}>
                      {v.target}
                    </span>
                  </div>
                ))}
              </div>
            )}
          </div>

          {/* Heap Panel */}
          <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
            <h3 style={{ fontSize: "1.2rem", borderBottom: "1px solid var(--border-glass)", paddingBottom: "0.5rem", color: "var(--accent-purple)" }}>
              Heap Memory (Objects)
            </h3>
            {step.heap.length === 0 ? (
              <div style={{ color: "var(--text-muted)", fontSize: "0.95rem", fontStyle: "italic", padding: "1rem" }}>RAM heap is clean.</div>
            ) : (
              <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
                {step.heap.map((obj) => (
                  <div
                    key={obj.address}
                    className={obj.highlight ? "pulse-highlight" : ""}
                    style={{
                      padding: "1rem",
                      background: "rgba(178, 36, 239, 0.08)",
                      border: "1px solid var(--border-glass)",
                      borderRadius: "8px",
                      transition: "var(--transition-smooth)",
                    }}
                  >
                    <div style={{ display: "flex", justifyContent: "space-between", marginBottom: "0.5rem" }}>
                      <span style={{ fontFamily: "var(--font-mono)", fontSize: "0.85rem", color: "var(--accent-purple)", fontWeight: 600 }}>{obj.address}</span>
                      <span style={{ fontSize: "0.75rem", background: "rgba(255,255,255,0.05)", padding: "0.1rem 0.4rem", borderRadius: "4px", color: "var(--text-secondary)" }}>
                        {obj.type}
                      </span>
                    </div>
                    <div style={{ fontSize: "1.2rem", fontFamily: "var(--font-mono)", color: "var(--text-primary)", marginBottom: "0.5rem" }}>{obj.value}</div>
                    <div style={{ fontSize: "0.8rem", color: "var(--text-muted)", display: "flex", justifyContent: "space-between" }}>
                      <span>Refcount: <strong style={{ color: "var(--accent-green)" }}>{obj.refCount}</strong></span>
                      <span>Heap object details</span>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
