import pandas as pd
from app import generate_markets, prepare_markets, calculate_monopoly_and_pc

def main():
    generate_markets()
    prepare_markets()
    calculate_monopoly_and_pc()
    
if __name__ == "__main__":
    main()