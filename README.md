# Lumber Optimizer

A Python package for optimizing lumber cutting patterns to minimize waste.

The algorithm takes into account multiple key factors:

1. Kerf compensation - Accounts for material loss from saw blade width
2. Multiple stock lengths - Optimizes across different available lumber lengths (e.g. 8ft, 10ft, 12ft)
3. Cut requirements - Processes both small and large cut lengths
4. Composite pieces - Handles cuts that exceed single stock length,  the optimizer preserves cut integrity whenever possible, only creating composite pieces when absolutely necessary due to stock length constraints.
5. Waste minimization - Calculates optimal cutting patterns to reduce material waste
6. Material constraints - Works within available stock length limitations
7. Cost efficiency - Helps reduce material costs by maximizing usage

## Installation

```
pip install lumber-optimizer
```

## Usage

```
from src.optimizer import optimize_cuts

# Define your cuts and stock lengths
cuts = [48.5, 24.25, 24.25]  # inches
stock_lengths = [8, 10, 12]   # feet

# Run the optimization
result = optimize_cuts(cuts, stock_lengths)
```

## Features

- Optimizser cutting patters to minimize waste
- Accounts for kerf (saw blade width)
- Handles multiple stock lengths
- Supports componsite pieces (cuts longer than stock length)
