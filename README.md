# Artificial Intelligence for Autonomous Systems (IASA)

A comprehensive academic project demonstrating the progression from reactive agents to sophisticated autonomous systems with planning and reinforcement learning. Built for the "Artificial Intelligence for Autonomous Systems" course (IASA47094) at ISEC - Instituto Superior de Engenharia de Lisboa.


---

## Project Overview

This repository contains **two integrated AI projects** totaling **13 development phases**:

### **Part 1: Animal Photography Game (Java) - Phases 1-2**
A reactive agent simulation where a virtual character autonomously photographs animals using state machine-based decision-making.

### **Part 2: Autonomous Agents Framework (Python) - Phases 3-13**
Progressive implementation of increasingly sophisticated agent architectures:
- **Reactive Behaviors** (Phases 3-5)
- **State Space Search** (Phases 6-8)
- **Deliberative Planning** (Phases 9-10)
- **Markov Decision Processes** (Phases 11-12)
- **Reinforcement Learning** (Phase 13)

---

## Repository Structure

```
Artificial-Intelligence-for-Autonomous-Systems/
├── iasa_jogo/                           # Phase 1-2: Java Game Agent
│   └── src/
│       ├── Jogo.java                    # Main game controller
│       ├── Personagem.java              # Intelligent agent character
│       ├── Ambiente.java                # Environment simulator
│       ├── Controlo.java                # State machine control
│       ├── Estado.java                  # State definition
│       ├── MaquinaEstados.java          # Generic state machine
│       ├── Transicao.java               # State transitions
│       ├── Percecao.java                # Perception wrapper
│       ├── Accao.java                   # Action enumeration
│       └── Evento.java                  # Event enumeration
│
├── iasa_agente/                         # Phase 3-13: Python Agents
│   └── src/
│       ├── controlo_react/              # Phase 3-5: Reactive Control
│       │   ├── controloreact.py
│       │   └── reacoes/                 # Behavior implementations
│       │       ├── explorar.py          # Exploration
│       │       ├── aproximar/           # Approach behavior
│       │       ├── evitar/              # Avoidance behavior
│       │       └── recolher.py          # Collection behavior
│       │
│       ├── controlo_delib/              # Phase 9-10: Deliberative Control
│       │   ├── controlodelib.py
│       │   ├── modelomundo.py           # World model
│       │   └── operadormover.py
│       │
│       ├── controlo_aprend/             # Phase 13: Learning Control
│       │   ├── controloaprendref.py
│       │   └── mecaprend.py
│       │
│       ├── lib/                         # Core AI Libraries
│       │   ├── pee/                     # Phase 6-8: State Space Search
│       │   │   └── Search algorithms: BFS, DFS, A*, Greedy
│       │   │
│       │   ├── pdm/                     # Phase 11-12: Markov Decision Processes
│       │   │   └── MDP solver
│       │   │
│       │   ├── aprend_ref/              # Phase 13: Reinforcement Learning
│       │   │   ├── aprendq.py           # Q-Learning
│       │   │   ├── selaccaoegreedy.py   # ε-Greedy action selection
│       │   │   └── memoriaesparsa.py    # Sparse memory
│       │   │
│       │   ├── plan/                    # Planning algorithms
│       │   ├── ecr/                     # Reactive behavior control
│       │   ├── mod/                     # Models library
│       │   └── sae/                     # Execution environment
│       │
│       └── teste/                       # Test files
│
├── README.md                            # Main project README
├── iasa47094relatorio.pdf               # Academic final report
└── .gitignore
```

---

##  Project Phases

### **Phase 1-2: Reactive Game Agent (Java)**
**Location**: `iasa_jogo/src/`

A reactive intelligent agent that autonomously photographs animals using state machines.

- **Architecture**: Perception → State Machine → Action
- **Components**: 10 Java classes implementing agent cycle
- **Key Concept**: Reactive agent with stateful behavior
- **Patterns**: State Machine design pattern

[👉 **Detailed README**](./iasa_jogo/README.md)

---

### **Phase 3-5: Reactive Behavior Architecture (Python)**
**Location**: `iasa_agente/src/controlo_react/`

Hierarchical reactive behaviors with agent memory and obstacle avoidance.

- **Behaviors**: 
  - `Explorar` - Random exploration
  - `AproximarAlvo` - Approach targets with priority
  - `EvitarObst` - Obstacle avoidance
  - `Recolher` - Collection behavior
- **Key Concept**: Behavior hierarchy with suppression
- **Implementation**: Behavior modules composed into reactive controller
- **Memory Integration**: Prevents infinite loops through visited location tracking

---

### **Phase 6-8: State Space Search (Python)**
**Location**: `iasa_agente/src/lib/pee/`

Implementation of multiple search algorithms for problem-solving.

**Search Algorithms**:
| Algorithm | Optimal | Complete | Notes |
|---|---|---|---|
| Breadth-First (BFS) | ✓ | ✓ | Guarantees shortest path |
| Depth-First (DFS) | ✗ | Limited | Memory efficient |
| Iterative Deepening | ✓ | ✓ | Combines BFS+DFS benefits |
| Uniform Cost | ✓ | ✓ | Finds cheapest path |
| Greedy (Best-First) | ✗ | ✗ | Fast but suboptimal |
| A* | ✓ | ✓ | Optimal with admissible heuristic |

**Problem Model**:
- States: Unique configurations
- Operators: State transformations with costs
- Goal: Target state definition
- Search Space: Graph of reachable states

---

### **Phase 9-10: Deliberative Agent with Planning (Python)**
**Location**: `iasa_agente/src/controlo_delib/`, `iasa_agente/src/lib/plan/`

Agents that plan multi-step solutions using world models.

**Planner Types**:

1. **PlanPEE** (State-Space Planner)
   - Uses search algorithms (A*, Greedy, Uniform Cost)
   - Builds explicit plan before execution
   - Reconsiders when environment changes

2. **PlanPDM** (MDP-Based Planner)
   - Probabilistic decision-making
   - Balances exploration vs. exploitation
   - Handles stochastic environments

**Decision Cycle**:
```
Perceive → Update World Model → Deliberate (Plan) → Execute → Repeat
```

---

### **Phase 11-12: Markov Decision Processes (Python)**
**Location**: `iasa_agente/src/lib/pdm/`

Probabilistic framework for decision-making under uncertainty.

**Key Concepts**:
- **States**: Complete system configurations
- **Actions**: Available choices per state
- **Transition Probabilities**: Likelihood of outcomes
- **Rewards**: Immediate payoff per action
- **Discount Factor (γ)**: Weights future vs. immediate rewards

**Utility Calculation**:
```
U(s) = max_a [ Σ P(s'|s,a) × (R(a,s) + γ × U(s')) ]
```

**Impact of Parameters**:
- γ ≈ 0: Immediate rewards preferred (short-sighted)
- γ ≈ 1: Long-term planning (far-sighted)
- Higher discount → Better convergence but more computation

---

### **Phase 13: Reinforcement Learning (Python)**
**Location**: `iasa_agente/src/controlo_aprend/`, `iasa_agente/src/lib/aprend_ref/`

Learning from experience without a world model.

**Algorithm**: Q-Learning (Off-Policy Temporal Difference)

**Components**:
- **AprendQ**: Q-Learning algorithm
- **MemoriaEsparsa**: Sparse Q-value storage (state-action pairs)
- **SelAccaoEGreedy**: ε-Greedy exploration strategy
- **ControloAprendRef**: Integration with control system

**Key Parameters**:
- **Learning Rate (α)**: How fast to update Q-values
- **Discount Factor (γ)**: Future reward weighting
- **Exploration Rate (ε)**: Balance exploration vs. exploitation

**Q-Value Update**:
```
Q(s,a) ← Q(s,a) + α × [r + γ × max_a' Q(s',a') - Q(s,a)]
```

---

## 🛠️ Technologies & Tools

### Languages
- **Java** (12.2% of codebase)
  - OOP, generics, design patterns
  
- **Python** (87.8% of codebase)
  - NumPy, SciPy for numerical computation
  - Object-oriented design

### Libraries & Frameworks
- **SAE (Sistema de Ambientes de Execução)**
  - Environment simulation and visualization
  - Agent execution framework
  - Integrated with all projects

### Development Tools
- **IDE**: PyCharm, VS Code, IntelliJ IDEA
- **Version Control**: Git/GitHub
- **Documentation**: PDF report (academic format)

---

## 📖 Detailed Project Documentation

### Project 1: Java Game Agent
- **File**: [iasa_jogo/README.md](./iasa_jogo/README.md)
- **Content**: 
  - Reactive agent architecture
  - State machine implementation
  - Class structure and design patterns
  - Game flow and execution
  - How to compile and run

### Project 2: Python Autonomous Agents
- **File**: [iasa_agente/README.md](./iasa_agente/README.md) *(to be created)*
- **Content**:
  - Reactive behavior control
  - Search algorithms and problem-solving
  - Planning and world models
  - Markov Decision Processes
  - Reinforcement learning implementation
  - Integration guide

---

##  Course Context

**Course**: Artificial Intelligence for Autonomous Systems (IASA47094)  
**Institution**: ISEL - Instituto Superior de Engenharia de Lisboa   

---

## Academic Report

A comprehensive final report document is included: **`iasa47094relatorio.pdf`**

**Report Contents**:
- Theoretical frameworks and AI concepts
- Implementation details for all phases
- Algorithm explanations and pseudocode
- Simulation results and visualizations
- Performance analysis and comparisons
- Limitations and future improvements
- Bibliography and webography

---

## Key Features

### Software Engineering
✓ Modular architecture with clear separation of concerns  
✓ Generic programming (Java generics, Python protocols)  
✓ Design patterns (State, Strategy, Composite)  
✓ Encapsulation and abstraction principles  
✓ Extensible framework for custom agents/behaviors  

### AI Concepts
✓ Reactive agent paradigm  
✓ State machine formalism  
✓ Search algorithms with complexity analysis  
✓ Planning under deterministic and stochastic conditions  
✓ Reinforcement learning with Q-Learning  

### Code Quality
✓ Well-documented with inline comments  
✓ Clear class hierarchies and interfaces  
✓ Separation between models, control, and execution  
✓ Reusable libraries for algorithm implementation  


py` | 50+ Python modules for agents |

---

## 💡 Key Insights

1. **Reactive agents are fast but brittle** - No learning or planning; cannot handle novel situations
2. **Planning adds sophistication** - Lookahead enables multi-step problem-solving
3. **Stochastic models handle uncertainty** - MDPs provide principled decision-making under risk
4. **Learning improves over time** - Q-Learning adapts behavior without explicit programming
5. **Architecture determines capability** - Same environment, different control produces vastly different behaviors

---


**Last Updated**: January 29, 2026  
**Repository Created**: 2022  
**Status**: Complete (13 phases implemented)
