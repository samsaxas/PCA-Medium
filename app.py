import streamlit as st
import streamlit.components.v1 as components
import os

st.set_page_config(page_title="Dimensionality Reduction Dashboard", layout="wide")

st.title("📉 Dimensionality Reduction Visualization Dashboard")
st.markdown("""
Explore the PCA, t-SNE, and UMAP projections of the Human Activity Recognition dataset.
Each visualization is interactive — hover, zoom, and explore the clusters!
""")

# --- Helper to embed HTML file ---
def embed_plot(filename, height=600):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    components.html(html, height=height, scrolling=True)

# --- Tabs for each visualization ---
tab1, tab2, tab3 = st.tabs(["📊 PCA", "🌐 t-SNE", "🔍 UMAP"])

with tab1:
    st.subheader("Principal Component Analysis (PCA)")
    embed_plot(r"C:\Users\LENOVO\ML Blog\pca.html")

with tab2:
    st.subheader("t-distributed Stochastic Neighbor Embedding (t-SNE)")
    embed_plot(r"C:\Users\LENOVO\ML Blog\tSNE.html")

with tab3:
    st.subheader("Uniform Manifold Approximation and Projection (UMAP)")
    embed_plot(r"C:\Users\LENOVO\ML Blog\umap.html")
