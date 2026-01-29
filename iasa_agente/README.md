# Autonomous Agents (iasa_agente)

## Phases 3-13: From Reactive Behaviors to Reinforcement Learning

A comprehensive Python implementation of progressively sophisticated autonomous agent architectures, demonstrating the evolution from simple reactive behaviors to advanced learning systems.
---

## Overview

This project implements **11 development phases** (3-13) covering the complete spectrum of agent design paradigms:

| Phase | Name | Focus | Algorithms |
|---|---|---|---|
| **3-5** | Reactive Behaviors | Agent responds to stimuli | Hierarchy, Suppression, Memory |
| **6-8** | State Space Search | Problem-solving with search | BFS, DFS, A*, Greedy |
| **9-10** | Deliberative Planning | Multi-step planning | PlanPEE, PlanPDM |
| **11-12** | MDPs | Decision under uncertainty | Utility iteration |
| **13** | Learning | Adaptive behavior | Q-Learning |

---

## Directory Structure

```
iasa_agente/
├── src/
│   ├── controlo_react/              # Phases 3-5: Reactive Control
│   │   ├── controloreact.py         # Main reactive controller
│   │   └── reacoes/                 # Behavior implementations
│   │       ├── aproximar/           # Approach behavior module
│   │       ├── evitar/              # Avoidance behavior module
│   │       ├── explorar.py          # Exploration behavior
│   │       ├── resposta/            # Response behavior
│   │       └── recolher.py          # Collection behavior
│   │
│   ├── controlo_delib/              # Phases 9-10: Deliberative Control
│   │   ├── controlodelib.py         # Deliberative controller
│   │   ├── modelomundo.py           # World model representation
│   │   ├── operadormover.py         # Movement operators
│   │   └── planeador.py             # Planning interface
│   │
│   ├── controlo_aprend/             # Phase 13: Learning Control
│   │   ├── controloaprendref.py     # Learning control integration
│   │   └── mecaprend.py             # Learning mechanism
│   │
│   ├── lib/                         # Core AI Libraries
│   │   ├── pee/                     # Phases 6-8: State Space Search
│   │   │   ├── estado.py            # State representation
│   │   │   ├── operador.py          # Operator (state transition)
│   │   │   ├── problema.py          # Problem definition
│   │   │   ├── fronteira.py         # Search frontier (FIFO/LIFO/Priority)
│   │   │   ├── mecanismoprocura.py  # Search mechanism base
│   │   │   ├── busca_profundidade.py # DFS implementation
│   │   │   ├── busca_largura.py     # BFS implementation
│   │   │   ├── busca_custo_uniforme.py # Uniform cost
│   │   │   ├── busca_sfrega.py      # Greedy search
│   │   │   ├── busca_astar.py       # A* search
│   │   │   └── procura_grafo.py     # Graph search with cycle detection
│   │   │
│   │   ├── pdm/                     # Phases 11-12: Markov Decision Process
│   │   │   ├── mdp.py               # MDP model
│   │   │   ├── solucionadorpdm.py   # MDP solver
│   │   │   ├── utilidade.py         # Utility calculation
│   │   │   └── politica.py          # Policy representation
│   │   │
│   │   ├── aprend_ref/              # Phase 13: Reinforcement Learning
│   │   │   ├── aprendref.py         # Reinforcement learning base
│   │   │   ├── aprendq.py           # Q-Learning implementation
│   │   │   ├── memoriaaprend.py     # Learning memory interface
│   │   │   ├── memoriaesparsa.py    # Sparse Q-value storage
│   │   │   ├── selaccao.py          # Action selection interface
│   │   │   ├── selaccaoegreedy.py   # ε-Greedy strategy
│   │   │   └── selaccaomaxima.py    # Maximal action selection
│   │   │
│   │   ├── plan/                    # Planning algorithms
│   │   │   ├── planpee.py           # State-space planner
│   │   │   ├── planpdm.py           # MDP-based planner
│   │   │   └── planejador.py        # Planner interface
│   │   │
│   │   ├── ecr/                     # Behavior Control Libraries
│   │   │   ├── comportamento.py     # Behavior base class
│   │   │   ├── comportamento_ativo.py # Active behavior
│   │   │   └── compilador_comportamentos.py # Behavior composition
│   │   │
│   │   ├── mod/                     # Model Components
│   │   │   ├── componente.py        # Component base class
│   │   │   ├── agente.py            # Agent interface
│   │   │   ├── ambiente.py          # Environment interface
│   │   │   └── simulador.py         # Simulation framework
│   │   │
│   │   └── sae/                     # System for Execution Environments
│   │       ├── sae_doc.pdf          # SAE documentation
│   │       ├── ambiente_exec.py     # Execution environment
│   │       └── simulador_sae.py     # SAE simulator integration
│   │
│   └── teste/                       # Test files and examples
│       ├── teste_busca.py           # Search algorithm tests
│       ├── teste_pdm.py             # MDP solver tests
│       ├── teste_aprendq.py         # Q-Learning tests
│       └── teste_comportamentos.py  # Behavior tests
│
├── .env                             # Environment configuration
├── .idea/                           # IDE settings (PyCharm)
└── requirements.txt                 # Python dependencies
```

---

## Project Phases Detail

### **Phase 3-5: Reactive Behavior Control**

**Objective**: Implement hierarchical reactive behaviors with memory integration.

#### Architecture

```
┌─────────────────────────────┐
│   Reactive Controller       │
├─────────────────────────────┤
│ Behavior Hierarchy:         │
│ ├─ EvitarObstaculo (HIGH)  │
│ ├─ AproximarAlvo (MEDIUM)  │
│ └─ Explorar (LOW)           │
│                             │
│ Memory: Visited locations   │
│ Goal: Collect targets      │
└─────────────────────────────┘
```

#### Key Components

**1. ControloReact** (`controloreact.py`)
- Manages behavior hierarchy
- Selects active behavior based on priority
- Integrates memory system
- Executes action determined by active behavior

**2. Behavior Modules** (`reacoes/`)
- **Explorar**: Random exploration with memory
- **AproximarAlvo**: Approach nearest target with collision awareness
- **EvitarObstaculo**: Avoid obstacles with priority suppression
- **Recolher**: Collect/interact with targets

**3. Memory System**
- Tracks visited locations
- Prevents infinite loops
- Maintains state across cycles

#### Key Concepts

**Behavior Hierarchy**:
```
If obstacle detected → Execute EvitarObstaculo (suppresses lower behaviors)
Else if target visible → Execute AproximarAlvo
Else → Execute Explorar (default)
```

**Suppression Mechanism**:
- Higher priority behaviors can inhibit lower ones
- Prevents conflicting actions
- Enables coordinated composite behaviors

**Memory Integration**:
- Agents remember visited locations
- Prevents re-exploration of known areas
- Improves exploration efficiency

---

### **Phase 6-8: State Space Search**

**Objective**: Implement search algorithms for problem-solving in deterministic environments.

#### Problem Model

**State Representation** (`estado.py`)
```python
state = (x, y, facing_direction)  # Complete system configuration
```

**Operators** (`operador.py`)
```python
operator = (action, preconditions, cost, effects)
# Example: Move north costs 1, changes (x,y) coordinates
```

**Problem Definition** (`problema.py`)
```python
problem = (initial_state, operators, goal_state)
```

#### Search Algorithms Implemented

**1. Uninformed Search** (No domain knowledge)

| Algorithm | Optimal | Complete | Space | Time | Notes |
|---|---|---|---|---|---|
| **BFS** | ✓ | ✓ | O(b^d) | O(b^d) | Explores level-by-level |
| **DFS** | ✗ | Limited | O(d) | O(b^d) | Memory efficient |
| **Depth-Limited** | ✗ | ✗ | O(d) | O(b^d) | Prevents infinite loops |
| **Iterative Deepening** | ✓ | ✓ | O(d) | O(b^d) | Combines BFS+DFS |

**2. Informed Search** (Uses heuristics)

| Algorithm | Optimal | Complete | Strategy |
|---|---|---|---|
| **Uniform Cost** | ✓ | ✓ | Minimize path cost |
| **Greedy** | ✗ | ✗ | Minimize estimated remaining cost |
| **A\*** | ✓ | ✓ | g(n) + h(n) = cost + heuristic |

#### Key Files

- `busca_profundidade.py` - Depth-First Search
- `busca_largura.py` - Breadth-First Search
- `busca_custo_uniforme.py` - Uniform cost search
- `busca_astar.py` - A* with heuristics
- `procura_grafo.py` - Graph search with cycle detection

#### Frontier Management

```
FIFO (Queue) → Breadth-First
LIFO (Stack) → Depth-First
Priority Queue → Uniform Cost / A*
```

---

### **Phase 9-10: Deliberative Planning**

**Objective**: Build agents that plan multi-step solutions before execution.

#### Agent Architecture

```
┌──────────────────────────────────┐
│   Perception                     │
│   (Read current world state)     │
└──────────────────────────────────┘
           ↓
┌──────────────────────────────────┐
│   World Model Update             │
│   (Maintain belief state)        │
└──────────────────────────────────┘
           ↓
┌──────────────────────────────────┐
│   Planning (Deliberation)        │
│   - PlanPEE: A* search          │
│   - PlanPDM: MDP solver         │
└──────────────────────────────────┘
           ↓
┌──────────────────────────────────┐
│   Plan Execution                 │
│   (Follow computed plan)         │
└──────────────────────────────────┘
           ↓
┌──────────────────────────────────┐
│   Replanning Check               │
│   (Replan if world changed)      │
└──────────────────────────────────┘
```

#### Planner Types

**1. PlanPEE** (`planpee.py`) - State-Space Planner
- Uses A* search to find action sequence
- Creates explicit plan before execution
- Replans when environment deviates from model

**2. PlanPDM** (`planpdm.py`) - MDP-Based Planner
- Uses probabilistic model of environment
- Computes expected utilities per action
- Handles stochastic transitions

#### World Model

**ModeloMundo** (`modelomundo.py`)
- Represents agent's beliefs about environment
- Updated with perceptions
- Used for lookahead during planning
- Independent of actual environment

#### Planning Process

```
1. Current State (perception)
2. Goal Definition (what to achieve)
3. Lookahead Simulation (what-if analysis)
4. Operator Application (possible actions)
5. Plan Generation (sequence of actions)
6. Plan Execution (follow plan)
7. Monitoring (check if still valid)
8. Replanning (if necessary)
```

---

### **Phase 11-12: Markov Decision Processes**

**Objective**: Model decision-making under uncertainty and probabilistic environments.

#### MDP Formalism

**Components** (`mdp.py`)
```python
MDP = {
    states: S,                  # Set of all possible states
    actions: A(s),              # Available actions per state
    transitions: P(s'|s,a),    # Probability of outcome
    rewards: R(s,a),           # Immediate payoff
    gamma: γ                    # Discount factor (0 < γ ≤ 1)
}
```

#### Utility Calculation (`utilidade.py`)

**Bellman Equation**:
```
U(s) = max_a [ Σ P(s'|s,a) × (R(s,a) + γ × U(s')) ]
```

**Iterative Algorithm**:
1. Initialize utilities (U = 0)
2. Repeat until convergence:
   - For each state: Update U(s) using Bellman equation
   - Check if max difference < ε (convergence threshold)
3. Return final utility values

#### Policy Extraction (`politica.py`)

Once utilities converge:
```python
policy(s) = argmax_a [ Σ P(s'|s,a) × (R(s,a) + γ × U(s')) ]
```

#### Parameter Impact

| Parameter | Low Value | High Value | Effect |
|---|---|---|---|
| **γ (discount)** | 0 | 1 | Myopic ← → Far-sighted |
| **α (learning rate)** | 0 | 1 | Slow ← → Fast updates |
| **ε (exploration)** | 0 | 1 | Greedy ← → Random |

---

### **Phase 13: Reinforcement Learning**

**Objective**: Learn optimal behavior through trial-and-error without world model.

#### Q-Learning Algorithm (`aprendq.py`)

**Q-Value**: Estimated utility of action in state
```
Q(s,a) = expected future discounted reward for action a in state s
```

**Learning Rule** (Temporal Difference):
```
Q(s,a) ← Q(s,a) + α × [r + γ × max_a' Q(s',a') - Q(s,a)]
         └──────┘        └─────────────────────────────┘
         old value       prediction error (TD error)
```

#### Components

**1. AprendQ** (`aprendq.py`)
- Core Q-Learning algorithm
- Updates Q-values based on experience
- Maintains learning statistics

**2. Memory System** (`memoriaesparsa.py`)
- Stores Q-values for state-action pairs
- Only stores non-zero values (sparse)
- Efficient for large state spaces

**3. Action Selection** (`selaccaoegreedy.py`)
- ε-Greedy strategy
- Probability ε: random action (exploration)
- Probability 1-ε: best known action (exploitation)
- Epsilon decays over time for convergence

#### Learning Process

```
Initialize: Q(s,a) = 0 for all s,a

Repeat for each episode:
    s = initial_state
    Repeat for each step in episode:
        a = select_action(s) using ε-Greedy
        Execute a, observe reward r and next state s'
        Q(s,a) ← Q(s,a) + α × [r + γ × max_a' Q(s',a') - Q(s,a)]
        s ← s'
    Until s is terminal
Until convergence
```

#### Key Parameters

| Parameter | Typical Range | Effect |
|---|---|---|
| **Learning Rate (α)** | 0.01 - 0.1 | Fast vs. slow convergence |
| **Discount (γ)** | 0.9 - 0.99 | Future reward importance |
| **Initial Epsilon (ε)** | 0.1 - 1.0 | Starting exploration level |
| **Epsilon Decay** | 0.995 - 0.9999 | How fast to reduce exploration |

---

## Environment Integration

### SAE Framework

**Sistema de Ambientes de Execução** (System for Execution Environments)

The SAE provides:
- **Environment Simulation**: Grid worlds, continuous spaces
- **Agent Execution**: Timestep-based or event-based
- **Visualization**: Real-time display of agent behavior
- **Data Logging**: Trajectory and reward tracking

**Usage**:
```python
from lib.sae import ambiente_exec
env = ambiente_exec.AmbienteSAE(grid_size=10, obstacles=True)
agent = MeuAgente(env)
agent.executar(timesteps=1000)
```

### Integration Patterns

**Phase 3-5**: Behaviors interact with SAE environment
**Phase 6-8**: Search uses problem model of environment
**Phase 9-10**: Planning with world model, execution in SAE
**Phase 11-12**: MDP solver for SAE environment
**Phase 13**: Q-Learning agents in SAE environment

---



---

## Testing & Validation

Test files in `src/teste/`:
- `teste_busca.py` - Validates search algorithms
- `teste_pdm.py` - Validates MDP solver
- `teste_aprendq.py` - Validates Q-Learning
- `teste_comportamentos.py` - Validates behaviors

Run tests:
```bash
python -m pytest src/teste/ -v
```

---

## Performance Characteristics

### Search Algorithms (Phases 6-8)

| Algorithm | Time | Space | Optimal | Use Case |
|---|---|---|---|---|
| BFS | O(b^d) | O(b^d) | ✓ | Small graphs, shortest path |
| DFS | O(b^d) | O(d) | ✗ | Memory constrained |
| A* | O(b^d) | O(b^d) | ✓ | Heuristic available |
| Greedy | O(b log b) | O(b) | ✗ | Speed critical |

### Planning (Phases 9-10)

| Planner | Complexity | Stochastic | Use Case |
|---|---|---|---|
| PlanPEE | O(search complexity) | No | Deterministic environments |
| PlanPDM | O(states² × iterations) | Yes | Uncertain environments |

### Learning (Phase 13)

| Aspect | Value | Notes |
|---|---|---|
| Convergence | O(1/iterations) | Slower than planned agents |
| Memory | O(states × actions) | Sparse representation efficient |
| Time/Step | O(1) | Constant action selection |

---

## Learning Outcomes

After completing this project, you understand:

1. ✓ Reactive behavior hierarchies and suppression
2. ✓ State space search with various strategies
3. ✓ Graph search with cycle detection
4. ✓ Heuristic design (admissibility, consistency)
5. ✓ Planning with world models and lookahead
6. ✓ Markov Decision Processes and utility
7. ✓ Q-Learning and temporal difference learning
8. ✓ Exploration-exploitation trade-off
9. ✓ Architecture progression from reactive to learning
10. ✓ Software engineering for AI systems
---

**Author**: Pedro Azevedo (A47094)  
**Institution**: ISEL - Instituto Superior de Engenharia de Lisboa  
**Course**: Artificial Intelligence for Autonomous Systems (IASA)  
