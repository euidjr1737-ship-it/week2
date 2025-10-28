import streamlit as st
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import io

# Page config
st.set_page_config(page_title="Star Poster", page_icon="⭐", layout="wide")

st.title("⭐ Generative Star Poster")
st.markdown("**Week 2 • Arts & Advanced Big Data**")

# Sidebar
st.sidebar.header("Settings")
n_layers = st.sidebar.slider("Stars", 3, 20, 8)
wobble = st.sidebar.slider("Wobble", 0.01, 0.5, 0.15)
points = st.sidebar.slider("Points", 5, 9, 6)
seed = st.sidebar.slider("Seed", 0, 9999, 0)

# Palette
PALETTE = [(1.0, 0.6, 0.4), (1.0, 0.4, 0.3), (0.9, 0.5, 0.2), 
           (1.0, 0.7, 0.3), (0.95, 0.45, 0.35)]

def star(center=(0.5, 0.5), r=0.3, points=5, wobble=0.1):
    angles = np.linspace(0, 2*math.pi, points * 2, endpoint=False)
    radii = []
    for i in range(points * 2):
        if i % 2 == 0:
            radii.append(r * (1 + wobble*(random.random()-0.5)))
        else:
            radii.append(r * 0.4 * (1 + wobble*(random.random()-0.5)))
    radii = np.array(radii)
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

def draw_poster(n_layers, wobble, points, seed):
    random.seed(seed)
    np.random.seed(seed)
    
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.axis('off')
    ax.set_facecolor((0.98, 0.98, 0.97))

    for i in range(n_layers):
        cx, cy = random.random(), random.random()
        rr = random.uniform(0.15, 0.45)
        p = random.choice(range(points-1, points+2))
        x, y = star(center=(cx, cy), r=rr, points=p, wobble=wobble)
        color = random.choice(PALETTE)
        alpha = random.uniform(0.3, 0.6)
        ax.fill(x, y, color=color, alpha=alpha, edgecolor=(0, 0, 0, 0))

    ax.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', 
            transform=ax.transAxes)
    ax.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, 
            transform=ax.transAxes)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    return fig

# Generate and display
fig = draw_poster(n_layers, wobble, points, seed)
st.pyplot(fig)
plt.close(fig)

# Download
buf = io.BytesIO()
fig.savefig(buf, format='png', dpi=300, bbox_inches='tight')
buf.seek(0)
st.download_button("📥 Download", buf, f"poster_{seed}.png", "image/png")
