import streamlit as st
import dis
import asyncio
from pathlib import Path

# Set page configuration with a premium dark theme feel
st.set_page_config(
    page_title="Code Pathshala - Interactive Learning Visualizer",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for premium styling (cyberpunk space dark design, glassmorphism card layouts, animations)
st.markdown(
    """
<style>
    /* Main App Background */
    .stApp {
        background-color: #070913;
        background-image: 
            radial-gradient(at 0% 0%, rgba(79, 172, 254, 0.08) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(178, 36, 239, 0.08) 0px, transparent 50%);
        color: #f1f5f9;
    }
    
    /* Headings */
    h1, h2, h3 {
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 600;
        letter-spacing: -0.02em;
    }
    
    /* Glassmorphism Card Style */
    .glass-card {
        background: rgba(22, 29, 63, 0.45);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
        border-color: rgba(0, 242, 254, 0.2);
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.45), 0 0 20px rgba(0, 242, 254, 0.15);
    }
    
    /* Memory block design */
    .memory-block {
        padding: 1rem;
        background: rgba(178, 36, 239, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        margin-bottom: 0.8rem;
    }
    .memory-block.highlight {
        border-color: #00F2FE;
        box-shadow: 0 0 15px rgba(0, 242, 254, 0.25);
    }
</style>
""",
    unsafe_allow_html=True,
)

# ----------------- DATA STRUCTURES -----------------

scenarios = [
    {
        "title": "Variable Aliasing (Lists)",
        "code": ["original = [1, 2, 3]", "alias = original", "alias.append(4)"],
        "steps": [
            {
                "explanation": "Allocates a list [1, 2, 3] on the Heap (address 0x7fa1) and binds variable 'original' on the Stack to point to it. Refcount = 1.",
                "stack": [{"name": "original", "val": "0x7fa1"}],
                "heap": [
                    {
                        "addr": "0x7fa1",
                        "type": "list",
                        "val": "[1, 2, 3]",
                        "ref": 1,
                        "hl": True,
                    }
                ],
            },
            {
                "explanation": "Assignment 'alias = original' copies the reference pointer, not the list data. Both variables point to 0x7fa1. Refcount increases to 2.",
                "stack": [
                    {"name": "original", "val": "0x7fa1"},
                    {"name": "alias", "val": "0x7fa1"},
                ],
                "heap": [
                    {
                        "addr": "0x7fa1",
                        "type": "list",
                        "val": "[1, 2, 3]",
                        "ref": 2,
                        "hl": False,
                    }
                ],
            },
            {
                "explanation": "Modifying via 'alias' updates the shared list object in-place at 0x7fa1. Both variables reflect changes since they share the pointer.",
                "stack": [
                    {"name": "original", "val": "0x7fa1"},
                    {"name": "alias", "val": "0x7fa1"},
                ],
                "heap": [
                    {
                        "addr": "0x7fa1",
                        "type": "list",
                        "val": "[1, 2, 3, 4]",
                        "ref": 2,
                        "hl": True,
                    }
                ],
            },
        ],
    },
    {
        "title": "Reference Counting & del",
        "code": ["x = ['payload']", "y = x", "del x", "del y"],
        "steps": [
            {
                "explanation": "Creates a list at 0x810c. Stack variable 'x' binds to it. Refcount = 1.",
                "stack": [{"name": "x", "val": "0x810c"}],
                "heap": [
                    {
                        "addr": "0x810c",
                        "type": "list",
                        "val": "['payload']",
                        "ref": 1,
                        "hl": True,
                    }
                ],
            },
            {
                "explanation": "Variable 'y' is assigned the same reference. Both point to 0x810c. Refcount is 2.",
                "stack": [
                    {"name": "x", "val": "0x810c"},
                    {"name": "y", "val": "0x810c"},
                ],
                "heap": [
                    {
                        "addr": "0x810c",
                        "type": "list",
                        "val": "['payload']",
                        "ref": 2,
                        "hl": False,
                    }
                ],
            },
            {
                "explanation": "'del x' removes variable 'x' from scope. Heap refcount decreases to 1. The object remains alive.",
                "stack": [{"name": "y", "val": "0x810c"}],
                "heap": [
                    {
                        "addr": "0x810c",
                        "type": "list",
                        "val": "['payload']",
                        "ref": 1,
                        "hl": True,
                    }
                ],
            },
            {
                "explanation": "'del y' removes the last reference. Refcount hits 0. Python's memory manager immediately deallocates the object.",
                "stack": [],
                "heap": [],
            },
        ],
    },
    {
        "title": "Shallow Copy vs Deep Copy",
        "code": ["x = [[1]]", "y = x.copy() # Shallow", "y[0].append(2)"],
        "steps": [
            {
                "explanation": "Creates an outer list at 0x90a1 containing a pointer reference to a nested inner list at 0x90a2.",
                "stack": [{"name": "x", "val": "0x90a1"}],
                "heap": [
                    {
                        "addr": "0x90a1",
                        "type": "list (outer)",
                        "val": "[0x90a2]",
                        "ref": 1,
                        "hl": False,
                    },
                    {
                        "addr": "0x90a2",
                        "type": "list (inner)",
                        "val": "[1]",
                        "ref": 1,
                        "hl": False,
                    },
                ],
            },
            {
                "explanation": "Shallow copy creates a NEW outer list at 0x90b1. However, it copies pointers of nested elements. Both outer lists share inner list 0x90a2.",
                "stack": [
                    {"name": "x", "val": "0x90a1"},
                    {"name": "y", "val": "0x90b1"},
                ],
                "heap": [
                    {
                        "addr": "0x90a1",
                        "type": "list (outer)",
                        "val": "[0x90a2]",
                        "ref": 1,
                        "hl": False,
                    },
                    {
                        "addr": "0x90b1",
                        "type": "list (outer)",
                        "val": "[0x90a2]",
                        "ref": 1,
                        "hl": True,
                    },
                    {
                        "addr": "0x90a2",
                        "type": "list (inner)",
                        "val": "[1]",
                        "ref": 2,
                        "hl": False,
                    },
                ],
            },
            {
                "explanation": "Appending 2 to y[0] targets the nested list 0x90a2. Both variables now reflect the nested change since they share the pointer.",
                "stack": [
                    {"name": "x", "val": "0x90a1"},
                    {"name": "y", "val": "0x90b1"},
                ],
                "heap": [
                    {
                        "addr": "0x90a1",
                        "type": "list (outer)",
                        "val": "[0x90a2]",
                        "ref": 1,
                        "hl": False,
                    },
                    {
                        "addr": "0x90b1",
                        "type": "list (outer)",
                        "val": "[0x90a2]",
                        "ref": 1,
                        "hl": False,
                    },
                    {
                        "addr": "0x90a2",
                        "type": "list (inner)",
                        "val": "[1, 2]",
                        "ref": 2,
                        "hl": True,
                    },
                ],
            },
        ],
    },
]

challenges = {
    "variables": {
        "title": "Reference Swap",
        "description": "Implement a function `swap_values(a, b)` that swaps references and returns a tuple `(b, a)`.",
        "template": "def swap_values(a, b):\n    # Write your solution here\n    pass",
        "test": lambda fn: fn(10, 20) == (20, 10)
        and fn("hello", "world") == ("world", "hello"),
    },
    "strings": {
        "title": "Reverse String Slicing",
        "description": "Implement `reverse_string(s)` using Python slicing syntax (`s[::-1]`) to return a reversed copy.",
        "template": "def reverse_string(s):\n    # Write your solution here\n    pass",
        "test": lambda fn: fn("python") == "nohtyp" and fn("radar") == "radar",
    },
    "oop": {
        "title": "Custom Car Class",
        "description": "Implement a class `Car` with constructor `__init__(self, brand)` and a method `drive(self)` returning 'Driving [brand]'.",
        "template": "class Car:\n    # Implement constructor and drive method\n    pass",
        "test": lambda cls: hasattr(cls, "drive")
        and cls("Tesla").drive() == "Driving Tesla",
    },
    "advanced": {
        "title": "Custom Calls Decorator",
        "description": "Implement a decorator `count_calls` that increments and stores call counts under wrapper attribute `calls` on each execution.",
        "template": "def count_calls(func):\n    # Write decorator wrapping logic\n    pass",
        "test": lambda decorator: hasattr(decorator(lambda: None), "calls"),
    },
    "asyncio": {
        "title": "Concurrent Adder",
        "description": "Create an async function `add_async(a, b)` that yields control with `await asyncio.sleep(0.05)` and then returns sum `a + b`.",
        "template": "import asyncio\n\nasync def add_async(a, b):\n    # Write async code here\n    pass",
        "test": lambda fn: asyncio.run(fn(5, 5)) == 10,
    },
}

# ----------------- SIDEBAR ROUTING -----------------

st.sidebar.markdown(
    "<h2 style='text-align: center; color: #00F2FE;'>🐍 Code Pathshala</h2>",
    unsafe_allow_html=True,
)
st.sidebar.markdown(
    "<p style='text-align: center; color: #64748b; font-size:0.85em;'>Centralized Visual Learning Platform</p>",
    unsafe_allow_html=True,
)
st.sidebar.divider()

page = st.sidebar.radio(
    "Choose Platform Section:",
    [
        "📚 Course Curriculum",
        "💾 RAM/Memory Visualizer",
        "⚙️ Live Bytecode Disassembler",
        "🎯 Live Coding Playground",
    ],
)

st.sidebar.divider()
st.sidebar.info(
    "💡 Tip: All simulations and code execution sandbox run live locally using your local Python interpreter!"
)

# ----------------- PAGE 1: CURRICULUM -----------------

if page == "📚 Course Curriculum":
    st.markdown(
        "<h1 class='gradient-text'>Python Course Curriculum</h1>",
        unsafe_allow_html=True,
    )
    st.write("Browse tracks and inspect lessons, internals, and source code modules.")
    st.divider()

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📚 Modules Selection")
        selected_track = st.selectbox(
            "Select Track:",
            [
                "Track 1: College Foundations",
                "Track 2: Intermediate OOP",
                "Track 3: Advanced VM Features",
                "Track 4: Professional Internals",
            ],
        )

        if selected_track == "Track 1: College Foundations":
            topic = st.radio(
                "Select Lesson:", ["ex_01_variables", "ex_02_strings", "ex_03_loops"]
            )
        elif selected_track == "Track 2: Intermediate OOP":
            topic = st.radio("Select Lesson:", ["ex_04_oop"])
        elif selected_track == "Track 3: Advanced VM Features":
            topic = st.radio("Select Lesson:", ["ex_05_advanced"])
        else:
            topic = st.radio("Select Lesson:", ["ex_06_internals"])

    with col2:
        st.subheader("📖 Lesson Content Viewer")
        filepath = Path(f"exercises/{topic}.md")
        if filepath.exists():
            content = filepath.read_text(encoding="utf-8")
            st.markdown(content)
        else:
            st.warning(f"Exercise file {filepath.name} not found.")

# ----------------- PAGE 2: MEMORY VISUALIZER -----------------

elif page == "💾 RAM/Memory Visualizer":
    st.markdown(
        "<h1 class='gradient-text'>Interactive Memory Visualizer</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Step through Python statements to trace heap objects, variable pointers, and reference counters."
    )
    st.divider()

    scenario_idx = st.selectbox(
        "Select Scenario:",
        range(len(scenarios)),
        format_func=lambda idx: scenarios[idx]["title"],
    )
    scene = scenarios[scenario_idx]

    if (
        "step" not in st.session_state
        or st.session_state.get("last_scene") != scenario_idx
    ):
        st.session_state["step"] = 0
        st.session_state["last_scene"] = scenario_idx

    step_idx = st.session_state["step"]

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("📝 Code Trace")
        # Render code trace lines
        for i, line in enumerate(scene["code"]):
            is_active = i == step_idx
            bg = "rgba(0, 242, 254, 0.15)" if is_active else "transparent"
            border = "3px solid #00F2FE" if is_active else "3px solid transparent"
            weight = "bold" if is_active else "normal"
            color = "#f1f5f9" if is_active else "#64748b"

            st.markdown(
                f"""
            <div style='background: {bg}; border-left: {border}; font-family: monospace; padding: 0.4rem 0.8rem; border-radius: 4px; font-weight: {weight}; color: {color};'>
                {line}
            </div>
            """,
                unsafe_allow_html=True,
            )

        st.write("")

        # Navigation buttons
        ctrl_prev, ctrl_next = st.columns(2)
        with ctrl_prev:
            if st.button("◀ Previous", disabled=step_idx == 0):
                st.session_state["step"] -= 1
                st.rerun()
        with ctrl_next:
            if st.button("Next ▶", disabled=step_idx == len(scene["steps"]) - 1):
                st.session_state["step"] += 1
                st.rerun()

        # Description
        curr_step = scene["steps"][step_idx]
        st.info(f"💡 {curr_step['explanation']}")

    with col2:
        st.subheader("🧬 Memory State (RAM)")

        sub_stack, sub_heap = st.columns(2)

        with sub_stack:
            st.markdown("#### Call Stack (Variables)")
            if not curr_step["stack"]:
                st.write("*No variables in scope*")
            for var in curr_step["stack"]:
                st.markdown(
                    f"""
                <div style='padding: 0.8rem; background: rgba(79, 172, 254, 0.08); border: 1px solid rgba(255,255,255,0.05); border-radius: 6px; margin-bottom: 0.5rem; display: flex; justify-content: space-between;'>
                    <strong>{var['name']}</strong>
                    <span style='color: #00F2FE;'>➔ {var['val']}</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )

        with sub_heap:
            st.markdown("#### Heap Memory (Objects)")
            if not curr_step["heap"]:
                st.write("*No objects allocated*")
            for obj in curr_step["heap"]:
                hl_class = "highlight" if obj["hl"] else ""
                border_color = "#00F2FE" if obj["hl"] else "rgba(255,255,255,0.08)"
                glow = "box-shadow: 0 0 15px rgba(0,242,254,0.15);" if obj["hl"] else ""
                st.markdown(
                    f"""
                <div style='padding: 0.8rem; background: rgba(178, 36, 239, 0.08); border: 1px solid {border_color}; {glow} border-radius: 6px; margin-bottom: 0.5rem;'>
                    <div style='display:flex; justify-content:space-between; font-size: 0.75em;'>
                        <span style='color:#B224EF;'>{obj['addr']}</span>
                        <span style='color:#64748b;'>{obj['type']}</span>
                    </div>
                    <div style='font-size: 1.1em; font-family: monospace; color: #f1f5f9; margin: 0.2rem 0;'>{obj['val']}</div>
                    <div style='font-size: 0.75em; color: #64748b;'>Refcount: <strong style='color:#00FF87;'>{obj['ref']}</strong></div>
                </div>
                """,
                    unsafe_allow_html=True,
                )

# ----------------- PAGE 3: BYTECODE DISASSEMBLER -----------------

elif page == "⚙️ Live Bytecode Disassembler":
    st.markdown(
        "<h1 class='gradient-text'>CPython Bytecode Disassembler</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Write any valid Python expression, compile it, and view its actual CPython assembly instructions."
    )
    st.divider()

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🐍 Write Code Block")
        user_code = st.text_area(
            "Write custom Python snippet here:",
            "x = 5\ny = x + 10\nprint(y)",
            height=180,
        )
        dis_btn = st.button("⚙️ Disassemble Code")

    with col2:
        st.subheader("📃 Compiled Bytecode Output")
        if dis_btn:
            try:
                # Disassemble code safely
                bytecode = dis.Bytecode(user_code)

                instructions_data = []
                for instr in bytecode:
                    instructions_data.append(
                        {
                            "Offset": instr.offset,
                            "Opcode Name": instr.opname,
                            "Arg Val": instr.argval if instr.argval is not None else "",
                        }
                    )

                st.table(instructions_data)
            except Exception as e:
                st.error(f"Compilation error: {e}")
        else:
            st.info("👈 Enter custom python code on the left and click Disassemble.")

# ----------------- PAGE 4: CODING PLAYGROUND -----------------

elif page == "🎯 Live Coding Playground":
    st.markdown(
        "<h1 class='gradient-text'>Interactive Coding Playground</h1>",
        unsafe_allow_html=True,
    )
    st.write(
        "Solve coding challenges, run your implementations, and verify them against actual unit tests."
    )
    st.divider()

    challenge_key = st.selectbox(
        "Select Challenge Challenge:",
        list(challenges.keys()),
        format_func=lambda k: challenges[k]["title"],
    )

    chall = challenges[challenge_key]

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("📝 Challenge Instructions")
        st.markdown(
            f"""
        <div style='background: rgba(22, 29, 63, 0.4); border-left: 3px solid #00F2FE; padding: 1rem; border-radius: 6px;'>
            <h4>{chall['title']}</h4>
            <p>{chall['description']}</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

        # Display sample tests
        st.write("")
        st.write(
            "💡 **Verification Rule:** The platform executes your code block locally and checks the resulting functions against assertion states."
        )

    with col2:
        st.subheader("🐍 Python Code Editor")
        user_edit = st.text_area(
            "Write your code below:", chall["template"], height=220
        )

        run_btn = st.button("🚀 Verify & Run")

        if run_btn:
            locs = {}
            try:
                # Execute user code locally in an isolated namespace dict
                # We compile first to catch syntactic errors early
                compiled = compile(user_edit, "<string>", "exec")
                exec(compiled, {}, locs)

                # Check for correct function/class presence
                expected_fn_name = (
                    "Car"
                    if challenge_key == "oop"
                    else (
                        "add_async"
                        if challenge_key == "asyncio"
                        else (
                            "count_calls"
                            if challenge_key == "advanced"
                            else (
                                "reverse_string"
                                if challenge_key == "strings"
                                else "swap_values"
                            )
                        )
                    )
                )

                if expected_fn_name not in locs:
                    st.error(
                        f"❌ Error: Expected function or class '{expected_fn_name}' not defined in your code."
                    )
                else:
                    target_obj = locs[expected_fn_name]
                    # Evaluate assertion rules
                    test_success = chall["test"](target_obj)
                    if test_success:
                        st.success("✅ All unit tests passed! Excellent solution.")
                    else:
                        st.error(
                            "❌ Test assertion failed. Review your function logic and outputs."
                        )
            except Exception as e:
                st.exception(e)
