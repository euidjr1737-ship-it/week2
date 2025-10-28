# Generative Abstract Poster
# Concepts: randomness, lists, loops, functions, matplotlib

import random
import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 🎨 CSV 팔레트 불러오기
PALETTE_FILE = "palette.csv"

def read_palette():
    return pd.read_csv(PALETTE_FILE)

def load_csv_palette():
    df = read_palette()
    return [(row.r, row.g, row.b) for row in df.itertuples()]

palette_csv = load_csv_palette()

def star(center=(0.5, 0.5), r=0.3, points=5, wobble=0.1):
    """generate a wobbly star shape"""
    angles = np.linspace(0, 2*math.pi, points * 2, endpoint=False)
    radii = []
    for i in range(points * 2):
        # 홀수 번째는 안쪽, 짝수 번째는 바깥쪽
        if i % 2 == 0:
            radii.append(r * (1 + wobble*(random.random()-0.5)))
        else:
            radii.append(r * 0.4 * (1 + wobble*(random.random()-0.5)))
    radii = np.array(radii)
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

# 🎲 랜덤 시드 설정
random.seed()
plt.figure(figsize=(7,10))
plt.axis('off')

# 🎨 배경
plt.gca().set_facecolor((0.98,0.98,0.97))

# 🖌️ 별 여러 개 생성
n_layers = 8
for i in range(n_layers):
    cx, cy = random.random(), random.random()
    rr = random.uniform(0.15, 0.45)
    points = random.choice([5, 6, 7, 8])
    wobble = random.uniform(0.05, 0.25)
    x, y = star(center=(cx, cy), r=rr, points=points, wobble=wobble)
    color = random.choice(palette_csv)
    alpha = random.uniform(0.3, 0.6)
    plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0))

# 🧾 텍스트 라벨
plt.text(0.05, 0.95, "Generative Poster", fontsize=18, weight='bold', transform=plt.gca().transAxes)
plt.text(0.05, 0.91, "Week 2 • Arts & Advanced Big Data", fontsize=11, transform=plt.gca().transAxes)

plt.xlim(0,1); plt.ylim(0,1)
plt.show()
