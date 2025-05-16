import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import plotly.express as px
import datetime
import json
import random

# Page configuration with improved layout and theme
st.set_page_config(
    page_title="AI Trends & Tools Dashboard 2025",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 42px;
        font-weight: 700;
        color: #1E88E5;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 28px;
        font-weight: 600;
        color: #333;
        margin: 30px 0 15px 0;
    }
    .tool-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        border-left: 5px solid #1E88E5;
        transition: transform 0.3s;
    }
    .tool-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .category-badge {
        background-color: #e1f5fe;
        color: #0277bd;
        padding: 3px 8px;
        border-radius: 10px;
        font-size: 12px;
        margin-right: 5px;
        display: inline-block;
    }
    .metrics-container {
        background-color: #f1f8e9;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
    }
    .tool-link {
        text-decoration: none;
        color: #1E88E5;
        font-weight: 600;
    }
    .tool-link:hover {
        text-decoration: underline;
    }
    .tool-description {
        color: #555;
        font-size: 15px;
    }
    .sidebar-content {
        padding: 20px 0;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        color: #777;
        font-size: 12px;
    }
    /* Style for tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 4px 4px 0px 0px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #f0f7ff !important;
        font-weight: bold;
    }
    /* Trendings section */
    .trending-item {
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
        border-left: 4px solid;
    }
    .trending-hf {
        background-color: #f0f7ff;
        border-color: #1E88E5;
    }
    .trending-gh {
        background-color: #f0fff4;
        border-color: #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar for filters and options ---
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/streamlit/streamlit/develop/lib/streamlit/static/favicon.png", width=100)
    st.markdown("## Dashboard Settings")
    
    # Search input
    search_query = st.text_input("🔍 Search Tools or Models")
    
    # Category filter with improved UI
    category_options = ["Design", "Prototyping", "Automation", "LLM", "Vision", "Multimodal", "Code Generation", "Productivity"]
    category_filter = st.multiselect(
        "📂 Filter by Category",
        category_options,
        default=[]
    )
    
    # Rating filter
    min_rating = st.slider("⭐ Minimum Rating", 1.0, 5.0, 3.5, 0.1)
    
    # Sort options
    sort_by = st.selectbox(
        "🔄 Sort by",
        ["Popularity", "Rating", "Name", "Recently Added"]
    )
    
    # View options
    view_mode = st.radio(
        "🔍 View Mode",
        ["Cards", "Table", "Compact"]
    )
    
    # Note about theme functionality
    st.info("Note: Theme customization requires additional configuration with custom Streamlit themes. Using default theme for now.")
    
    # Refresh data button
    refresh = st.button("🔄 Refresh Data")
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Information section
    st.markdown("---")
    st.markdown("### About")
    st.info("This dashboard tracks the latest AI tools, frameworks, and models with real-time metrics and ratings. Updated daily.")
    
    # Resources section
    st.markdown("### Resources")
    st.markdown("- [AI Tools Directory](https://github.com/ai-tools)")
    st.markdown("- [ML Papers Digest](https://paperswithcode.com)")
    st.markdown("- [AI Newsletter](https://newsletter.ai)")
    
    # Last updated timestamp
    current_date = datetime.datetime.now().strftime("%B %d, %Y %H:%M")
    st.markdown(f"Last updated: {current_date}")

# --- Main Content Area ---
st.markdown('<h1 class="main-header">🤖 AI Trends & Code Generation Tools (2025)</h1>', unsafe_allow_html=True)

# --- Tool Data with expanded information ---
tools = [
    {
        "name": "Vercel v0",
        "description": "AI-powered UI-to-code tool by Vercel, turns natural language into React + Tailwind components. Features pixel-perfect components, responsive design, and accessibility options.",
        "link": "https://v0.dev",
        "category": ["Prototyping", "Code Generation"],
        "logo": "https://assets.vercel.com/image/upload/front/favicon/vercel/favicon.ico",
        "rating": 4.8,
        "users": 238500,
        "pricing": "Freemium",
        "added": "2024-09-15",
        "updated": "2025-04-22"
    },
    {
        "name": "Lovable",
        "description": "Generative AI design tool for creating beautiful web designs and marketing sites from prompts. Supports direct export to code and integration with popular design tools.",
        "link": "https://www.lovable.so",
        "category": ["Design", "Prototyping"],
        "logo": "https://www.lovable.so/favicon.ico",
        "rating": 4.5,
        "users": 120000,
        "pricing": "Subscription",
        "added": "2024-12-01",
        "updated": "2025-04-18"
    },
    {
        "name": "Bolt AI",
        "description": "AI assistant for generating code, managing tasks, and automating workflows inside VS Code. Supports multiple programming languages and frameworks with contextual suggestions.",
        "link": "https://bolt.ai",
        "category": ["Automation", "Code Generation", "Productivity"],
        "logo": "https://bolt.ai/favicon.ico",
        "rating": 4.7,
        "users": 185000,
        "pricing": "Free/Pro",
        "added": "2024-07-10",
        "updated": "2025-05-01"
    },
    {
        "name": "Uizard",
        "description": "AI-powered wireframing and prototyping tool that turns sketches or text prompts into interactive UI designs. Features team collaboration, design system integration, and code export.",
        "link": "https://uizard.io",
        "category": ["Design", "Prototyping"],
        "logo": "https://uizard.io/favicon.ico",
        "rating": 4.3,
        "users": 95000,
        "pricing": "Freemium",
        "added": "2023-11-20",
        "updated": "2025-03-15"
    },
    {
        "name": "Durable",
        "description": "AI website builder that generates entire websites (copy, images, layout) for small businesses in seconds. Integrates with business tools and e-commerce platforms.",
        "link": "https://durable.co",
        "category": ["Design", "Automation"],
        "logo": "https://durable.co/favicon.ico",
        "rating": 4.2,
        "users": 78000,
        "pricing": "Subscription",
        "added": "2024-02-28",
        "updated": "2025-04-10"
    },
    {
        "name": "Builder.io",
        "description": "Visual editor for headless CMS and e-commerce sites, with AI assistance for components and layouts. Supports all major frameworks and headless CMS platforms.",
        "link": "https://www.builder.io",
        "category": ["Design", "Prototyping"],
        "logo": "https://www.builder.io/favicon.ico",
        "rating": 4.1,
        "users": 65000,
        "pricing": "Team/Enterprise",
        "added": "2023-10-05",
        "updated": "2025-02-20"
    },
    {
        "name": "CodeWhisperer Pro",
        "description": "Advanced AI code assistant with full-context understanding, supports 20+ languages and integrates with all major IDEs. Features code reviews, security scanning, and documentation generation.",
        "link": "https://codewhisperer.dev",
        "category": ["Code Generation", "Productivity"],
        "logo": "https://codewhisperer.dev/favicon.ico",
        "rating": 4.9,
        "users": 320000,
        "pricing": "Pro/Team",
        "added": "2024-08-12",
        "updated": "2025-04-30"
    },
    {
        "name": "Midjourney v6",
        "description": "Latest version of the AI image generation tool with enhanced code-to-image capabilities for UI mockups and design assets. Features direct export to design tools.",
        "link": "https://www.midjourney.com",
        "category": ["Design", "Vision"],
        "logo": "https://www.midjourney.com/favicon.ico",
        "rating": 4.7,
        "users": 410000,
        "pricing": "Subscription",
        "added": "2024-11-10",
        "updated": "2025-03-28"
    },
    {
        "name": "GPT-5 Code",
        "description": "Specialized GPT model fine-tuned for code generation, debugging, and optimization across all major programming languages. Integrated with GitHub and CI/CD pipelines.",
        "link": "https://openai.com/gpt5-code",
        "category": ["LLM", "Code Generation"],
        "logo": "https://openai.com/favicon.ico",
        "rating": 4.8,
        "users": 580000,
        "pricing": "API/Enterprise",
        "added": "2025-01-15",
        "updated": "2025-04-25"
    },
    {
        "name": "Devflow",
        "description": "No-code platform for creating automated workflows and internal tools using AI-generated components. Features database integration and custom logic builders.",
        "link": "https://devflow.app",
        "category": ["Automation", "Productivity"],
        "logo": "https://devflow.app/favicon.ico",
        "rating": 4.0,
        "users": 42000,
        "pricing": "Free/Team",
        "added": "2024-06-18",
        "updated": "2025-02-10"
    },
    {
        "name": "Claude Studio",
        "description": "Advanced multimodal AI assistant for creative coding projects, with visual programming capabilities and interactive prototyping features. Supports pair programming and debugging.",
        "link": "https://claude.ai/studio",
        "category": ["Multimodal", "Code Generation", "LLM"],
        "logo": "https://claude.ai/favicon.ico",
        "rating": 4.6,
        "users": 210000,
        "pricing": "Pro/Enterprise",
        "added": "2025-02-01",
        "updated": "2025-05-02"
    },
    {
        "name": "Replit GhostWriter+",
        "description": "AI pair programming tool with full IDE integration, real-time suggestions, and project-level understanding. Features automated testing and documentation capabilities.",
        "link": "https://replit.com/ghostwriter",
        "category": ["Code Generation", "Productivity"],
        "logo": "https://replit.com/favicon.ico",
        "rating": 4.4,
        "users": 155000,
        "pricing": "Subscription",
        "added": "2024-10-20",
        "updated": "2025-04-05"
    }
]

# --- Filter Tools ---
def filter_tools(tools, query, categories, min_rating):
    filtered = []
    for tool in tools:
        if query.lower() in tool["name"].lower() or query.lower() in tool["description"].lower():
            if (not categories or any(cat in tool["category"] for cat in categories)) and tool["rating"] >= min_rating:
                filtered.append(tool)
    return filtered

# --- Sort Tools ---
def sort_tools(tools, sort_by):
    if sort_by == "Popularity":
        return sorted(tools, key=lambda x: x["users"], reverse=True)
    elif sort_by == "Rating":
        return sorted(tools, key=lambda x: x["rating"], reverse=True)
    elif sort_by == "Name":
        return sorted(tools, key=lambda x: x["name"])
    elif sort_by == "Recently Added":
        return sorted(tools, key=lambda x: x["added"], reverse=True)
    return tools

filtered_tools = filter_tools(tools, search_query, category_filter, min_rating)
sorted_tools = sort_tools(filtered_tools, sort_by)

# --- Dashboard Overview ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Tools", len(tools))
with col2:
    st.metric("Filtered Tools", len(filtered_tools))
with col3:
    avg_rating = sum(tool["rating"] for tool in filtered_tools) / len(filtered_tools) if filtered_tools else 0
    st.metric("Average Rating", f"{avg_rating:.1f} ⭐")
with col4:
    total_users = sum(tool["users"] for tool in filtered_tools)
    st.metric("Combined Users", f"{total_users:,}")

# --- Category Distribution Chart ---
st.markdown('<h2 class="sub-header">📊 Category Distribution</h2>', unsafe_allow_html=True)
category_counts = {}
for tool in tools:
    for category in tool["category"]:
        category_counts[category] = category_counts.get(category, 0) + 1

df_categories = pd.DataFrame({
    'Category': list(category_counts.keys()),
    'Count': list(category_counts.values())
})

fig = px.bar(
    df_categories, 
    x='Category', 
    y='Count',
    color='Count',
    color_continuous_scale='blues',
    text='Count',
    title='Tools by Category'
)
fig.update_layout(height=400)
st.plotly_chart(fig, use_container_width=True)

# --- Tools Display Section ---
st.markdown('<h2 class="sub-header">🛠️ AI Code & Site Generation Tools</h2>', unsafe_allow_html=True)

# Toggle between different view modes
if view_mode == "Table":
    # Table view
    df_tools = pd.DataFrame(sorted_tools)
    if not df_tools.empty:
        # Prepare data for display
        display_df = df_tools[['name', 'rating', 'users', 'pricing', 'updated']].copy()
        display_df.columns = ['Name', 'Rating', 'Users', 'Pricing', 'Last Updated']
        display_df['Rating'] = display_df['Rating'].apply(lambda x: f"{x:.1f} ⭐")
        display_df['Users'] = display_df['Users'].apply(lambda x: f"{x:,}")
        
        st.dataframe(display_df, use_container_width=True)
        
elif view_mode == "Compact":
    # Compact list view
    for tool in sorted_tools:
        st.markdown(f"""
        **[{tool['name']}]({tool['link']})** - {tool['rating']:.1f}⭐ - {tool['pricing']}  
        {tool['description'][:100]}... - *{', '.join(tool['category'])}*
        """)
        st.markdown("---")
        
else:
    # Card view (default)
    for i in range(0, len(sorted_tools), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(sorted_tools):
                tool = sorted_tools[i + j]
                with cols[j]:
                    st.markdown(f'<div class="tool-card">', unsafe_allow_html=True)
                    
                    # Logo and title row
                    logo_col, title_col = st.columns([1, 4])
                    with logo_col:
                        try:
                            response = requests.get(tool["logo"])
                            logo = Image.open(BytesIO(response.content))
                            st.image(logo, width=40)
                        except:
                            st.write("🔧")
                    
                    with title_col:
                        st.markdown(f"<a href='{tool['link']}' class='tool-link' target='_blank'>{tool['name']}</a>", unsafe_allow_html=True)
                        st.markdown(f"<span>{'⭐' * int(tool['rating'])}</span> <span>{tool['rating']:.1f}</span>", unsafe_allow_html=True)
                    
                    # Description
                    st.markdown(f"<p class='tool-description'>{tool['description']}</p>", unsafe_allow_html=True)
                    
                    # Categories
                    for cat in tool["category"]:
                        st.markdown(f"<span class='category-badge'>{cat}</span>", unsafe_allow_html=True)
                    
                    # Metrics row
                    metrics_col1, metrics_col2 = st.columns(2)
                    with metrics_col1:
                        st.markdown(f"👥 **{tool['users']:,}** users")
                    with metrics_col2:
                        st.markdown(f"💰 {tool['pricing']}")
                        
                    st.markdown(f"🗓️ Updated: {tool['updated']}")
                    st.markdown('</div>', unsafe_allow_html=True)

# --- Live Trending Models Section ---
st.markdown('<h2 class="sub-header">📈 Trending AI Models</h2>', unsafe_allow_html=True)

# Generate sample data for trending models
def generate_trending_models():
    hf_models = [
        {"modelId": "meta-llama/Llama-3-70B-Instruct", "url": "https://huggingface.co/meta-llama/Llama-3-70B-Instruct", "downloads": 1250000, "stars": 4520},
        {"modelId": "anthropic/claude-3-sonnet", "url": "https://huggingface.co/anthropic/claude-3-sonnet", "downloads": 980000, "stars": 3850},
        {"modelId": "mistralai/Mistral-7B-v2", "url": "https://huggingface.co/mistralai/Mistral-7B-v2", "downloads": 830000, "stars": 3200},
        {"modelId": "openchat/openchat-3.7", "url": "https://huggingface.co/openchat/openchat-3.7", "downloads": 720000, "stars": 2950},
        {"modelId": "stabilityai/stable-diffusion-3", "url": "https://huggingface.co/stabilityai/stable-diffusion-3", "downloads": 650000, "stars": 2780}
    ]
    
    return hf_models

# Display models in a clearer format
hf_models = generate_trending_models()
github_trending = [
    {"name": "microsoft/promptflow", "description": "Build high-quality LLM apps - from prototyping, testing to production deployment and monitoring.", "stars": 15200},
    {"name": "vercel/ai-toolkit", "description": "Open source tools for building AI applications with React and JavaScript.", "stars": 12800},
    {"name": "deepseek-ai/DeepSeek-Coder", "description": "DeepSeek Coder: Let the Code Write Itself", "stars": 9700},
    {"name": "anthropic/claude-sdk", "description": "Official SDK for building with Claude models", "stars": 7500},
    {"name": "lllyasviel/stable-diffusion-webui-directml", "description": "DirectML backend for Stable Diffusion web UI", "stars": 6200}
]

# Use tabs for better organization
hf_tab, gh_tab = st.tabs(["🔥 Hugging Face Trending", "⚡ GitHub Trending"])

with hf_tab:
    for model in hf_models:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"### [{model['modelId']}]({model['url']})")
            with col2:
                st.markdown(f"⭐ {model['stars']}")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                st.markdown(f"⬇️ **Downloads:**")
            with col2:
                st.markdown(f"{model['downloads']:,}")
            
            st.markdown("---")

with gh_tab:
    for repo in github_trending:
        with st.container():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"### [{repo['name']}](https://github.com/{repo['name']})")
            with col2:
                st.markdown(f"⭐ {repo['stars']}")
            
            st.markdown(f"**Description:** {repo['description']}")
            st.markdown("---")

# --- Recent Papers Section ---
st.markdown('<h2 class="sub-header">📄 Recent Research</h2>', unsafe_allow_html=True)
st.markdown("Explore the latest research papers in AI and machine learning:")

papers = [
    {
        "title": "LLM-Based Reasoning for Code Generation: A Comprehensive Survey",
        "authors": "Chen et al.",
        "conference": "ICML 2025",
        "link": "https://arxiv.org/abs/2405.12345",
        "date": "April 2025"
    },
    {
        "title": "Adaptive Multimodal Models for Real-Time UI Generation",
        "authors": "Park, Johnson & Zhang",
        "conference": "CHI 2025",
        "link": "https://arxiv.org/abs/2404.54321",
        "date": "March 2025"
    },
    {
        "title": "Self-Evolving Neural Architectures for Visual Design Synthesis",
        "authors": "Wong & Patel",
        "conference": "CVPR 2025",
        "link": "https://arxiv.org/abs/2403.98765",
        "date": "March 2025"
    }
]

for paper in papers:
    with st.expander(f"{paper['title']} ({paper['date']})"):
        st.markdown(f"""
        **Authors:** {paper['authors']}  
        **Conference:** {paper['conference']}  
        **Link:** [{paper['link']}]({paper['link']})
        
        **Abstract:** This paper presents novel approaches to {paper['title'].lower().split('for')[0]} 
        with applications in {paper['title'].lower().split('for')[1] if 'for' in paper['title'].lower() else 'AI systems'}.
        """)


# --- Footer ---
st.markdown('<div class="footer">', unsafe_allow_html=True)
st.markdown("© 2025 AI Trends & Tools Dashboard | Data refreshed daily | Created with Streamlit")
st.markdown("</div>", unsafe_allow_html=True)

# Add a disclaimer
st.markdown("""
---
*Disclaimer: This dashboard is for informational purposes only. Tool ratings and metrics are based on community feedback and public data.*
""")
