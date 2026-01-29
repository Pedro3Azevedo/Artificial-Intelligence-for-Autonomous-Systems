# IASA47094 Report - Academic Project Summary

This is a **comprehensive final report** for the course "Artificial Intelligence for Autonomous Systems" (IASA) completed by Pedro Azevedo (Student ID: 47094) in July 2022 at ISEC (Instituto Superior de Engenharia de Lisboa), Licenciatura in Computer Engineering and Multimedia.

## Project Scope

The project implements **multiple intelligent agent architectures** progressing from reactive to deliberative agents with reinforcement learning, demonstrating sophisticated application of artificial intelligence principles combined with software engineering best practices.

## Project Phases & Implementations

### **Phase 1-2: Reactive Game Agent (Java)**
- **Application**: A photography game where a virtual character detects and photographs animals
- **Architecture**: Reactive agent using **state machines** with perception-action loops
- **Components**: `Jogo` (game), `Ambiente` (environment with events), `Personagem` (character with perception, control, and action)
- **Key Classes**: 
  - `Estado` (state representations)
  - `MaquinaEstados` (state machine managing transitions)
  - `Transicao` (state transitions with associated actions)
  - `Controlo` (event processing and action selection)

### **Phase 3-5: Reactive Behavior Architecture (Python)**
- **Environment**: Agent with obstacles and targets
- **Behaviors Implemented**: 
  - `Explorar` (random exploration)
  - `AproximarAlvo` (approach targets with priority selection)
  - `EvitarObst` (obstacle avoidance)
- **Hierarchical Behavior Control** with priority-based action selection
- **Memory Integration**: Prevents cyclic revisits and improves exploration efficiency

### **Phase 6-8: State Space Search Mechanisms (Python)**
Implemented multiple search strategies in problem-solving:

| Search Method | Optimality | Completeness | Complexity | Key Feature |
|---|---|---|---|---|
| **Breadth-First (BFS)** | ✓ Optimal | ✓ Complete | High time/space | Explores all paths |
| **Depth-First (DFS)** | ✗ Sub-optimal | ✓ Limited variants | Lower space | Single branch exploration |
| **Iterative Deepening** | ✓ Optimal | ✓ Complete | Moderate | Progressive depth increase |
| **Uniform Cost** | ✓ Optimal | ✓ Complete | Variable | Cheapest-path priority |
| **Greedy (A\*)** | ✗ Sub-optimal | ✗ Incomplete | Lower space | Heuristic-guided |
| **A\*** | ✓ Optimal | ✓ Complete | Higher space | Cost + heuristic combination |

**Architecture**: Library (`mod` package) with:
- `Estado` (unique state representation)
- `Operador` (state transformations with cost calculation)
- `Problema` (initial state + goal definition)
- `MecanismoProcura` (abstract search framework)
- `Frontiera` (LIFO, FIFO, Priority variants)

### **Phase 9-10: Deliberative Agent with Planning**
- **Agent Cycle**: Perceive → Update World Model → Deliberate → Plan → Execute
- **Reconsideration**: Re-plans when environment changes or goals are reassessed
- **Two Planner Types**:
  1. **PlanPEE** - State-space search based (using A*, Greedy, Uniform Cost)
  2. **PlanPDM** - Markov Decision Process based (probability-driven)

### **Phase 11-12: Markov Decision Processes**
- **Model Parameters**: States, actions, transition probabilities, expected rewards, discount factor (gamma)
- **Utility Calculation**: Iterative computation of state-action utilities with convergence criteria
- **Policy Generation**: Optimal action selection per state based on utility maximization
- **Key Insight**: Discount factor `gamma` influences future exploration depth; higher values = better long-term decisions but increased computational cost

### **Phase 13: Reinforcement Learning (Q-Learning)**
- **Algorithm**: Off-policy learning with temporal-difference updates
- **Agent Type**: No world knowledge; learns through trial-and-error exploration
- **Exploration vs. Exploitation**:
  - **ε-Greedy Strategy**: Balances random exploration with known high-reward actions
  - **Learning Rate (α)**: Governs speed of Q-value updates
  - **Discount Factor (γ)**: Weights immediate vs. future rewards

**Implementation Classes**:
- `AprendQ` - Q-Learning algorithm
- `MemoriaEsparsa` - Sparse Q-value storage
- `SelAccaoEGreedy` - Action selection strategy
- `ControloAprendRef` - Learning control integration

## Technical Architecture

**Languages**: Java (Phases 1-2), Python (Phases 3-13)  
**Key Libraries**: SAE (Sistema de Ambientes de Execução) for environment simulation and visualization  
**Design Patterns**: Strategy (action selection), Facade (learning abstraction), State Machine (behavior control)

## Key Software Engineering Principles Applied

- **Modularity**: Decomposition into specialized libraries (state machines, problem models, search mechanisms)
- **Factorization**: Elimination of code redundancy through inheritance and delegation
- **Abstraction**: Generic classes for extensible agent architectures
- **Low Coupling**: Interfaces separate concerns (Planner, Model, Search)
- **High Cohesion**: Specialized behaviors grouped logically

## Critical Analysis & Limitations

The report acknowledges several implementation gaps:
- **Redundant Code**: Refactoring suggestions provided for cleaner architecture
- **Computational Complexity**: Trade-off between optimal solutions (A*) and real-time performance (Greedy)
- **Non-Stationary Environments**: Deliberative agents require reconsideration logic for dynamic worlds
- **Exploration-Exploitation Trade-off**: ε-Greedy heuristic requires parameter tuning for convergence

## Learning Outcomes

The student progressed significantly in:
- Understanding AI paradigms (symbolic, connectionist, behavioral)
- Implementing reactive and deliberative agent architectures
- Software engineering discipline in complex systems
- Python proficiency, especially OOP and algorithm design

## Conclusion

This project demonstrates comprehensive mastery of **classical AI techniques** from reactive behaviors to machine learning, combining theoretical AI foundations with production-grade software engineering. The iterative progression from simple state machines to learning agents reflects industry-standard approaches in autonomous systems development.
