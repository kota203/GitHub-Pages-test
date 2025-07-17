import plotly.graph_objects as go
import plotly.io as pio

# This script generates a single, self-contained, clickable HTML file that
# features an interactive, zooming sunburst chart for your Life Map.

# 1. Define the Hierarchical Data Structure
# ---
# These lists define the layers and connections of your diagram.
ids = [
    # Level 0 (Root)
    "HQ",
    # Level 1 (Main Categories)
    "Foundational", "Health", "Knowledge", "Finance", "Career", "Social", "Lifestyle",
    # Level 2 (Data Classes / Focus Points)
    "Goals", "Habits", "Projects", "Time", "Decisions", "Values", "Mindset", "Information", # Foundational
    "Exercise", "Nutrition", "Sleep", "Medical", "Wellness", "Relaxation",             # Health
    "Learning", "Reading", "Ideas", "Creativity",                                     # Knowledge
    "Budgets", "Investments", "Income", "Savings",                                    # Finance
    "Occupation", "Business", "Networking", "Development",                            # Career
    "Relationships", "Engagements", "Community",                                     # Social
    "Assets"                                                                          # Lifestyle
]

labels = [
    # Level 0 (Root)
    "🏆 Life<br>HQ",
    # Level 1 (Main Categories)
    "Foundational", "Health", "Knowledge", "Finance", "Career", "Social", "Lifestyle",
    # Level 2 (Data Classes / Focus Points)
    "Goals", "Habits", "Projects", "Time", "Decisions", "Values", "Mindset", "Information", # Foundational
    "Exercise", "Nutrition", "Sleep", "Medical", "Wellness", "Relaxation",             # Health
    "Learning", "Reading", "Ideas", "Creativity",                                     # Knowledge
    "Budgets", "Investments", "Income", "Savings",                                    # Finance
    "Occupation", "Business", "Networking", "Development",                            # Career
    "Relationships", "Engagements", "Community",                                     # Social
    "Home & Assets"                                                                   # Lifestyle
]

parents = [
    # Level 0 (Root)
    "",
    # Level 1 (Main Categories)
    "HQ", "HQ", "HQ", "HQ", "HQ", "HQ", "HQ",
    # Level 2 (Data Classes)
    "Foundational", "Foundational", "Foundational", "Foundational", "Foundational", "Foundational", "Foundational", "Foundational",
    "Health", "Health", "Health", "Health", "Health", "Health",
    "Knowledge", "Knowledge", "Knowledge", "Knowledge",
    "Finance", "Finance", "Finance", "Finance",
    "Career", "Career", "Career", "Career",
    "Social", "Social", "Social",
    "Lifestyle"
]

# 2. Add Your URLs Here
# IMPORTANT: Replace the "#" placeholders with your actual URLs.
# ---
notion_urls = [
    # Level 0
    "#",  # URL for the main HQ page
    # Level 1
    "https://www.notion.so/your-page-link",  # Foundational
    "https://www.notion.so/your-page-link",  # Health
    "https://www.notion.so/your-page-link",  # Knowledge
    "https://www.notion.so/your-page-link",  # Finance
    "https://www.notion.so/your-page-link",  # Career
    "https://www.notion.so/your-page-link",  # Social
    "https://www.notion.so/your-page-link",  # Lifestyle
    # Level 2 - You would continue to fill these in for every single item
    "#", "#", "#", "#", "#", "#", "#", "#",  # Foundational children
    "#", "#", "#", "#", "#", "#",             # Health children
    "#", "#", "#", "#",                        # Knowledge children
    "#", "#", "#", "#",                        # Finance children
    "#", "#", "#", "#",                        # Career children
    "#", "#", "#",                           # Social children
    "#"                                        # Lifestyle children
]


# 3. Create the Plotly Figure
# ---
# The go.Sunburst object automatically handles the zooming "move" animation on click.
fig = go.Figure(go.Sunburst(
    ids=ids,
    labels=labels,
    parents=parents,
    customdata=notion_urls,  # This links the URLs to each chart segment
    hovertemplate='<b>%{label}</b><br>Click to zoom or open link<extra></extra>',
    root_color="lightgrey"
))

fig.update_layout(
    margin=dict(t=50, l=20, r=20, b=20),
    title_text="Life Management HQ",
    title_font_size=24,
    font_family="Arial, sans-serif"
)

# 4. Define JavaScript for Clickable Links
# ---
# This script injects JavaScript into the HTML file to handle opening URLs.
# The sunburst's default click action is to zoom. This script adds a
# secondary action to open a link in a new tab.
js_click_handler = """
var plot_div = document.getElementsByClassName('plotly-graph-div')[0];
var a_element = document.createElement('a');
plot_div.on('plotly_click', function(data){
    var url = data.points[0].customdata;
    if (url && url !== '#') {
        a_element.href = url;
        a_element.target = '_blank'; // Ensures the link opens in a new tab
        a_element.click();
    }
});
"""

# 5. Generate and Save the HTML File
# ---
pio.write_html(
    fig,
    file="life_map_clickable.html",
    post_script=[js_click_handler],
    full_html=True,
    include_plotlyjs='cdn'
)

print("Successfully generated 'life_map_clickable.html'.")
print("Open this file in your web browser to see the interactive diagram.")
