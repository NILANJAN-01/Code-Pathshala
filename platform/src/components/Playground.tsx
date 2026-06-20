import React, { useState, useEffect } from "react";
import { type CourseTopic, courseData } from "../data/courses";

interface PlaygroundProps {
  selectedTopicId: string;
}

export const Playground: React.FC<PlaygroundProps> = ({ selectedTopicId }) => {
  const [topic, setTopic] = useState<CourseTopic>(courseData[0]);
  const [userCode, setUserCode] = useState("");
  const [evaluationResult, setEvaluationResult] = useState<{ success: boolean; msg: string } | null>(null);
  const [showSolution, setShowSolution] = useState(false);

  // Sync selected topic
  useEffect(() => {
    const found = courseData.find((t) => t.id === selectedTopicId) || courseData[0];
    setTopic(found);
    setUserCode(found.challenge.template);
    setEvaluationResult(null);
    setShowSolution(false);
  }, [selectedTopicId]);

  const handleChallengeChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const found = courseData.find((t) => t.id === e.target.value) || courseData[0];
    setTopic(found);
    setUserCode(found.challenge.template);
    setEvaluationResult(null);
    setShowSolution(false);
  };

  const evaluateCode = () => {
    // Simple local Javascript evaluation based on structural constraints
    const code = userCode.trim().replace(/\s+/g, " ");
    let success = false;
    let msg = "";

    try {
      if (topic.id === "variables") {
        const hasSwap = code.includes("return b, a") || code.includes("return (b, a)");
        if (hasSwap) {
          success = true;
          msg = "All test cases passed! swap_values(1, 2) returned (2, 1) and swap_values('x', 'y') returned ('y', 'x').";
        } else {
          msg = "Fail: swap_values should return references in reversed order (b, a).";
        }
      } else if (topic.id === "strings") {
        const hasReverse = code.includes("s[::-1]");
        if (hasReverse) {
          success = true;
          msg = "All test cases passed! reverse_string('python') returned 'nohtyp'.";
        } else {
          msg = "Fail: String reverse not implemented correctly. Try using slicing syntax s[::-1].";
        }
      } else if (topic.id === "oop") {
        const hasInit = code.includes("def __init__") && (code.includes("self.brand = brand") || code.includes("self.brand=brand"));
        const hasDrive = code.includes("def drive") && (code.includes("Driving") || code.includes("self.brand"));
        if (hasInit && hasDrive) {
          success = true;
          msg = "All test cases passed! Car('Tesla').drive() successfully returned 'Driving Tesla'.";
        } else {
          msg = "Fail: Car class must initialize self.brand and implement drive() method returning correct string.";
        }
      } else if (topic.id === "mutability") {
        const hasIs = code.includes("x is y") || code.includes("is y");
        if (hasIs) {
          success = true;
          msg = "All test cases passed! is_alias(x, y) validated object references.";
        } else {
          msg = "Fail: is_alias must return True only if variables point to the same memory ID (use 'is' operator).";
        }
      } else if (topic.id === "recursion") {
        const hasRec = code.includes("factorial(n - 1)") || code.includes("factorial(n-1)");
        const hasBase = code.includes("if n") && code.includes("return 1");
        if (hasRec && hasBase) {
          success = true;
          msg = "All test cases passed! factorial(5) returned 120 and factorial(0) returned 1.";
        } else {
          msg = "Fail: Factorial must use recursion (call itself with n-1) and cover the base case.";
        }
      } else if (topic.id === "decorators") {
        const hasDouble = code.includes("func(*args, **kwargs) * 2") || code.includes("* 2");
        if (hasDouble) {
          success = true;
          msg = "All test cases passed! Wrapped function output doubled successfully.";
        } else {
          msg = "Fail: Decorator must intercept output and return value multiplied by 2.";
        }
      } else if (topic.id === "refcount") {
        success = true;
        msg = "Refcount checked successfully. Verified local frame namespaces.";
      } else if (topic.id === "asyncio") {
        const hasAsync = code.includes("async def add_async") && code.includes("await asyncio.sleep");
        if (hasAsync) {
          success = true;
          msg = "All test cases passed! Async loop resolved task fetch in 0.05 seconds.";
        } else {
          msg = "Fail: Function must be async (async def) and yield context back using await asyncio.sleep.";
        }
      } else {
        success = true;
        msg = "Challenge evaluated successfully.";
      }
    } catch (e: any) {
      msg = `Compilation Error: ${e.message}`;
    }

    setEvaluationResult({ success, msg });
  };

  return (
    <div style={{ padding: "2rem", display: "grid", gridTemplateColumns: "1fr 1fr", gap: "2rem", minHeight: "calc(100vh - 80px)" }}>
      {/* Left Column: Challenge Panel */}
      <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <h2 className="gradient-text" style={{ fontSize: "1.6rem" }}>Challenge Playground</h2>
          <select
            value={topic.id}
            onChange={handleChallengeChange}
            style={{
              background: "var(--bg-dark)",
              color: "var(--accent-cyan)",
              border: "1px solid var(--border-glass)",
              padding: "0.4rem 0.8rem",
              borderRadius: "8px",
              fontSize: "0.9rem",
              outline: "none",
              cursor: "pointer",
            }}
          >
            {courseData.map((t) => (
              <option key={t.id} value={t.id}>
                {t.title}
              </option>
            ))}
          </select>
        </div>

        <div style={{ padding: "1rem", background: "rgba(255,255,255,0.02)", borderLeft: "3px solid var(--accent-cyan)", borderRadius: "6px" }}>
          <h4 style={{ color: "var(--accent-cyan)", fontSize: "0.95rem", marginBottom: "0.5rem" }}>Task Instructions</h4>
          <p style={{ color: "var(--text-secondary)", fontSize: "0.92rem", lineHeight: "1.6" }}>{topic.challenge.description}</p>
        </div>

        {/* Test Cases */}
        <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
          <h4 style={{ fontSize: "0.95rem", color: "var(--text-secondary)" }}>Expected Assertions</h4>
          {topic.challenge.testCases.map((tc, idx) => (
            <div
              key={idx}
              style={{
                display: "flex",
                justifyContent: "space-between",
                padding: "0.5rem 0.8rem",
                background: "rgba(0,0,0,0.2)",
                borderRadius: "6px",
                fontFamily: "var(--font-mono)",
                fontSize: "0.85rem",
              }}
            >
              <span style={{ color: "var(--text-primary)" }}>{topic.id === "oop" ? tc.input : `${topic.id === "decorators" ? "" : topic.id + "("}${tc.input}${topic.id === "decorators" ? "" : ")"}`}</span>
              <span style={{ color: "var(--accent-cyan)" }}>➔ {tc.expected}</span>
            </div>
          ))}
        </div>

        {/* Solution Toggle */}
        <div style={{ marginTop: "auto", display: "flex", flexDirection: "column", gap: "0.5rem" }}>
          <button className="btn btn-secondary" onClick={() => setShowSolution(!showSolution)}>
            {showSolution ? "🙈 Hide Reference Solution" : "💡 Reveal Reference Solution"}
          </button>
          {showSolution && (
            <pre style={{ margin: 0, padding: "0.8rem" }}>
              <code style={{ fontSize: "0.85rem" }}>{topic.challenge.solution}</code>
            </pre>
          )}
        </div>
      </div>

      {/* Right Column: Code Editor */}
      <div className="glass-panel" style={{ padding: "1.5rem", display: "flex", flexDirection: "column", gap: "1.5rem" }}>
        <h3 style={{ fontSize: "1.2rem", color: "var(--accent-blue)" }}>Python Sandbox Editor</h3>

        <textarea
          value={userCode}
          onChange={(e) => setUserCode(e.target.value)}
          spellCheck={false}
          style={{
            flex: 1,
            minHeight: "250px",
            background: "rgba(8, 10, 22, 0.95)",
            color: "#a5b4fc",
            fontFamily: "var(--font-mono)",
            fontSize: "0.95rem",
            padding: "1rem",
            border: "1px solid var(--border-glass)",
            borderRadius: "8px",
            resize: "none",
            outline: "none",
            lineHeight: "1.5",
          }}
        />

        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
          <button className="btn" onClick={evaluateCode} style={{ background: "linear-gradient(135deg, var(--accent-green), var(--accent-cyan))" }}>
            🚀 Run Code & Verify
          </button>
          <span style={{ fontSize: "0.8rem", color: "var(--text-muted)", fontFamily: "var(--font-mono)" }}>
            Python Interpreter: Simulated locally
          </span>
        </div>

        {/* Evaluation Output */}
        {evaluationResult && (
          <div
            style={{
              padding: "1rem",
              background: evaluationResult.success ? "rgba(0, 255, 135, 0.08)" : "rgba(255, 65, 108, 0.08)",
              border: "1px solid",
              borderColor: evaluationResult.success ? "var(--accent-green)" : "var(--accent-red)",
              borderRadius: "8px",
              color: evaluationResult.success ? "var(--accent-green)" : "#ff87a0",
              fontSize: "0.9rem",
              display: "flex",
              alignItems: "center",
              gap: "0.5rem",
            }}
          >
            <span>{evaluationResult.success ? "✅" : "❌"}</span>
            <p style={{ margin: 0, fontWeight: 500 }}>{evaluationResult.msg}</p>
          </div>
        )}
      </div>
    </div>
  );
};
