import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_search_db_image():
    # Setup the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')

    # Title
    plt.text(0.5, 0.9, 'Search Optimized Database (Elasticsearch, Solr)',
             horizontalalignment='center', fontsize=16, fontweight='bold', color='#2c3e50')

    # Draw boxes
    # Client
    client = patches.FancyBboxPatch((0.1, 0.4), 0.15, 0.15, boxstyle="round,pad=0.05", ec="blue", fc="#e0f7fa", lw=2)
    ax.add_patch(client)
    plt.text(0.175, 0.475, 'Client\n(Search\nQuery)', ha='center', va='center', fontsize=12, fontweight='bold')

    # API / Load Balancer
    api = patches.FancyBboxPatch((0.4, 0.4), 0.15, 0.15, boxstyle="round,pad=0.05", ec="green", fc="#e8f5e9", lw=2)
    ax.add_patch(api)
    plt.text(0.475, 0.475, 'Search\nAPI', ha='center', va='center', fontsize=12, fontweight='bold')

    # Search Cluster
    cluster = patches.Rectangle((0.7, 0.2), 0.25, 0.55, fill=True, color="#fff3e0", ec="#f57c00", lw=2)
    ax.add_patch(cluster)
    plt.text(0.825, 0.7, 'Search Cluster', ha='center', va='center', fontsize=14, fontweight='bold')

    # Nodes in cluster
    node1 = patches.Rectangle((0.725, 0.5), 0.2, 0.15, fill=True, color="#ffe0b2", ec="#f57c00", lw=1)
    ax.add_patch(node1)
    plt.text(0.825, 0.575, 'Node 1\n(Inverted Index)', ha='center', va='center', fontsize=10)

    node2 = patches.Rectangle((0.725, 0.25), 0.2, 0.15, fill=True, color="#ffe0b2", ec="#f57c00", lw=1)
    ax.add_patch(node2)
    plt.text(0.825, 0.325, 'Node 2\n(Inverted Index)', ha='center', va='center', fontsize=10)

    # Arrows
    ax.annotate('', xy=(0.4, 0.475), xytext=(0.25, 0.475), arrowprops=dict(arrowstyle="->", lw=2, color="gray"))
    ax.annotate('', xy=(0.7, 0.575), xytext=(0.55, 0.5), arrowprops=dict(arrowstyle="->", lw=2, color="gray"))
    ax.annotate('', xy=(0.7, 0.325), xytext=(0.55, 0.45), arrowprops=dict(arrowstyle="->", lw=2, color="gray"))

    # Features text
    features = [
        "• Inverted Index for fast lookups",
        "• Tokenization & Stemming",
        "• Distributed & Horizontally Scalable",
        "• Real-time aggregations"
    ]
    for i, feature in enumerate(features):
        plt.text(0.1, 0.2 - (i * 0.05), feature, fontsize=11, color='#34495e')

    plt.tight_layout()
    plt.savefig('search_optimised_db.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_key_tech_image():
    # Setup the figure
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('off')

    # Title
    plt.text(0.5, 0.95, 'System Design: Key Technologies',
             horizontalalignment='center', fontsize=18, fontweight='bold', color='#2c3e50')

    # Define tech boxes
    techs = [
        {"name": "API Gateway", "desc": "Entry point for clients, routing, auth", "pos": (0.1, 0.7), "color": "#e3f2fd", "edge": "#1565c0"},
        {"name": "Load Balancer", "desc": "Distributes traffic across servers", "pos": (0.5, 0.7), "color": "#e8f5e9", "edge": "#2e7d32"},
        {"name": "CDN", "desc": "Caches static content at edge locations", "pos": (0.1, 0.45), "color": "#fff3e0", "edge": "#ef6c00"},
        {"name": "Message Queue", "desc": "Asynchronous communication buffer", "pos": (0.5, 0.45), "color": "#f3e5f5", "edge": "#6a1b9a"},
        {"name": "Distributed Cache", "desc": "In-memory fast data access (Redis/Memcached)", "pos": (0.1, 0.2), "color": "#ffebee", "edge": "#c62828"},
        {"name": "Event Streams", "desc": "Real-time event processing (Kafka)", "pos": (0.5, 0.2), "color": "#e0f7fa", "edge": "#00838f"},
    ]

    for tech in techs:
        x, y = tech["pos"]
        # Box
        box = patches.FancyBboxPatch((x, y), 0.35, 0.15, boxstyle="round,pad=0.02", ec=tech["edge"], fc=tech["color"], lw=2)
        ax.add_patch(box)
        # Title
        plt.text(x + 0.175, y + 0.1, tech["name"], ha='center', va='center', fontsize=14, fontweight='bold', color='#212121')
        # Description
        plt.text(x + 0.175, y + 0.05, tech["desc"], ha='center', va='center', fontsize=10, color='#424242', wrap=True)

    plt.tight_layout()
    plt.savefig('key_technologies.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating images...")
    create_search_db_image()
    create_key_tech_image()
    print("Images generated successfully!")
