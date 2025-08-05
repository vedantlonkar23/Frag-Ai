#!/usr/bin/env python3
"""
Test script to verify all imports work correctly
"""

def test_imports():
    print("Testing imports...")
    
    try:
        import streamlit as st
        print("✓ streamlit imported successfully")
    except ImportError as e:
        print(f"✗ streamlit import failed: {e}")
        return False
    
    try:
        import pandas as pd
        print("✓ pandas imported successfully")
    except ImportError as e:
        print(f"✗ pandas import failed: {e}")
        return False
    
    try:
        import numpy as np
        print("✓ numpy imported successfully")
    except ImportError as e:
        print(f"✗ numpy import failed: {e}")
        return False
    
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        print("✓ scikit-learn imported successfully")
    except ImportError as e:
        print(f"✗ scikit-learn import failed: {e}")
        return False
    
    try:
        import matplotlib.pyplot as plt
        print("✓ matplotlib imported successfully")
    except ImportError as e:
        print(f"✗ matplotlib import failed: {e}")
        return False
    
    try:
        import seaborn as sns
        print("✓ seaborn imported successfully")
    except ImportError as e:
        print(f"✗ seaborn import failed: {e}")
        return False
    
    # Test our custom modules
    try:
        from utils.recommendation import recommend_perfumes
        print("✓ recommendation module imported successfully")
    except ImportError as e:
        print(f"✗ recommendation module import failed: {e}")
        return False
    
    try:
        from utils.ingredient_suggestion import suggest_ingredients
        print("✓ ingredient_suggestion module imported successfully")
    except ImportError as e:
        print(f"✗ ingredient_suggestion module import failed: {e}")
        return False
    
    try:
        from components.general_section import show_general_section
        print("✓ general_section module imported successfully")
    except ImportError as e:
        print(f"✗ general_section module import failed: {e}")
        return False
    
    try:
        from components.maker_section import show_maker_section
        print("✓ maker_section module imported successfully")
    except ImportError as e:
        print(f"✗ maker_section module import failed: {e}")
        return False
    
    print("\nAll imports successful!")
    return True

if __name__ == "__main__":
    test_imports() 