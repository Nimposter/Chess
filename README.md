# Chess Program
### A Command-Line Chess Application that allows two players to play chess using coordinate-based input

This program was built from scratch in Python to explore programming fundamentals, data structures and the implementation of chess rules without relying on external chess libraries

#### <ins>Features:</ins>
- Board Representation
- Turn Management
- Legal Move Generation (for all pieces)
- Captures
- Check Detection
- Checkmate
- Stalemate
- Castling
- Castling Rights
- En Passant
- Pawn Promotion
- King Safety Checks
- Half Move Clock
- Full Move Number
- FEN

## Program Flow
```mermaid
flowchart TD
    start((Start)) --> A
    A[DisplayBoard] --> B[GetMoves]
    B --> C{Match Piece}

    C -->|case Queen/Rook/Bishop| D[SlidingLegalMoves]
    C -->|case Knight| E[KnightLegalMoves]
    C -->|case Pawn| F[PawnLegalMoves]
    C -->|case King| G[KingLegalMoves]

    D --> H[FilterLegalMoves]
    E --> H
    F --> H
    G --> H

    H --> I{Is Selected Move Legal?}

    I -->|No| B
    I -->|Yes| K["Check for Special Moves<br>(Castling, En Passant, Promotion)"]

    K --> L[Modify Board]

    L --> M{CheckGameState}

    M -->|Checkmate/Stalemate| N((End))
    M -->|No| A
```
