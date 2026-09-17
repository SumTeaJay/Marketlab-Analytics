import pandas as pd
from app import generate_markets, prepare_markets, analyze_markets

def main():
    generate_markets()
    prepare_markets()
    analyze_markets()
    
if __name__ == "__main__":
    main()