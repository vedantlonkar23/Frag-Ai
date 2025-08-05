# ingredient_suggestion.py
import pandas as pd
from collections import Counter

def suggest_ingredients(primary_note, df):
    # Ensure correct column names and handle missing columns
    existing_columns = [col for col in ['Top', 'Middle', 'Base'] if col in df.columns]

    if not existing_columns:
        raise KeyError("Missing required columns (Top, Middle, Base) in the dataset.")

    # Combine all notes for analysis
    all_notes = pd.concat([df[col] for col in existing_columns]).dropna().str.split(', ').explode()
    
    # Filter for perfumes containing the primary note
    relevant_perfumes = df[df[existing_columns].apply(lambda x: primary_note in ', '.join(x.dropna()), axis=1)]

    # Extract notes from relevant perfumes
    related_notes = pd.concat([relevant_perfumes[col] for col in existing_columns]).dropna().str.split(', ').explode()

    # Count most common notes excluding the primary note
    note_counts = Counter(related_notes)
    note_counts.pop(primary_note, None)

    # Return top 5 complementary notes
    return pd.DataFrame(note_counts.most_common(5), columns=['Note', 'Count'])
