# Animal Photography Game - Intelligent Agent Project

A reactive agent simulation game where a character autonomously photographs animals in a dynamic environment using state machine-based artificial intelligence. Built as coursework for "Artificial Intelligence for Autonomous Systems" (Phases 1-2).

**Part of**: [Artificial Intelligence for Autonomous Systems (IASA47094)](../README_IASA_Main.md)

---

## 📋 Project Overview

This project demonstrates the practical implementation of a **reactive intelligent agent** with the following characteristics:

- **Autonomous behavior** driven by environment events
- **State machine architecture** for decision-making and action selection  
- **Perception-action cycle** processing environmental stimuli
- **Goal-oriented actions** (search, approach, observe, and photograph animals)

---

## 🤖 Intelligent Agent Architecture

### Agent Model

This implementation follows the **Reactive Agent** paradigm, a foundational approach in autonomous systems where agents respond directly to environmental stimuli without explicit planning or internal world models.

### Agent Components (Classic Agent Model)

```
┌─────────────────────────────────────────────┐
│         INTELLIGENT AGENT                   │
├─────────────────────────────────────────────┤
│ Sensors (Perception)                        │
│ ├─ Environment.getEvento()                  │
│ └─ Returns: Current environmental state     │
├─────────────────────────────────────────────┤
│ Brain (Control & Decision-Making)           │
│ ├─ State Machine (Controlo)                 │
│ ├─ Current State Tracking                   │
│ └─ Event → Action Mapping (Transition Dict) │
├─────────────────────────────────────────────┤
│ Actuators (Action Execution)                │
│ ├─ Character.atuar(Accao)                   │
│ └─ Returns: Behavioral response             │
└─────────────────────────────────────────────┘
```

### Agent Decision Cycle

**1. Perception Phase (Sensing)**
```java
Evento evento = ambiente.getEvento();        // Read sensors
Percecao percecao = new Percecao(evento);    // Encapsulate perception
```
- Agent queries environment for current state
- Wraps event in perception object for processing
- This is the agent's "sensor reading" of the world

**2. Cognition Phase (Thinking)**
```java
Accao accao = controlo.processar(percecao);  // Brain decides
```
- State machine receives perception
- Looks up transition in dictionary:
  - **Current state** (memory) + **event** (input) → lookup
  - Returns: `Transicao<Evento, Accao>`
  - Extracts: **next state** (updated memory) + **action** (output)
- State machine updates internal state automatically

**3. Action Phase (Doing)**
```java
personagem.atuar(accao);                     // Execute behavior
```
- Agent executes determined action
- In this system: prints behavioral output
- In real robotics: moves motors, manipulates objects
- Agent returns to perception phase; loop continues

### How State Machine Enables Agent Behavior

The state machine is the agent's "reasoning engine":

```
Current State (Agent's Memory)
        ↓
    + Incoming Event (Sensory Input)
        ↓
    → Transition Lookup (Decision)
        ↓
    ├─ Next State (Updated Memory)
    └─ Action (Behavior Output)
```

**Example**: Same event, different responses based on state
```
Event: RUIDO (noise detected)

In State "Procura":  RUIDO → Transition to "Inspecao" + APROXIMAR
In State "Inspecao": RUIDO → Transition to "Inspecao" + PROCURAR
In State "Observacao": RUIDO → No transition defined
```

This stateful behavior is more intelligent than a simple reflex because:
- **Context matters** - The agent remembers where it is
- **Cumulative learning** - Actions depend on history of states
- **Goal-oriented patterns** - State sequence drives toward photography goal

### Reactive Agent Characteristics

✓ **No World Model** - Agent doesn't maintain internal map of environment  
✓ **No Planning** - Decisions are immediate; no lookahead computation  
✓ **Direct Stimulus-Response** - Every event triggers predetermined action  
✓ **Stateful Behavior** - Internal state enables context-aware responses  
✓ **Autonomous Operation** - Self-initiated decisions without human direction  
✓ **Computational Efficiency** - Real-time processing; suitable for embedded systems  

### Agent Rationality

The agent exhibits **rational behavior** within its constraints:

**Goal**: Photograph animals successfully

**Strategy**: 
- When silent → continue searching (maintain Procura state)
- When noise detected → investigate closer (transition to Inspecao)
- When animal spotted → approach and observe (Observacao → Registo)
- When able to capture → record photograph (execute FOTOGRAFAR)
- When animal flees → resume search (return to Procura)

**Outcome**: Probabilistically increases chances of accomplishing goal

### Reactive vs. Other Agent Types

| Aspect | Reactive | Deliberative | Learning |
|---|---|---|---|
| **Decision Method** | State machine lookup | Planning algorithm | Trial & error |
| **World Model** | None | Explicit model | Learned model |
| **Adaptability** | Fixed | Replans on change | Improves over time |
| **Speed** | ⚡ Very fast | ⏱ Slower | ⏱ Variable |
| **Complexity** | ✓ Simple | ✗ Complex | ✗ Complex |
| **Example** | This project | Chess AI (minimax) | Game AI (Q-learning) |

### State Diagram (Agent Behavior Flow)

```
           ┌─────────────────────────────┐
           │   START (Procura state)     │
           └──────────┬──────────────────┘
                      │
                SILENCIO│ANIMAL│RUIDO
                      │
     ┌────────────────┼────────────────┐
     ↓                ↓                ↓
┌─────────────┐ ┌──────────────┐ ┌──────────────┐
│ PROCURAR    │ │ APROXIMAR    │ │ APROXIMAR    │
│ (stay)      │ │ (→Observacao)│ │ (→Inspecao)  │
└──────┬──────┘ └──────┬───────┘ └──────┬───────┘
       │               │                 │
       └───────────────┼─────────────────┘
                       │
                 ANIMAL detected
                       │
                       ↓
              ┌─────────────────┐
              │ APROXIMAR       │
              │ (→Observacao)   │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
        ANIMAL│               FUGA
              ↓                ↓
       ┌────────────┐    (back to
       │ OBSERVAR   │     Procura)
       │ (→Registo) │
       └────────┬───┘
                │
         FOTOGRAFIA
                │
                ↓
       ┌──────────────┐
       │ FOTOGRAFAR   │
       │ (→Procura)   │
       └──────┬───────┘
              │
       TERMINAR event
              │
              ↓
          ┌────────┐
          │  EXIT  │
          └────────┘
```

### Key Agent Concepts Demonstrated

1. **Sensors** → `ambiente.getEvento()` - Reads environmental state
2. **Actuators** → `personagem.atuar(action)` - Executes behaviors
3. **Internal State** → Current state in state machine - Enables context
4. **Decision Logic** → Transition dictionary - Maps inputs to outputs
5. **Autonomy** → Self-directed cycle without external control
6. **Reactivity** → Immediate response to all perceived events

### Limitations of Reactive Design

⚠ **No Learning** - Cannot improve behavior from experience  
⚠ **No Planning** - Cannot pursue multi-step goals autonomously  
⚠ **No Communication** - Cannot interact with other agents  
⚠ **Limited Scalability** - O(states × events) complexity grows rapidly  
⚠ **Brittle** - Fixed transitions cannot handle unforeseen situations  
⚠ **Goal Representation** - Implicit in code; not declarative  

### Performance Characteristics

| Metric | Rating | Notes |
|---|---|---|
| **Autonomy** | ✓✓✓ | Complete independence; no human intervention |
| **Reactivity** | ✓✓✓ | Instant response to all events |
| **Proactivity** | ✗ | Only reacts; no self-initiated goals |
| **Social Ability** | ✗ | Single-agent; no multi-agent communication |
| **Adaptability** | ✗ | Static; cannot learn or modify behavior |
| **Efficiency** | ✓✓✓ | O(1) decision time; minimal computation |

---

## 🏗️ Architecture

### Core Components

The system follows the classic reactive agent pattern: **Perception → Control → Action**

```
Environment (Events)
    ↓
Character (Perception)
    ↓
Control (State Machine Processing)
    ↓
Action Execution
```

### Class Structure

#### Game Engine

**`Jogo.java`** - Main Game Controller
- Initializes the game environment and character
- Executes the main game loop
- Terminates when environment reaches `TERMINAR` event
- Entry point: `main(String[] args)`

#### Environment Simulation

**`Ambiente.java`** - Game World
- Manages environmental events that drive character behavior
- User-controlled event generation via keyboard input
- Event-to-action mapping using HashMap
- Supported commands:
  - `s` → SILENCIO (silence - no animal sound)
  - `r` → RUIDO (noise - animal detected by sound)
  - `a` → ANIMAL (visual detection - animal spotted)
  - `f` → FUGA (escape - animal flees)
  - `o` → FOTOGRAFIA (photography - character captures image)
  - `t` → TERMINAR (terminate - end game)

**`Evento.java`** - Event Enumeration
- `SILENCIO` - Quiet state; nothing detected
- `RUIDO` - Audio cue indicating animal presence
- `ANIMAL` - Visual confirmation of animal
- `FUGA` - Animal escapes detection
- `FOTOGRAFIA` - Character captures photograph
- `TERMINAR` - Game termination signal

#### Character & Perception

**`Personagem.java`** - Intelligent Agent
- Core perception-action cycle: `executar()`
- Interfaces with environment to retrieve events
- Delegates state/action processing to Control
- Executes actions determined by state machine
- Lifecycle:
  1. Perceive environment event
  2. Send perception to Control
  3. Receive action from Control
  4. Execute action
  5. Repeat until TERMINAR event

**`Percecao.java`** - Perception Wrapper
- Encapsulates environment event data
- Passed from Personagem to Controlo
- Carries event information for processing

#### Control Logic

**`Controlo.java`** - Decision Making Agent
- Processes perceptions and generates actions
- Manages state machine initialization
- Defines all state transitions and associated actions
- Outputs current state for logging

**State Definitions**:
- `EstadoProcura` (Search State) - Initial state; character searches for animals
- `EstadoInspecao` (Inspection State) - Investigates noise detected
- `EstadoObservacao` (Observation State) - Watching animal closely
- `EstadoRegisto` (Recording State) - Preparing to/capturing photograph

**State Transition Table**:

| Current State | Event | Next State | Action |
|---|---|---|---|
| Procura | RUIDO | Inspecao | APROXIMAR |
| Procura | SILENCIO | Procura | PROCURAR |
| Procura | ANIMAL | Observacao | APROXIMAR |
| Inspecao | ANIMAL | Observacao | APROXIMAR |
| Inspecao | RUIDO | Inspecao | PROCURAR |
| Inspecao | SILENCIO | Procura | (none) |
| Observacao | ANIMAL | Registo | OBSERVAR |
| Observacao | FUGA | Inspecao | (none) |
| Registo | FUGA | Procura | (none) |
| Registo | FOTOGRAFIA | Procura | FOTOGRAFAR |
| Registo | ANIMAL | Registo | FOTOGRAFAR |

#### Action Execution

**`Accao.java`** - Action Enumeration
- `PROCURAR` - Search for animals (initial state action)
- `APROXIMAR` - Approach detected animal
- `OBSERVAR` - Observe animal closely
- `FOTOGRAFAR` - Capture photograph of animal

#### State Machine Framework

**`MaquinaEstados.java`** - Generic State Machine
- Parameterized for events and actions
- Maintains current state
- Processes events and triggers transitions
- Returns action associated with transition
- Handles null transitions gracefully

**`Estado.java`** - State Representation
- Unique name identifier
- Transition dictionary mapping events → transitions
- Methods:
  - `transicao(Evento, EstadoSucessor, Accao)` - Define transition
  - `processar(Evento)` - Look up transition for event
  - `getNome()` - Return state name

**`Transicao.java`** - State Transition
- Encapsulates: next state + associated action
- Accessed by state machine when event occurs
- Retrieved from state's transition dictionary

## 🎮 Game Flow

### Initialization
1. `Jogo.main()` creates new `Ambiente` and `Personagem`
2. `Personagem` stores reference to `Ambiente`
3. `Controlo` initializes all states and transitions
4. Character starts in "Procura" (search) state

### Main Loop (pseudocode)
```
do {
    character.executar()           // Character perceives and acts
    environment.evoluir()          // Environment generates next event
} while (environment.getEvento() != TERMINAR)
```

### Character Execution Cycle
```
executar() {
    1. percepcao = percecionar()           // Fetch current event
    2. accao = controlo.processar(percepcao) // Get action from state machine
    3. atuar(accao)                        // Execute action (print output)
}
```

## 💻 Development Details

**Language**: Java  
**Design Pattern**: State Machine (Behavioral)  
**Agent Type**: Reactive Agent with Stateful Behavior  
**Generic Programming**: State machine parameterized for `<Evento, Accao>`  
**Container**: HashMap for transition dictionary lookup  

## ✨ Key Features

✓ **Event-Driven Behavior** - Agent responds to environmental changes  
✓ **State Persistence** - Maintains internal state across iterations  
✓ **Deterministic Transitions** - Predefined mappings ensure consistency  
✓ **Generic State Machine** - Reusable framework for any (Event, Action) pair  
✓ **Clean Separation of Concerns** - Environment, Perception, Control, Action isolated  
✓ **Extensible Design** - Easy to add new states, events, or actions  
✓ **Autonomous Agent** - Self-directed behavior cycle with no external control

## 🚀 How to Compile and Run

```bash
# Compile all Java sources
javac -d bin src/**/*.java

# Run the game
java -cp bin src.Jogo

# Follow prompts to input events:
# s - Silence
# r - Noise
# a - Animal spotted
# f - Animal flees
# o - Take photo
# t - Terminate
```

## 📝 Example Game Sequence

```
Event: SILENCIO
State: Procura
Action: PROCURAR

Event: RUIDO
State: Inspecao
Action: APROXIMAR

Event: ANIMAL
State: Observacao
Action: APROXIMAR

Event: ANIMAL
State: Registo
Action: FOTOGRAFAR

Event: FOTOGRAFIA
State: Procura
Action: PROCURAR
```

## 📐 Design Principles Applied

- **Modularity** - Each class has single responsibility
- **Encapsulation** - Internal state hidden; public interfaces only
- **Abstraction** - Generic state machine abstraction
- **DRY Principle** - Transition logic centralized in state machine
- **Composition** - Personagem composes Controlo and references Ambiente
- **Agent Paradigm** - Implements classic reactive agent model with sensors, decision logic, and actuators

## 🎓 Connection to Course Content

This project directly implements concepts from **Artificial Intelligence for Autonomous Systems**:

- ✓ **Reactive Agent Architecture** (Chapter 2.6)
- ✓ **State-Based Behavior Control**
- ✓ **Perception-Action Cycle**
- ✓ **State Machine Formalism** (Chapter 2.4 - Dinâmica)
- ✓ **Goal-Directed Behavior** (implicit photography goal)
- ✓ **Software Engineering** for intelligent systems (modularity, interfaces, abstraction)

**Advanced Topics** for Future Expansion:
- Deliberative agents with planning (A* search)
- Markov Decision Processes (MDP)
- Reinforcement learning (Q-learning)
- Multi-agent coordination

## 📚 Educational Context

This project is part of the IASA (Artificial Intelligence for Autonomous Systems) course at ISEC, demonstrating:

1. Reactive agent architecture principles
2. State machine design patterns
3. Object-oriented software engineering practices
4. Generic programming techniques
5. Clean code principles for maintainability

## 📋 Files Summary

| File | Purpose | AI Component |
|---|---|---|
| `Jogo.java` | Game initialization and main loop | System orchestration |
| `Ambiente.java` | Environment state and event generation | **Sensor input** |
| `Evento.java` | Environmental event types enumeration | Sensor data types |
| `Personagem.java` | Character with perception-action cycle | **Agent body** |
| `Controlo.java` | State machine management and initialization | **Agent brain/decision logic** |
| `Percecao.java` | Event perception wrapper | Sensory processing |
| `Accao.java` | Character action types enumeration | **Actuator outputs** |
| `MaquinaEstados.java` | Generic state machine implementation | **Core reasoning engine** |
| `Estado.java` | State representation with transitions | Agent memory |
| `Transicao.java` | State transition (next state + action) | Decision mapping |

## 🔮 Future Enhancements

- **Deliberative Agent** - Add planning/goal-based decision making (A*, BFS, DFS)
- **Multiple Agent Types** - Hybrid reactive-deliberative agents
- **Learning** - Implement Q-Learning (Reinforcement Learning) for behavior optimization
- **Multi-Agent Systems** - Support concurrent characters with communication/coordination
- **Richer Environments** - 2D grid world with spatial navigation and obstacles
- **GUI** - Visual representation of states, transitions, and agent movement
- **Logging & Analytics** - Detailed trace of decision-making process and state history
- **Nondeterministic Transitions** - Probabilistic behavior for exploratory agents

---

## 📄 License

Educational use only. Project completed as coursework for IASA47094.

---

## 👤 Author

**Pedro Azevedo** (A47094)  
Master's Degree in Informatics Engineering and Multimedia  
ISEC - Instituto Superior de Engenharia de Lisboa

---

## 🔗 Related Resources

- **[Main IASA Project](../README_IASA_Main.md)** - Overview of all 13 phases
- **[Python Agents Documentation](../iasa_agente/README.md)** - Phases 3-13
- **[Final Report](../iasa47094relatorio.pdf)** - Detailed academic analysis

---

**Last Updated**: January 29, 2026  
**Course**: IASA47094 - Artificial Intelligence for Autonomous Systems  
**Status**: Complete (Phases 1-2)
