import React, { useState } from "react";

interface BytecodeInstruction {
  opName: string;
  arg: string;
  highlight?: boolean;
}

interface BytecodeStep {
  instructionIndex: number;
  explanation: string;
  evalStack: string[];
  locals: { name: string; value: string }[];
}

interface BytecodeScenario {
  title: string;
  code: string[];
  instructions: BytecodeInstruction[];
  steps: BytecodeStep[];
}

const bytecodeScenarios: BytecodeScenario[] = [
  {
    title: "1. Constant Addition (x = 5 + 3)",
    code: ["x = 5 + 3"],
    instructions: [
      { opName: "LOAD_CONST", arg: "5 (value: 5)" },
      { opName: "LOAD_CONST", arg: "6 (value: 3)" },
      { opName: "BINARY_ADD", arg: "" },
      { opName: "STORE_NAME", arg: "0 (x)" },
    ],
    steps: [
      {
        instructionIndex: 0,
        explanation: "The Python compiler compiles code to bytecode. The VM begins by preparing to load the first constant value 5.",
        evalStack: [],
        locals: [],
      },
      {
        instructionIndex: 1,
        explanation: "LOAD_CONST 5: Pushes the integer constant 5 onto CPython's evaluation stack.",
        evalStack: ["5"],
        locals: [],
      },
      {
        instructionIndex: 2,
        explanation: "LOAD_CONST 3: Pushes the integer constant 3 onto the top of the evaluation stack.",
        evalStack: ["5", "3"],
        locals: [],
      },
      {
        instructionIndex: 3,
        explanation: "BINARY_ADD: Pops the top two values (5 and 3), executes the addition, and pushes the result (8) back onto the stack.",
        evalStack: ["8"],
        locals: [],
      },
      {
        instructionIndex: 3, // Keep pointer on last store or end state
        explanation: "STORE_NAME x: Pops the value 8 from the top of the stack and binds it to key 'x' in the namespace dict.",
        evalStack: [],
        locals: [{ name: "x", value: "8" }],
      },
    ],
  },
  {
    title: "2. Conditional Branching (if x > 0)",
    code: [
      "if x > 0:",
      "    y = 10",
    ],
    instructions: [
      { opName: "LOAD_NAME", arg: "0 (x)" },
      { opName: "LOAD_CONST", arg: "1 (0)" },
      { opName: "COMPARE_OP", arg: "4 (>)" },
      { opName: "POP_JUMP_IF_FALSE", arg: "target: offset 12" },
      { opName: "LOAD_CONST", arg: "2 (10)" },
      { opName: "STORE_NAME", arg: "1 (y)" },
    ],
    steps: [
      {
        instructionIndex: 0,
        explanation: "CPython loads variable 'x' from the namespace to evaluate the conditional expression.",
        evalStack: [],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 1,
        explanation: "LOAD_NAME x: Pushes value of 'x' (which is 5) onto the evaluation stack.",
        evalStack: ["5"],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 2,
        explanation: "LOAD_CONST 0: Pushes constant value 0 onto the stack.",
        evalStack: ["5", "0"],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 3,
        explanation: "COMPARE_OP (>): Pops 5 and 0, evaluates 5 > 0, and pushes boolean result True onto the stack.",
        evalStack: ["True"],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 4,
        explanation: "POP_JUMP_IF_FALSE: Pops True from stack. Since it is True, it does NOT jump; execution continues to the next instruction.",
        evalStack: [],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 5,
        explanation: "LOAD_CONST 10: Pushes constant integer 10 onto evaluation stack.",
        evalStack: ["10"],
        locals: [{ name: "x", value: "5" }],
      },
      {
        instructionIndex: 5,
        explanation: "STORE_NAME y: Pops 10 from stack and binds it to 'y' in the local namespace.",
        evalStack: [],
        locals: [
          { name: "x", value: "5" },
          { name: "y", value: "10" },
        ],
      },
    ],
  },
];

export const BytecodeVisualizer: React.FC = () => {
  const [scenarioIndex, setScenarioIndex] = useState(0);
  const [stepIndex, setStepIndex] = useState(0);

  const scenario = bytecodeScenarios[scenarioIndex];
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
    setScenarioIndex(Number(e.target.value));
    setStepIndex(0);
  };

  return (
    <div style={{ padding: "2rem", display: "flex", flexDirection: "column", gap: "2rem", minHeight: "calc(100vh - 80px)" }}>
      {/* Header Panel */}
      <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <div>
          <h2 className="gradient-text" style={{ fontSize: "1.8rem" }}>CPython Bytecode Visualizer</h2>
          <p style={{ color: "var(--text-secondary)", fontSize: "0.95rem" }}>See how Python compiles code into bytecode instructions and executes them on an evaluation stack.</p>
        </div>
        <select
          value={scenarioIndex}
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
          {bytecodeScenarios.map((s, idx) => (
            <option key={idx} value={idx}>
              {s.title}
            </option>
          ))}
        </select>
      </div>

      {/* Main Grid */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem" }}>
        {/* Left Column: Bytecode list */}
        <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
          <h3 style={{ fontSize: "1.2rem", color: "var(--accent-blue)" }}>Compiled Bytecode Instructions</h3>

          <div style={{ display: "flex", flexDirection: "column", gap: "0.4rem" }}>
            {scenario.instructions.map((inst, idx) => {
              const isCurrent = step.instructionIndex === idx;
              return (
                <div
                  key={idx}
                  style={{
                    display: "flex",
                    justifyContent: "space-between",
                    padding: "0.6rem 1rem",
                    borderRadius: "6px",
                    background: isCurrent ? "rgba(0, 242, 254, 0.12)" : "rgba(255,255,255,0.02)",
                    borderLeft: isCurrent ? "4px solid var(--accent-cyan)" : "4px solid transparent",
                    fontFamily: "var(--font-mono)",
                    fontSize: "0.92rem",
                  }}
                >
                  <span style={{ color: isCurrent ? "var(--accent-cyan)" : "var(--text-primary)" }}>
                    {inst.opName}
                  </span>
                  <span style={{ color: "var(--text-muted)" }}>{inst.arg}</span>
                </div>
              );
            })}
          </div>

          <div style={{ padding: "1rem", background: "rgba(0, 242, 254, 0.04)", borderRadius: "8px", borderLeft: "2px solid var(--accent-cyan)" }}>
            <h4 style={{ fontSize: "0.9rem", color: "var(--accent-cyan)", marginBottom: "0.25rem" }}>Evaluation Status</h4>
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

        {/* Right Column: Virtual Machine Stack and Locals */}
        <div style={{ display: "flex", flexDirection: "column", gap: "2rem" }}>
          {/* Evaluation Stack */}
          <div className="glass-panel" style={{ padding: "1.5rem", flex: 1 }}>
            <h3 style={{ fontSize: "1.2rem", marginBottom: "1rem", color: "var(--accent-purple)", borderBottom: "1px solid var(--border-glass)", paddingBottom: "0.5rem" }}>
              CPython Evaluation Stack
            </h3>
            <div style={{ display: "flex", flexDirection: "column-reverse", gap: "0.5rem", minHeight: "150px", justifyContent: "flex-end", alignItems: "center", padding: "1rem", background: "rgba(0,0,0,0.2)", borderRadius: "8px" }}>
              {step.evalStack.length === 0 ? (
                <span style={{ color: "var(--text-muted)", fontStyle: "italic", alignSelf: "center", margin: "auto" }}>Stack is empty</span>
              ) : (
                step.evalStack.map((val, idx) => (
                  <div
                    key={idx}
                    className="pulse-highlight"
                    style={{
                      width: "80%",
                      padding: "0.8rem",
                      background: "rgba(178, 36, 239, 0.15)",
                      border: "1px solid var(--accent-purple)",
                      borderRadius: "6px",
                      textAlign: "center",
                      fontFamily: "var(--font-mono)",
                      fontSize: "1.1rem",
                      color: "var(--text-primary)",
                    }}
                  >
                    {val}
                  </div>
                ))
              )}
            </div>
          </div>

          {/* Locals / Namespace */}
          <div className="glass-panel" style={{ padding: "1.5rem", height: "fit-content" }}>
            <h3 style={{ fontSize: "1.2rem", marginBottom: "1rem", color: "var(--accent-green)", borderBottom: "1px solid var(--border-glass)", paddingBottom: "0.5rem" }}>
              Namespace dict (Locals)
            </h3>
            {step.locals.length === 0 ? (
              <div style={{ color: "var(--text-muted)", fontStyle: "italic", fontSize: "0.9rem" }}>No variables bound in namespace.</div>
            ) : (
              <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap" }}>
                {step.locals.map((variable) => (
                  <div
                    key={variable.name}
                    style={{
                      padding: "0.6rem 1rem",
                      background: "rgba(0, 255, 135, 0.05)",
                      border: "1px solid var(--border-glass)",
                      borderRadius: "6px",
                      display: "flex",
                      gap: "0.5rem",
                      fontFamily: "var(--font-mono)",
                    }}
                  >
                    <span style={{ color: "var(--accent-green)", fontWeight: 600 }}>{variable.name}</span>
                    <span style={{ color: "var(--text-muted)" }}>:</span>
                    <span style={{ color: "var(--text-primary)" }}>{variable.value}</span>
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
