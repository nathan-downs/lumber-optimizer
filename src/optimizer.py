#!/usr/bin/env python3
from typing import List, Tuple

def find_best_fit(remaining_space, available_cuts, kerf=0.125):
    best_combo = []
    best_remaining = remaining_space
    
    for i, cut in enumerate(available_cuts):
        current_space_needed = cut + kerf  # Add kerf to the cut
        if current_space_needed <= remaining_space:
            current_combo = [cut]
            current_remaining = remaining_space - current_space_needed
            
            for next_cut in available_cuts[i+1:]:
                next_space_needed = next_cut + kerf
                if next_space_needed <= current_remaining:
                    current_combo.append(next_cut)
                    current_remaining -= next_space_needed
            
            if current_remaining < best_remaining:
                best_remaining = current_remaining
                best_combo = current_combo
    
    return best_combo

def optimize_cuts(cuts, stock_lengths, kerf=0.125):
    print("Starting optimization...")
    max_length = max(stock_lengths) * 12
    remaining_cuts = []
    cutting_layouts = {length: [] for length in stock_lengths}
    total_waste = {length: 0 for length in stock_lengths}
    
    symbols = ['*', '^', '#', '@', '&', '+', '=', '~']
    symbol_index = 0
    composite_pieces = []  # List of tuples (original_cut, pieces, symbol)
    
    total_linear_inches = sum(cuts)
    
    # First pass - identify composite pieces
    for cut in sorted(cuts, reverse=True):
        if cut > max_length:
            full_pieces = int(cut // max_length)
            remainder = cut % max_length
            pieces = [max_length] * full_pieces
            if remainder > 0:
                pieces.append(remainder)
            
            composite_pieces.append((cut, pieces, symbols[symbol_index]))
            symbol_index += 1
            
            # Add to layouts/remaining cuts
            for _ in range(full_pieces):
                cutting_layouts[12].append([max_length])
            if remainder > 0:
                remaining_cuts.append(remainder)
        else:
            remaining_cuts.append(cut)
    
    # Now optimize remaining cuts to minimize waste
    remaining_cuts.sort(reverse=True)
    while remaining_cuts:
        best_stock = None
        best_combo = []
        
        for length in sorted(stock_lengths, reverse=True):
            length_inches = length * 12
            combo = find_best_fit(length_inches, remaining_cuts, kerf)
            if combo and (not best_combo or len(combo) > len(best_combo)):
                best_stock = length
                best_combo = combo
        
        if best_combo:
            cutting_layouts[best_stock].append(best_combo)
            total_cuts_with_kerf = sum(best_combo) + (len(best_combo) * kerf)
            waste = best_stock * 12 - total_cuts_with_kerf
            total_waste[best_stock] += waste
            for cut in best_combo:
                remaining_cuts.remove(cut)
        else:
            break
    
    print("\nCutting layouts for each length (including 1/8\" kerf loss per cut):")
    grand_total_waste = 0
    total_stock_inches = 0
    total_kerfs = 0
    total_used_inches = 0
    
    for length, layouts in cutting_layouts.items():
        if layouts:
            print(f"\n{length}' pieces:")
            board_length_inches = length * 12
            total_stock_inches += board_length_inches * len(layouts)
            
            for i, cuts in enumerate(layouts, 1):
                formatted_cuts = []
                for cut in cuts:
                    # Find if this cut is part of a composite piece
                    for original, pieces, symbol in composite_pieces:
                        if cut in pieces:
                            pieces.remove(cut)  # Remove to prevent reuse
                            formatted_cuts.append(f"{symbol}{cut}{symbol}")
                            break
                    else:
                        formatted_cuts.append(str(cut))
                
                kerfs = len(cuts) * kerf
                total_kerfs += kerfs
                total_used_inches += sum(cuts)
                waste = board_length_inches - (sum(cuts) + kerfs)
                print(f"  Board {i}: {formatted_cuts}")
                print(f"    Kerfs: {kerfs:.3f}\", Waste: {waste:.3f}\"")

            print(f"  Total {length}' pieces needed: {len(layouts)}")
            print(f"  Total waste for {length}' pieces: {total_waste[length]:.3f}\"")

    grand_total_waste = total_stock_inches - total_used_inches - total_kerfs
    waste_percentage = (grand_total_waste / total_stock_inches) * 100
    
    print(f"\nSummary:")
    print(f"Total linear footage needed: {total_linear_inches/12:.2f}'")
    print(f"Total stock footage used: {total_stock_inches/12:.2f}'")
    print(f"Total kerf loss: {total_kerfs:.2f}\" ({total_kerfs/12:.2f}')")
    print(f"Total waste (excluding kerfs): {grand_total_waste:.2f}\" ({grand_total_waste/12:.2f}')")
    print(f"Waste percentage: {waste_percentage:.1f}%")
    
    return cutting_layouts
