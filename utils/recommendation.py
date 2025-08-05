import pandas as pd
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    print("Warning: scikit-learn not available. Recommendation functionality will be limited.")

def recommend_perfumes(selected_perfume, df):
    if not SKLEARN_AVAILABLE:
        return pd.DataFrame({'Error': ['scikit-learn is required for recommendations']})
    
    try:
        # Combine all notes and accords to create a text representation for each fragrance
        df['combined_features'] = df[['Top', 'Middle', 'Base', 'mainaccord1', 'mainaccord2', 'mainaccord3']].astype(str).agg(' '.join, axis=1)

        # Vectorize using TF-IDF
        vectorizer = TfidfVectorizer()
        feature_matrix = vectorizer.fit_transform(df['combined_features'])

        # Calculate cosine similarity
        similarity_matrix = cosine_similarity(feature_matrix)

        # Get index of the selected perfume
        selected_index = df[df['Perfume'] == selected_perfume].index[0]

        # Get similarity scores and sort
        similarity_scores = list(enumerate(similarity_matrix[selected_index]))
        similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

        # Get top 5 recommendations (excluding itself)
        recommended_indices = [i[0] for i in similarity_scores[1:6]]
        recommendations = df.iloc[recommended_indices][['Perfume', 'Brand', 'Top', 'Middle', 'Base']]

        return recommendations
    except Exception as e:
        return pd.DataFrame({'Error': [f'Recommendation failed: {str(e)}']})
