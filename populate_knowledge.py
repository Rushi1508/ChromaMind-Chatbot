"""
Populates ChromaDB with extensive business knowledge.
"""

from knowledge_base import add_knowledge

# Extended knowledge base with comprehensive business insights
knowledge_entries = [
    # Company Overview
    {"id": "1", "text": "Way2Reach is a cloud-based AI/ML e-marketplace designed to connect buyers, sellers, and service providers.", "metadata": {"category": "Company Overview", "follow_up": "Would you like to know about our services or industries we serve?"}},

    # Business Model
    {"id": "2", "text": "We offer industry-specific solutions, cutting-edge digital integration, and a scalable model designed for pan-India operations and global expansion.", "metadata": {"category": "Business Model", "follow_up": "Do you want to learn more about our solutions or logistics services?"}},

    # Services
    {"id": "3", "text": "Our services include engineering design, logistics, financial solutions, third-party inspections, and skilled manpower provision tailored to various industries.", "metadata": {"category": "Services", "follow_up": "Would you like details about engineering, financial, or manpower services?"}},

    # Skilled Manpower
    {"id": "4", "text": "Skilled manpower is available for industries like Oil & Gas, Renewable Energy, Power, Infrastructure, and more.", "metadata": {"category": "Manpower", "follow_up": "Would you like to know about manpower availability, costs, or the hiring process?"}},

    # Financial Services
    {"id": "5", "text": "Financial services include Manufacturing Loans, Working Capital, Letters of Credit, Escrow, and Project Loans to support business needs.", "metadata": {"category": "Financial Services", "follow_up": "Do you need details about a specific loan type or financial planning?"}},

    # Survey Services
    {"id": "6", "text": "Survey services include Land Survey, Structural Survey, Ecological Survey, Noise Survey, and Tree Survey for precise planning.", "metadata": {"category": "Surveys", "follow_up": "Are you interested in land surveys, structural assessments, or ecological studies?"}},

    # TPIA (Third Party Inspection Agency) Services
    {"id": "7", "text": "Third Party Inspection Agency (TPIA) services include ISO certification, Industrial Inspection, Boiler Regulation compliance, and Commodity Inspections.", "metadata": {"category": "TPIA Services", "follow_up": "Would you like details about ISO certification, industrial inspection, or commodity checks?"}},

    # Logistics & Supply Chain
    {"id": "8", "text": "Logistics solutions include Sea Freight, Air Freight, Road Freight, Warehousing, and Door-to-Door delivery services.", "metadata": {"category": "Logistics", "follow_up": "Do you want details about sea freight, warehousing, or custom clearance services?"}},

    # Non-Destructive Testing (NDT) and Destructive Testing (DT) Services
    {"id": "9", "text": "Non-Destructive Testing (NDT) and Destructive Testing (DT) services ensure material integrity and quality assurance.", "metadata": {"category": "Testing Services", "follow_up": "Would you like more details about ultrasonic testing, corrosion analysis, or impact testing?"}},

    # Equipment Rental
    {"id": "10", "text": "Equipment rental includes Excavators, Cranes, Loaders, and other heavy machinery for construction and industrial needs.", "metadata": {"category": "Equipment Rental", "follow_up": "Are you looking to rent excavators, cranes, or other construction equipment?"}},

    # Sustainability & Green Energy
    {"id": "11", "text": "Way2Reach supports sustainability initiatives such as Decarbonization, Electrification, and Conservation efforts.", "metadata": {"category": "Sustainability", "follow_up": "Would you like to learn more about decarbonization projects or electrification solutions?"}},

    # MSME Support
    {"id": "12", "text": "Way2Reach empowers rural MSMEs by providing tools for scaling businesses and accessing global markets.", "metadata": {"category": "MSME Support", "follow_up": "Do you want details about our MSME support programs or market access tools?"}},

    # Women Empowerment
    {"id": "13", "text": "Our initiatives for women empowerment focus on skill development, entrepreneurship, and financial independence.", "metadata": {"category": "Women Empowerment", "follow_up": "Would you like information on entrepreneurship programs or skill development initiatives?"}},

    # Contact Information
    {"id": "14", "text": "Contact us at support@way2reach.com or +91-9876543210 for inquiries about our services and partnerships.", "metadata": {"category": "Contact Information", "follow_up": "Would you like us to connect you with a representative or share more contact options?"}},

    # Renewable Energy
    {"id": "15", "text": "Renewable energy services include Solar, Wind, Hydrogen, and Bio-Gas solutions.", "metadata": {"category": "Renewable Energy", "follow_up": "Would you like more information on our renewable energy projects?"}},

    # Infrastructure Development
    {"id": "16", "text": "We specialize in transportation infrastructure projects, including road construction, railway logistics, and urban development.", "metadata": {"category": "Infrastructure", "follow_up": "Do you want to know about road construction or railway logistics services?"}},

    # Telecommunication Infrastructure
    {"id": "17", "text": "We support telecommunication infrastructure projects, including fiber optics, network expansion, and 5G deployment.", "metadata": {"category": "Telecommunication", "follow_up": "Are you looking for telecom solutions or network expansion details?"}},

    # Water Infrastructure
    {"id": "18", "text": "Our water infrastructure projects include desalination plants, water distribution networks, and sanitation management.", "metadata": {"category": "Water Management", "follow_up": "Would you like to learn more about our water purification solutions?"}},

    # Industrial Infrastructure
    {"id": "19", "text": "We provide industrial infrastructure solutions, including factory setup, warehouse automation, and advanced manufacturing systems.", "metadata": {"category": "Industrial Infrastructure", "follow_up": "Do you need help with industrial automation or smart factory solutions?"}},

    # Rural Empowerment
    {"id": "20", "text": "We provide skill development, employment, and digital tools to empower rural communities.", "metadata": {"category": "Rural Development", "follow_up": "Would you like information on rural employment or community upliftment projects?"}},

    # Who Created Way2Reach
    {"id": "21", "text": "Way2Reach was created by a team of AI/ML engineers and business experts to revolutionize the marketplace with smart automation and digital integration.", "metadata": {"category": "Company Overview", "follow_up": "Would you like to learn more about our founders or mission?"}},

     # Industries Served
    {"id": "22", "text": "We serve industries including Oil & Gas, Renewable Energy, Power, Infrastructure, Manufacturing, MSMEs, and Telecommunications.", "metadata": {"category": "Industries", "follow_up": "Do you need solutions tailored to a specific industry?"}},

    # Internship Opportunities
    {"id": "23", "text": "Way2Reach provides free internships in various fields, especially in AI/ML, software development, business analytics, and digital marketing.", "metadata": {"category": "Internships", "follow_up": "Would you like to know about eligibility, duration, or application process?"}},
]

# Populate the knowledge base into ChromaDB
for entry in knowledge_entries:
    add_knowledge(entry["id"], entry["text"], entry["metadata"])

print("✅ Knowledge base populated successfully.")
