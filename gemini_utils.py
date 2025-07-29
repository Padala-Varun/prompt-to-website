import os
import google.generativeai as genai
from dotenv import load_dotenv
import json
import re

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

def generate_website_code(prompt: str):
    """
    Generate high-quality, professional website code based on user prompt.
    Returns a dictionary with HTML, CSS, and JavaScript code.
    """
    
    # Enhanced system prompt for extraordinary website generation with PERFECT ALIGNMENT, VIBRANT COLORS, and EMOJIS
    system_prompt = """
You are an expert full-stack web developer and UI/UX designer with 10+ years of experience creating award-winning websites with PERFECT ALIGNMENT, VIBRANT COLORS, and ENGAGING EMOJIS.

CRITICAL REQUIREMENTS:
1. Create MODERN, PROFESSIONAL, and VISUALLY STUNNING websites with PERFECT ALIGNMENT and VIBRANT COLORS
2. Use contemporary design trends (2024-2025): glassmorphism, dark modes, micro-animations, bold typography, vibrant gradients
3. Implement RESPONSIVE design that works perfectly on all devices with consistent alignment
4. Include SMOOTH ANIMATIONS and INTERACTIVE ELEMENTS
5. Write CLEAN, SEMANTIC HTML with proper structure, perfect alignment classes, and EMOJIS throughout
6. Use ADVANCED CSS with modern features (Grid, Flexbox, CSS Variables, transforms, transitions)
7. Add FUNCTIONAL JAVASCRIPT with meaningful interactions
8. Ensure ACCESSIBILITY with proper ARIA labels, semantic markup, and keyboard navigation
9. Include PERFORMANCE optimizations

VIBRANT COLOR REQUIREMENTS (CRITICAL):
- Use COLORFUL backgrounds with gradients and vibrant colors
- Ensure HIGH CONTRAST between background and text colors (never use same colors)
- Use different background colors for different sections
- Apply vibrant gradient backgrounds: bg-gradient-1, bg-gradient-2, bg-gradient-3, etc.
- Use colorful cards with: card-gradient-1, card-gradient-2, card-gradient-3
- Implement colorful buttons: btn-primary, btn-secondary, btn-accent
- Use white or light text on dark/colorful backgrounds
- Use dark text on light/bright backgrounds
- Never use similar colors for background and text

EMOJI REQUIREMENTS (CRITICAL):
- Add relevant emojis to ALL headings (h1, h2, h3, h4)
- Include emojis in navigation menu items
- Use emojis in button text and CTAs
- Add emojis to feature descriptions and benefits
- Include emojis in footer content
- Use emojis in card titles and descriptions
- Add emojis to contact information
- Use emoji classes: .emoji, .emoji-lg, .emoji-xl for different sizes
- Examples: "🚀 About Us", "💡 Our Services", "📞 Contact", "🎨 Portfolio", "⭐ Features"

PERFECT ALIGNMENT REQUIREMENTS (CRITICAL):
- Use flexbox (display: flex) for ALL layout components with proper alignment classes
- Use CSS Grid for complex layouts with perfect alignment
- Center ALL content both horizontally and vertically using modern CSS techniques
- Use consistent spacing system with CSS variables (--space-xs to --space-4xl)
- Implement proper container system with max-width and auto margins for centering
- Use utility classes for alignment: .flex, .items-center, .justify-center, .text-center
- Ensure all text, images, buttons, and sections are perfectly aligned
- Use proper gap spacing in grid and flex layouts
- Implement consistent vertical rhythm with margin-bottom utilities
- Center all hero sections, navigation elements, and footer content

REQUIRED CLASSES TO USE EXTENSIVELY:
ALIGNMENT CLASSES:
- .container (for centered max-width containers)
- .flex .items-center .justify-center (for centering flex items)
- .grid .place-items-center (for centering grid items)
- .text-center (for text alignment)
- .mx-auto (for horizontal centering of block elements)
- .section (for consistent section padding)
- .hero (for perfectly centered hero sections)
- .card (for consistently aligned card layouts)

COLOR CLASSES:
- .section-gradient-1, .section-gradient-2, .section-gradient-3, .section-gradient-4 (for section backgrounds)
- .bg-gradient-1, .bg-gradient-2, .bg-gradient-3, .bg-gradient-4, .bg-gradient-5 (for backgrounds)
- .card-gradient-1, .card-gradient-2, .card-gradient-3 (for colorful cards)
- .btn-primary, .btn-secondary, .btn-accent (for colorful buttons)
- .text-white, .text-primary (for proper text contrast)

EMOJI CLASSES:
- .emoji (for normal sized emojis)
- .emoji-lg (for large emojis)
- .emoji-xl (for extra large emojis)

DESIGN PRINCIPLES:
- Use vibrant, eye-catching color combinations
- Ensure proper contrast between text and background
- Create visual hierarchy with typography, colors, and spacing
- Add emojis to make content engaging and friendly
- Use contemporary layouts with perfect alignment
- Include modern UI components with vibrant colors
- Implement smooth color transitions and hover effects
- Add visual feedback for user interactions with color changes

HTML STRUCTURE REQUIREMENTS:
- Use semantic HTML5 elements (header, nav, main, section, article, footer)
- Add proper alignment classes to ALL elements
- Use .container class for all major sections
- Add emojis to ALL headings and important text
- Implement colorful section classes (section-gradient-1, etc.)
- Use .grid or .flex classes for all layouts
- Add proper spacing classes (py-4xl, mb-lg, etc.)
- Include emoji classes (.emoji, .emoji-lg) throughout

CSS REQUIREMENTS:
- Use the provided vibrant color variables extensively
- Implement colorful gradient backgrounds for sections
- Use high contrast text colors based on background
- Ensure perfect vertical and horizontal centering
- Use consistent spacing system with CSS variables
- Implement responsive breakpoints with maintained colors and alignment

EXAMPLE STRUCTURE:
<section class="hero section-gradient-1">
  <div class="container flex flex-col items-center justify-center text-center">
    <h1 class="text-white mb-lg">🚀 Welcome to Our Amazing Website <span class="emoji-lg">✨</span></h1>
    <p class="text-white mb-xl">💡 We create incredible experiences with perfect alignment</p>
    <button class="btn btn-primary">🎯 Get Started <span class="emoji">🚀</span></button>
  </div>
</section>

<section class="section section-primary">
  <div class="container">
    <h2 class="text-center text-primary mb-2xl">⭐ Our Amazing Features <span class="emoji-lg">🎨</span></h2>
    <div class="grid grid-cols-3 gap-xl">
      <div class="card card-gradient-1">
        <div class="card-body text-center">
          <h3 class="card-title">🚀 Fast Performance</h3>
          <p class="card-text">⚡ Lightning fast loading times</p>
        </div>
      </div>
    </div>
  </div>
</section>

OUTPUT FORMAT:
Return ONLY valid JSON in this exact format (no markdown, no extra text):
{
  "html": "complete HTML document with proper DOCTYPE, meta tags, semantic structure, PERFECT ALIGNMENT CLASSES, VIBRANT COLOR CLASSES, and EMOJIS THROUGHOUT",
  "css": "comprehensive CSS with modern styling, responsive design, animations, PERFECT ALIGNMENT UTILITIES, and VIBRANT COLOR SYSTEM",
  "js": "functional JavaScript with smooth interactions and modern features"
}

IMPORTANT: 
- Escape all quotes properly in JSON (\")
- Generate COMPLETE, FUNCTIONAL websites with PERFECT ALIGNMENT, VIBRANT COLORS, and EMOJIS
- Use alignment utility classes EXTENSIVELY throughout the HTML
- Use colorful gradient backgrounds for different sections
- Add emojis to EVERY heading, button, and important content
- Ensure high contrast between background and text colors
- Make it visually impressive and professional with pixel-perfect layouts
- Include real content with emojis, not just placeholders
- Add multiple colorful sections with consistent alignment
- Implement proper navigation and layout with perfect centering and colors
- Use modern design patterns with flawless alignment and vibrant aesthetics
- Every element must be perfectly aligned, colorfully designed, and emoji-enhanced
"""

    try:
        # Enhanced prompt with specific requirements
        enhanced_prompt = f"""
        {system_prompt}
        
        User Request: {prompt}
        
        Additional Requirements:
        - Create a complete, multi-section website
        - Include navigation, hero section, features, and footer
        - Use modern design trends and animations
        - Make it responsive and accessible
        - Add interactive elements and smooth transitions
        - Include proper meta tags and SEO optimization
        - Use contemporary color schemes and typography
        - Implement loading animations and hover effects
        """
        
        response = model.generate_content(enhanced_prompt)
        raw = response.text.strip()
        
        # Clean up the response
        raw = clean_gemini_response(raw)
        
        # Parse JSON and validate
        site_code = json.loads(raw)
        
        # Validate and enhance the generated code
        site_code = validate_and_enhance_code(site_code, prompt)
        
        return site_code
        
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
        print(f"Raw response: {raw[:500]}...")
        return generate_fallback_website(prompt)
    except Exception as e:
        print(f"Error generating website: {e}")
        return generate_fallback_website(prompt)

def clean_gemini_response(raw_response: str) -> str:
    """Clean and format the Gemini API response"""
    # Remove markdown code blocks
    if "```json" in raw_response:
        raw_response = raw_response.split("```json")[1].split("```")[0]
    elif "```" in raw_response:
        raw_response = raw_response.strip("`").strip()
    
    # Remove any leading/trailing whitespace
    raw_response = raw_response.strip()
    
    # Fix common JSON formatting issues
    raw_response = re.sub(r'^\s*json\s*', '', raw_response, flags=re.IGNORECASE)
    
    return raw_response

def validate_and_enhance_code(site_code: dict, original_prompt: str) -> dict:
    """Validate and enhance the generated code"""
    
    # Ensure all required keys exist
    required_keys = ["html", "css", "js"]
    for key in required_keys:
        if key not in site_code or not site_code[key]:
            site_code[key] = ""
    
    # Enhance HTML with meta tags and structure
    if site_code["html"] and not "<!DOCTYPE html>" in site_code["html"]:
        site_code["html"] = enhance_html_structure(site_code["html"], original_prompt)
    
    # Enhance CSS with modern features
    site_code["css"] = enhance_css_styling(site_code["css"])
    
    # Enhance JavaScript with modern features
    site_code["js"] = enhance_javascript_functionality(site_code["js"])
    
    return site_code

def enhance_html_structure(html_content: str, prompt: str) -> str:
    """Enhance HTML with proper structure and meta tags"""
    if "<!DOCTYPE html>" in html_content:
        return html_content
    
    # Generate a title based on the prompt
    title = generate_title_from_prompt(prompt)
    
    enhanced_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional website created with AI">
    <title>{title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    {html_content}
</body>
</html>"""
    
    return enhanced_html

def enhance_css_styling(css_content: str) -> str:
    """Enhance CSS with modern styling, PERFECT ALIGNMENT, and VIBRANT COLORS"""
    modern_css_base = """
/* Modern CSS Reset and Base Styles */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    /* Vibrant Color Palette */
    --primary-color: #6366f1;
    --primary-light: #818cf8;
    --primary-dark: #4f46e5;
    --secondary-color: #ec4899;
    --secondary-light: #f472b6;
    --secondary-dark: #db2777;
    --accent-color: #f59e0b;
    --accent-light: #fbbf24;
    --accent-dark: #d97706;
    
    /* Vibrant Background Colors */
    --bg-gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --bg-gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --bg-gradient-3: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --bg-gradient-4: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    --bg-gradient-5: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    --bg-gradient-6: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    --bg-gradient-7: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
    --bg-gradient-8: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    
    /* Text Colors with High Contrast */
    --text-primary: #1a202c;
    --text-secondary: #4a5568;
    --text-light: #ffffff;
    --text-muted: #718096;
    --text-accent: #2d3748;
    
    /* Vibrant Surface Colors */
    --surface-primary: #ffffff;
    --surface-secondary: #f7fafc;
    --surface-accent: #edf2f7;
    --surface-dark: #2d3748;
    --surface-darker: #1a202c;
    
    /* Colorful Borders */
    --border-primary: #e2e8f0;
    --border-accent: #cbd5e0;
    --border-vibrant: #ed64a6;
    
    /* Vibrant Shadows */
    --shadow-primary: 0 4px 15px rgba(99, 102, 241, 0.2);
    --shadow-secondary: 0 4px 15px rgba(236, 72, 153, 0.2);
    --shadow-accent: 0 4px 15px rgba(245, 158, 11, 0.2);
    --shadow-lg: 0 10px 25px rgba(0, 0, 0, 0.15);
    --shadow-xl: 0 20px 40px rgba(0, 0, 0, 0.1);
    
    --radius-sm: 0.375rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-xl: 1rem;
    --radius-2xl: 1.5rem;
    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    
    /* Perfect spacing system */
    --space-xs: 0.25rem;   /* 4px */
    --space-sm: 0.5rem;    /* 8px */
    --space-md: 1rem;      /* 16px */
    --space-lg: 1.5rem;    /* 24px */
    --space-xl: 2rem;      /* 32px */
    --space-2xl: 3rem;     /* 48px */
    --space-3xl: 4rem;     /* 64px */
    --space-4xl: 6rem;     /* 96px */
    
    /* Container widths */
    --container-sm: 640px;
    --container-md: 768px;
    --container-lg: 1024px;
    --container-xl: 1280px;
    --container-2xl: 1536px;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
    color: var(--text-primary);
    background: var(--bg-gradient-1);
    scroll-behavior: smooth;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    min-height: 100vh;
}

/* PERFECT ALIGNMENT UTILITIES */

/* Container System - Perfect Centering */
.container {
    width: 100%;
    max-width: var(--container-xl);
    margin: 0 auto;
    padding: 0 var(--space-lg);
}

.container-sm { max-width: var(--container-sm); }
.container-md { max-width: var(--container-md); }
.container-lg { max-width: var(--container-lg); }
.container-xl { max-width: var(--container-xl); }
.container-2xl { max-width: var(--container-2xl); }

/* Flexbox Alignment System */
.flex { display: flex; }
.inline-flex { display: inline-flex; }
.flex-col { flex-direction: column; }
.flex-row { flex-direction: row; }
.flex-wrap { flex-wrap: wrap; }
.flex-nowrap { flex-wrap: nowrap; }

/* Perfect Alignment Classes */
.items-start { align-items: flex-start; }
.items-center { align-items: center; }
.items-end { align-items: flex-end; }
.items-stretch { align-items: stretch; }
.items-baseline { align-items: baseline; }

.justify-start { justify-content: flex-start; }
.justify-center { justify-content: center; }
.justify-end { justify-content: flex-end; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }
.justify-evenly { justify-content: space-evenly; }

.content-start { align-content: flex-start; }
.content-center { align-content: center; }
.content-end { align-content: flex-end; }
.content-between { align-content: space-between; }
.content-around { align-content: space-around; }

/* Grid System for Perfect Layouts */
.grid { display: grid; }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.grid-cols-6 { grid-template-columns: repeat(6, minmax(0, 1fr)); }
.grid-cols-12 { grid-template-columns: repeat(12, minmax(0, 1fr)); }

.col-span-1 { grid-column: span 1 / span 1; }
.col-span-2 { grid-column: span 2 / span 2; }
.col-span-3 { grid-column: span 3 / span 3; }
.col-span-4 { grid-column: span 4 / span 4; }
.col-span-6 { grid-column: span 6 / span 6; }
.col-span-12 { grid-column: span 12 / span 12; }

.gap-0 { gap: 0; }
.gap-xs { gap: var(--space-xs); }
.gap-sm { gap: var(--space-sm); }
.gap-md { gap: var(--space-md); }
.gap-lg { gap: var(--space-lg); }
.gap-xl { gap: var(--space-xl); }
.gap-2xl { gap: var(--space-2xl); }
.gap-3xl { gap: var(--space-3xl); }

/* Text Alignment and Colors */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }
.text-justify { text-align: justify; }

/* Vibrant Text Color Classes */
.text-white { color: var(--text-light); }
.text-primary { color: var(--text-primary); }
.text-secondary { color: var(--text-secondary); }
.text-accent { color: var(--text-accent); }
.text-muted { color: var(--text-muted); }

/* Vibrant Background Classes */
.bg-primary { background-color: var(--surface-primary); }
.bg-secondary { background-color: var(--surface-secondary); }
.bg-accent { background-color: var(--surface-accent); }
.bg-dark { background-color: var(--surface-dark); }
.bg-gradient-1 { background: var(--bg-gradient-1); }
.bg-gradient-2 { background: var(--bg-gradient-2); }
.bg-gradient-3 { background: var(--bg-gradient-3); }
.bg-gradient-4 { background: var(--bg-gradient-4); }
.bg-gradient-5 { background: var(--bg-gradient-5); }

/* Spacing System */
.m-0 { margin: 0; }
.m-auto { margin: auto; }
.mx-auto { margin-left: auto; margin-right: auto; }
.my-auto { margin-top: auto; margin-bottom: auto; }

.p-0 { padding: 0; }
.p-xs { padding: var(--space-xs); }
.p-sm { padding: var(--space-sm); }
.p-md { padding: var(--space-md); }
.p-lg { padding: var(--space-lg); }
.p-xl { padding: var(--space-xl); }
.p-2xl { padding: var(--space-2xl); }
.p-3xl { padding: var(--space-3xl); }
.p-4xl { padding: var(--space-4xl); }

.px-0 { padding-left: 0; padding-right: 0; }
.px-xs { padding-left: var(--space-xs); padding-right: var(--space-xs); }
.px-sm { padding-left: var(--space-sm); padding-right: var(--space-sm); }
.px-md { padding-left: var(--space-md); padding-right: var(--space-md); }
.px-lg { padding-left: var(--space-lg); padding-right: var(--space-lg); }
.px-xl { padding-left: var(--space-xl); padding-right: var(--space-xl); }
.px-2xl { padding-left: var(--space-2xl); padding-right: var(--space-2xl); }

.py-0 { padding-top: 0; padding-bottom: 0; }
.py-xs { padding-top: var(--space-xs); padding-bottom: var(--space-xs); }
.py-sm { padding-top: var(--space-sm); padding-bottom: var(--space-sm); }
.py-md { padding-top: var(--space-md); padding-bottom: var(--space-md); }
.py-lg { padding-top: var(--space-lg); padding-bottom: var(--space-lg); }
.py-xl { padding-top: var(--space-xl); padding-bottom: var(--space-xl); }
.py-2xl { padding-top: var(--space-2xl); padding-bottom: var(--space-2xl); }
.py-3xl { padding-top: var(--space-3xl); padding-bottom: var(--space-3xl); }
.py-4xl { padding-top: var(--space-4xl); padding-bottom: var(--space-4xl); }

.mb-0 { margin-bottom: 0; }
.mb-xs { margin-bottom: var(--space-xs); }
.mb-sm { margin-bottom: var(--space-sm); }
.mb-md { margin-bottom: var(--space-md); }
.mb-lg { margin-bottom: var(--space-lg); }
.mb-xl { margin-bottom: var(--space-xl); }
.mb-2xl { margin-bottom: var(--space-2xl); }
.mb-3xl { margin-bottom: var(--space-3xl); }

.mt-0 { margin-top: 0; }
.mt-xs { margin-top: var(--space-xs); }
.mt-sm { margin-top: var(--space-sm); }
.mt-md { margin-top: var(--space-md); }
.mt-lg { margin-top: var(--space-lg); }
.mt-xl { margin-top: var(--space-xl); }
.mt-2xl { margin-top: var(--space-2xl); }
.mt-3xl { margin-top: var(--space-3xl); }

/* Perfect Section Layouts with Vibrant Colors */
.section {
    padding: var(--space-4xl) 0;
    position: relative;
}

.section-primary {
    background: var(--surface-primary);
    color: var(--text-primary);
}

.section-gradient-1 {
    background: var(--bg-gradient-1);
    color: var(--text-light);
}

.section-gradient-2 {
    background: var(--bg-gradient-2);
    color: var(--text-light);
}

.section-gradient-3 {
    background: var(--bg-gradient-3);
    color: var(--text-light);
}

.section-gradient-4 {
    background: var(--bg-gradient-4);
    color: var(--text-primary);
}

/* Hero Section Perfect Alignment with Vibrant Colors */
.hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 80vh;
    padding: var(--space-4xl) 0;
    background: var(--bg-gradient-1);
    color: var(--text-light);
    position: relative;
    overflow: hidden;
}

.hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%);
    z-index: 0;
}

.hero > * {
    position: relative;
    z-index: 1;
}

/* Card Perfect Alignment with Vibrant Colors */
.card {
    display: flex;
    flex-direction: column;
    background: var(--surface-primary);
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-xl);
    overflow: hidden;
    transition: var(--transition);
    border: 2px solid transparent;
    background-clip: padding-box;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: var(--shadow-primary);
    border-color: var(--primary-color);
}

.card-gradient-1 {
    background: var(--bg-gradient-6);
    color: var(--text-primary);
}

.card-gradient-2 {
    background: var(--bg-gradient-7);
    color: var(--text-primary);
}

.card-gradient-3 {
    background: var(--bg-gradient-8);
    color: var(--text-primary);
}

.card-body {
    padding: var(--space-xl);
    flex: 1;
    display: flex;
    flex-direction: column;
}

.card-title {
    margin-bottom: var(--space-md);
    font-weight: 600;
    font-size: 1.5rem;
}

.card-text {
    flex: 1;
    margin-bottom: var(--space-lg);
    opacity: 0.9;
}

/* Perfect Button Alignment with Vibrant Colors */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: var(--space-md) var(--space-xl);
    border: none;
    border-radius: var(--radius-lg);
    font-weight: 600;
    text-decoration: none;
    transition: var(--transition);
    cursor: pointer;
    position: relative;
    overflow: hidden;
    white-space: nowrap;
    text-align: center;
    vertical-align: middle;
    font-size: 1rem;
}

.btn-primary {
    background: linear-gradient(135deg, var(--primary-color), var(--primary-light));
    color: var(--text-light);
    box-shadow: var(--shadow-primary);
}

.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
    background: linear-gradient(135deg, var(--primary-dark), var(--primary-color));
}

.btn-secondary {
    background: linear-gradient(135deg, var(--secondary-color), var(--secondary-light));
    color: var(--text-light);
    box-shadow: var(--shadow-secondary);
}

.btn-secondary:hover {
    transform: translateY(-3px);
    background: linear-gradient(135deg, var(--secondary-dark), var(--secondary-color));
}

.btn-accent {
    background: linear-gradient(135deg, var(--accent-color), var(--accent-light));
    color: var(--text-light);
    box-shadow: var(--shadow-accent);
}

.btn-accent:hover {
    transform: translateY(-3px);
    background: linear-gradient(135deg, var(--accent-dark), var(--accent-color));
}

/* Navigation Perfect Alignment with Colors */
.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: var(--space-lg) 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    margin-bottom: var(--space-lg);
}

.nav-links {
    display: flex;
    align-items: center;
    gap: var(--space-xl);
    list-style: none;
}

.nav-link {
    color: var(--text-light);
    text-decoration: none;
    font-weight: 500;
    transition: var(--transition);
}

.nav-link:hover {
    color: var(--accent-light);
    transform: translateY(-2px);
}

/* Perfect Footer Alignment with Colors */
.footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: var(--space-3xl) 0;
    background: var(--bg-gradient-2);
    color: var(--text-light);
}

/* Emoji Enhancement */
.emoji {
    font-size: 1.2em;
    margin: 0 0.25rem;
}

.emoji-lg {
    font-size: 2em;
    margin: 0 0.5rem;
}

.emoji-xl {
    font-size: 3em;
    margin: 0 0.75rem;
}

/* Smooth animations */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes bounceIn {
    0% {
        opacity: 0;
        transform: scale(0.3);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
    }
    70% {
        transform: scale(0.9);
    }
    100% {
        opacity: 1;
        transform: scale(1);
    }
}

.animate-fade-in-up {
    animation: fadeInUp 0.8s ease-out forwards;
}

.animate-bounce-in {
    animation: bounceIn 1s ease-out forwards;
}

/* Perfect Responsive Design */
@media (max-width: 1024px) {
    .container {
        padding: 0 var(--space-md);
    }
    
    .grid-cols-4 {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
    
    .grid-cols-3 {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

@media (max-width: 768px) {
    .container {
        padding: 0 var(--space-md);
    }
    
    .section {
        padding: var(--space-2xl) 0;
    }
    
    .hero {
        min-height: 60vh;
        padding: var(--space-2xl) 0;
    }
    
    .grid-cols-2,
    .grid-cols-3,
    .grid-cols-4 {
        grid-template-columns: 1fr;
    }
    
    .flex-row {
        flex-direction: column;
    }
    
    .navbar {
        flex-direction: column;
        gap: var(--space-lg);
    }
    
    .nav-links {
        flex-direction: column;
        gap: var(--space-md);
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 var(--space-sm);
    }
    
    .p-xl,
    .px-xl,
    .py-xl {
        padding: var(--space-md);
    }
    
    .card-body {
        padding: var(--space-lg);
    }
    
    .emoji-xl {
        font-size: 2em;
    }
    
    .emoji-lg {
        font-size: 1.5em;
    }
}

"""
    
    return modern_css_base + "\n\n" + css_content

def enhance_javascript_functionality(js_content: str) -> str:
    """Enhance JavaScript with modern features and interactions"""
    modern_js_base = """
// Modern JavaScript enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add loading animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in-up');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    document.querySelectorAll('section, .card, .feature').forEach(el => {
        observer.observe(el);
    });
    
    // Add hover effects to interactive elements
    document.querySelectorAll('.btn, .card, .hover-effect').forEach(element => {
        element.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        element.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
});

"""
    
    return modern_js_base + "\n\n" + js_content

def generate_title_from_prompt(prompt: str) -> str:
    """Generate a title from the user prompt"""
    # Simple title generation logic
    words = prompt.lower().split()
    
    # Common website types and their titles
    title_map = {
        'portfolio': 'Professional Portfolio',
        'restaurant': 'Restaurant & Dining',
        'business': 'Business Solutions',
        'blog': 'Personal Blog',
        'corporate': 'Corporate Website',
        'startup': 'Startup Landing Page',
        'agency': 'Creative Agency',
        'shop': 'Online Store',
        'photography': 'Photography Portfolio',
        'music': 'Music & Entertainment'
    }
    
    for keyword, title in title_map.items():
        if keyword in words:
            return title
    
    return "Professional Website"

def generate_fallback_website(prompt: str) -> dict:
    """Generate a fallback website when API fails"""
    title = generate_title_from_prompt(prompt)
    
    fallback_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="container">
        <section class="hero">
            <div class="flex flex-col items-center justify-center text-center">
                <h1>Welcome to {title}</h1>
                <p>A modern, professional website created with AI technology and perfect alignment</p>
                <button class="btn">Get Started</button>
            </div>
        </section>
        
        <section class="features section">
            <div class="container">
                <h2 class="section-title">Our Amazing Features</h2>
                <div class="feature-grid">
                    <div class="feature-card">
                        <h3>Perfect Design</h3>
                        <p>Every element is perfectly aligned and professionally designed for maximum visual impact</p>
                    </div>
                    <div class="feature-card">
                        <h3>Responsive Layout</h3>
                        <p>Looks amazing on all devices with consistent alignment and spacing throughout</p>
                    </div>
                    <div class="feature-card">
                        <h3>Modern Technology</h3>
                        <p>Built with the latest web technologies and best practices for optimal performance</p>
                    </div>
                </div>
            </div>
        </section>
        
        <footer class="footer">
            <div class="container">
                <p>&copy; 2024 {title}. All rights reserved. | Perfectly crafted with AI</p>
            </div>
        </footer>
    </div>
</body>
</html>"""

    fallback_css = """
:root {
    --primary: #3b82f6;
    --secondary: #8b5cf6;
    --text: #1f2937;
    --bg: #ffffff;
    --border: #e5e7eb;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    --space-4xl: 6rem;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
}

/* Perfect Container System */
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-xl);
}

/* Perfect Flexbox Utilities */
.flex { display: flex; }
.flex-col { flex-direction: column; }
.items-center { align-items: center; }
.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.text-center { text-align: center; }
.mx-auto { margin-left: auto; margin-right: auto; }

/* Perfect Grid System */
.grid { display: grid; }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.gap-lg { gap: var(--space-lg); }
.gap-xl { gap: var(--space-xl); }

/* Perfect Hero Section */
.hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: var(--space-4xl) 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border-radius: 1rem;
    margin: var(--space-xl) 0;
    min-height: 70vh;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: var(--space-md);
    font-weight: 700;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: var(--space-xl);
    opacity: 0.9;
    max-width: 600px;
}

/* Perfect Button Alignment */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: var(--space-md) var(--space-xl);
    background: rgba(255, 255, 255, 0.2);
    color: white;
    text-decoration: none;
    border-radius: 0.5rem;
    border: none;
    cursor: pointer;
    font-weight: 500;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
    white-space: nowrap;
}

.btn:hover {
    background: rgba(255, 255, 255, 0.3);
    transform: translateY(-2px);
}

/* Perfect Section Alignment */
.section {
    padding: var(--space-4xl) 0;
}

.features {
    padding: var(--space-4xl) 0;
}

.features .container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.section-title {
    text-align: center;
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: var(--space-2xl);
    color: var(--text);
}

/* Perfect Grid Layout */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-xl);
    margin-top: var(--space-xl);
    width: 100%;
}

/* Perfect Card Alignment */
.feature-card {
    display: flex;
    flex-direction: column;
    background: white;
    padding: var(--space-xl);
    border-radius: 1rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: all 0.3s ease;
    border: 1px solid var(--border);
    text-align: center;
}

.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 25px rgba(0, 0, 0, 0.15);
}

.feature-card h3 {
    color: var(--primary);
    margin-bottom: var(--space-md);
    font-size: 1.5rem;
    font-weight: 600;
}

.feature-card p {
    color: var(--text);
    flex: 1;
}

/* Perfect Footer Alignment */
.footer {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: var(--space-2xl) 0;
    border-top: 1px solid var(--border);
    color: #6b7280;
}

/* Perfect Responsive Design */
@media (max-width: 768px) {
    .hero h1 {
        font-size: 2rem;
    }
    
    .container {
        padding: 0 var(--space-md);
    }
    
    .feature-grid {
        grid-template-columns: 1fr;
        gap: var(--space-lg);
    }
    
    .section-title {
        font-size: 2rem;
    }
    
    .hero {
        padding: var(--space-2xl) 0;
        min-height: 50vh;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 var(--space-md);
    }
    
    .hero h1 {
        font-size: 1.75rem;
    }
    
    .section-title {
        font-size: 1.75rem;
    }
    
    .feature-card {
        padding: var(--space-lg);
    }
}
"""

    fallback_js = """
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth animations
    const cards = document.querySelectorAll('.feature-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    });
    
    cards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease';
        observer.observe(card);
    });
    
    // Add button interactions
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('click', function() {
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'translateY(-2px)';
            }, 150);
        });
    });
});
"""

    return {
        "html": fallback_html,
        "css": fallback_css,
        "js": fallback_js
    }