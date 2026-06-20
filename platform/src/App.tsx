import React, { useState } from "react";
import { Navigation } from "./components/Navigation";
import { Curriculum } from "./components/Curriculum";
import { MemoryVisualizer } from "./components/MemoryVisualizer";
import { BytecodeVisualizer } from "./components/BytecodeVisualizer";
import { Playground } from "./components/Playground";

const App: React.FC = () => {
  const [activeTab, setActiveTab] = useState<string>("curriculum");
  const [selectedTopicId, setSelectedTopicId] = useState<string>("variables");

  const handleSelectTopic = (topicId: string, actionTab: string) => {
    setSelectedTopicId(topicId);
    setActiveTab(actionTab);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>
      {/* Navigation Bar */}
      <Navigation activeTab={activeTab} setActiveTab={setActiveTab} />

      {/* Page Content Workspace */}
      <main style={{ flex: 1, background: "var(--bg-deep)" }}>
        {activeTab === "curriculum" && (
          <Curriculum onSelectTopic={handleSelectTopic} />
        )}
        {activeTab === "memory" && (
          <MemoryVisualizer />
        )}
        {activeTab === "bytecode" && (
          <BytecodeVisualizer />
        )}
        {activeTab === "playground" && (
          <Playground selectedTopicId={selectedTopicId} />
        )}
      </main>
    </div>
  );
};

export default App;
