#!/usr/bin/env python3
from src.optimizer import optimize_cuts

def main():
    cuts = [
        3.25, 3.25, 3.25, 3.25, 3.375, 52, 3.5, 56.5, 55.75, 9, 9, 7, 7, 24.375,
        4.75, 6.74, 8.25, 8.5, 8.5, 11, 11, 11.75, 12.5, 12.625, 14.25, 17.25,
        20, 20.25, 20.625, 20.75, 21.125, 21.825, 24.25, 24.75, 25.5, 25.5,
        25.625, 25.625, 25.75, 27.75, 27.75, 29.125, 29.5, 37, 38.25, 38.75,
        38.75, 42.625, 46.75, 48.25, 49.625, 50, 53.25, 58, 58.75, 68, 68.25,
        77, 90, 94.25, 127.75, 127.75, 143, 150.625, 226
    ]
    
    stock_lengths = [8, 10, 12]  # Available stock lengths in feet
    
    # Run optimization with default kerf of 0.125 inches
    result = optimize_cuts(cuts, stock_lengths)

if __name__ == "__main__":
    main()
