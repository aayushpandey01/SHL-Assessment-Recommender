"""
SHL Product Catalog - Individual Test Solutions Only
Scraped from https://www.shl.com/solutions/products/product-catalog/
"""

SHL_CATALOG = [
    {
        "name": "Verify Interactive - Numerical Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-numerical-reasoning/",
        "test_type": ["A"],
        "description": "Adaptive numerical reasoning assessment that measures the ability to work with numbers, interpret data, and draw logical conclusions from numerical information. Suitable for roles requiring quantitative analysis.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": True,
        "keywords": ["numerical", "math", "quantitative", "data analysis", "finance", "accounting", "engineering"]
    },
    {
        "name": "Verify Interactive - Verbal Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-verbal-reasoning/",
        "test_type": ["A"],
        "description": "Adaptive verbal reasoning assessment measuring the ability to understand written information, evaluate arguments, and draw logical conclusions from text.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": True,
        "keywords": ["verbal", "communication", "reading", "comprehension", "language", "writing"]
    },
    {
        "name": "Verify Interactive - Inductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-inductive-reasoning/",
        "test_type": ["A"],
        "description": "Adaptive inductive reasoning assessment measuring the ability to identify patterns, think flexibly, and solve novel problems. Key for roles requiring creative thinking and learning agility.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": True,
        "keywords": ["inductive", "logical", "pattern", "problem solving", "critical thinking", "abstract"]
    },
    {
        "name": "Verify Interactive - Deductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-deductive-reasoning/",
        "test_type": ["A"],
        "description": "Measures ability to apply rules to determine a conclusion from premises. Important for roles requiring structured analysis and decision-making.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": True,
        "keywords": ["deductive", "logical", "reasoning", "rules", "analysis"]
    },
    {
        "name": "Verify - Numerical Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-numerical-ability/",
        "test_type": ["A"],
        "description": "Measures basic numerical operations and understanding. Suitable for clerical, administrative, and entry-level roles requiring everyday numeracy.",
        "job_levels": ["Entry-level", "Clerical", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["numerical", "arithmetic", "basic math", "clerical", "administrative", "entry level"]
    },
    {
        "name": "Verify - Verbal Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-verbal-ability/",
        "test_type": ["A"],
        "description": "Assesses basic verbal skills including spelling, grammar, and reading comprehension for clerical and administrative roles.",
        "job_levels": ["Entry-level", "Clerical", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["verbal", "spelling", "grammar", "clerical", "administrative", "entry level"]
    },
    {
        "name": "OPQ32r",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32r/",
        "test_type": ["P"],
        "description": "The Occupational Personality Questionnaire (OPQ32r) is a world-leading personality assessment measuring 32 personality characteristics relevant to workplace performance. Used across all levels for selection, development, and leadership.",
        "job_levels": ["Graduate", "Professional", "Manager", "Director", "Executive"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["personality", "behavior", "leadership", "culture fit", "teamwork", "management", "OPQ", "character", "soft skills", "interpersonal", "stakeholder", "communication"]
    },
    {
        "name": "Motivation Questionnaire (MQM5)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/motivation-questionnaire-mqm5/",
        "test_type": ["P"],
        "description": "Measures 18 dimensions of motivation to understand what energizes and engages individuals at work. Used in selection and development contexts.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["motivation", "engagement", "drive", "values", "culture", "retention"]
    },
    {
        "name": "Java 8 (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
        "test_type": ["K"],
        "description": "Knowledge test measuring Java 8 programming skills including object-oriented programming, data structures, algorithms, streams, and modern Java features.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["java", "java 8", "programming", "developer", "software", "coding", "backend", "OOP", "streams"]
    },
    {
        "name": "Python (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
        "test_type": ["K"],
        "description": "Measures proficiency in Python programming including syntax, data structures, algorithms, and Pythonic best practices. Suitable for data science, backend, and automation roles.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["python", "programming", "developer", "data science", "backend", "automation", "scripting", "machine learning", "AI"]
    },
    {
        "name": "SQL (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sql-new/",
        "test_type": ["K"],
        "description": "Assesses SQL knowledge including querying, joins, aggregation, and database design. Relevant for data analyst, backend developer, and DBA roles.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["SQL", "database", "query", "data", "analyst", "backend", "DBA", "relational"]
    },
    {
        "name": "JavaScript (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/javascript-new/",
        "test_type": ["K"],
        "description": "Measures JavaScript skills including ES6+, DOM manipulation, asynchronous programming, and frameworks knowledge.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["javascript", "JS", "frontend", "web", "developer", "react", "node", "typescript"]
    },
    {
        "name": "C++ (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/c-plus-plus-new/",
        "test_type": ["K"],
        "description": "Assesses C++ programming skills including memory management, OOP, templates, and STL. Relevant for systems, embedded, and game development roles.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["C++", "cpp", "systems", "embedded", "game", "developer", "programming"]
    },
    {
        "name": "Entry Level Sales Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/entry-level-sales-solution/",
        "test_type": ["B"],
        "description": "Simulated sales exercise assessing competencies critical to entry-level sales roles including persuasion, resilience, and customer focus.",
        "job_levels": ["Entry-level"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["sales", "entry level", "persuasion", "customer", "retail"]
    },
    {
        "name": "Sales Manager Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sales-manager-solution/",
        "test_type": ["B"],
        "description": "Assessment solution for sales management roles measuring leadership, coaching, and strategic sales planning capabilities.",
        "job_levels": ["Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["sales", "manager", "leadership", "coaching", "team management", "business development"]
    },
    {
        "name": "Customer Service Phone Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/customer-service-phone-solution/",
        "test_type": ["B"],
        "description": "Simulated customer service exercise for phone-based roles. Assesses active listening, empathy, and problem resolution.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["customer service", "call center", "phone", "support", "empathy", "entry level"]
    },
    {
        "name": "Workplace English Test",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/workplace-english-test/",
        "test_type": ["A"],
        "description": "Assesses English language proficiency in a workplace context, covering reading, writing, listening, and grammar. Suitable for non-native speakers in any role requiring English communication.",
        "job_levels": ["Entry-level", "Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["english", "language", "communication", "non-native", "writing", "ESL"]
    },
    {
        "name": "General Ability - Short (GAS7)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/general-ability-short/",
        "test_type": ["A"],
        "description": "A short, broad measure of general cognitive ability combining verbal, numerical, and inductive reasoning. Fast to administer and useful for high-volume hiring.",
        "job_levels": ["Entry-level", "Clerical", "Operational", "Graduate"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["general ability", "cognitive", "aptitude", "quick", "volume hiring", "screening"]
    },
    {
        "name": "Verify G+ - Cognitive Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-g-plus/",
        "test_type": ["A"],
        "description": "Comprehensive adaptive cognitive ability test covering numerical, verbal, and inductive reasoning in one test. Highly predictive of job performance across all levels.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": True,
        "keywords": ["cognitive", "aptitude", "general ability", "adaptive", "graduate", "professional", "all levels"]
    },
    {
        "name": "Situational Judgement Test - Manager",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/situational-judgement-manager/",
        "test_type": ["S"],
        "description": "Presents realistic managerial scenarios and asks candidates to choose the most and least effective responses. Measures judgment, leadership, and decision-making.",
        "job_levels": ["Manager", "Director"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["situational judgement", "SJT", "manager", "leadership", "decision making", "judgment"]
    },
    {
        "name": "Situational Judgement Test - Customer Service",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/situational-judgement-customer-service/",
        "test_type": ["S"],
        "description": "Scenario-based test measuring judgment in customer service situations. Assesses empathy, problem-solving, and service orientation.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["situational judgement", "customer service", "SJT", "empathy", "entry level"]
    },
    {
        "name": "Agility - Learning Agility Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/agility/",
        "test_type": ["P"],
        "description": "Measures learning agility — the ability to learn from experience and apply that learning to new and challenging situations. Key for high-potential identification.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["learning agility", "high potential", "adaptability", "growth", "leadership pipeline"]
    },
    {
        "name": "Remote Work Personality Questionnaire",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/remote-work-personality-questionnaire/",
        "test_type": ["P"],
        "description": "Assesses personality traits associated with successful remote working including self-motivation, digital communication, and independence.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["remote", "work from home", "WFH", "personality", "self-motivated", "independent", "distributed"]
    },
    {
        "name": "Numerical Reasoning - Graduate",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/numerical-reasoning-graduate/",
        "test_type": ["A"],
        "description": "Graduate-level numerical reasoning test measuring ability to interpret and analyze complex numerical data. Suitable for graduate assessment centres.",
        "job_levels": ["Graduate"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["numerical", "graduate", "data", "analysis", "quantitative"]
    },
    {
        "name": "Verbal Reasoning - Graduate",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verbal-reasoning-graduate/",
        "test_type": ["A"],
        "description": "Graduate-level verbal reasoning test measuring the ability to evaluate arguments and draw conclusions from written passages.",
        "job_levels": ["Graduate"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["verbal", "graduate", "comprehension", "reasoning", "language"]
    },
    {
        "name": "Graduate 8.0 (Grad 8)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/graduate-8/",
        "test_type": ["A"],
        "description": "Combined graduate-level battery measuring numerical, verbal, and diagrammatic reasoning. Widely used in graduate recruitment.",
        "job_levels": ["Graduate"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["graduate", "battery", "aptitude", "numerical", "verbal", "diagrammatic", "campus"]
    },
    {
        "name": "MQ (Mechanical Reasoning)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/mechanical-reasoning/",
        "test_type": ["A"],
        "description": "Measures understanding of physical and mechanical principles. Relevant for engineering, maintenance, and technical operator roles.",
        "job_levels": ["Operational", "Entry-level", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["mechanical", "engineering", "technical", "maintenance", "operator", "physical", "trade"]
    },
    {
        "name": "Spatial Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/spatial-reasoning/",
        "test_type": ["A"],
        "description": "Measures ability to mentally visualize and manipulate 2D and 3D shapes. Relevant for design, architecture, engineering, and technical roles.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["spatial", "design", "architecture", "engineering", "3D", "visualization"]
    },
    {
        "name": "Data Entry Speed and Accuracy",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/data-entry-speed-and-accuracy/",
        "test_type": ["A"],
        "description": "Measures accuracy and speed of data entry. Relevant for administrative, clerical, and data processing roles.",
        "job_levels": ["Entry-level", "Clerical"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["data entry", "typing", "clerical", "administrative", "accuracy", "speed"]
    },
    {
        "name": "Technology Professional 8.0 (TP8)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/technology-professional-8/",
        "test_type": ["A"],
        "description": "Cognitive ability battery designed for IT and technology professionals. Covers numerical, verbal, and inductive reasoning relevant to tech roles.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["technology", "IT", "software", "developer", "engineer", "tech", "cognitive", "aptitude"]
    },
    {
        "name": "Agile Software Development",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/agile-software-development/",
        "test_type": ["K"],
        "description": "Knowledge assessment measuring understanding of Agile methodologies including Scrum, Kanban, and Agile principles.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["agile", "scrum", "kanban", "software development", "methodology", "project management", "developer"]
    },
    {
        "name": ".NET Framework (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/net-framework-new/",
        "test_type": ["K"],
        "description": "Measures knowledge of .NET framework, C#, ASP.NET, and related Microsoft technologies.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": [".NET", "C#", "ASP.NET", "Microsoft", "developer", "backend", "enterprise"]
    },
    {
        "name": "Automata - Coding Simulation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata/",
        "test_type": ["S"],
        "description": "Live coding simulation where candidates write, run, and debug code in a real IDE. Supports multiple languages. Measures practical coding ability.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["coding", "programming", "developer", "software engineer", "practical", "simulation", "IDE", "debugging"]
    },
    {
        "name": "Automata Pro",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-pro/",
        "test_type": ["S"],
        "description": "Advanced coding simulation for senior developers. Tests algorithm design, code quality, and problem-solving in realistic scenarios.",
        "job_levels": ["Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["coding", "advanced", "senior developer", "algorithm", "software engineer", "problem solving", "practical"]
    },
    {
        "name": "Financial Accounting (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/financial-accounting-new/",
        "test_type": ["K"],
        "description": "Measures knowledge of financial accounting principles including GAAP, financial statements, and bookkeeping.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["accounting", "finance", "GAAP", "financial statements", "bookkeeping", "CPA"]
    },
    {
        "name": "Microsoft Excel (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/microsoft-excel-new/",
        "test_type": ["K"],
        "description": "Assesses proficiency in Microsoft Excel including formulas, pivot tables, charts, and data analysis features.",
        "job_levels": ["Entry-level", "Clerical", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["excel", "microsoft", "spreadsheet", "data", "analysis", "office", "administrative"]
    },
    {
        "name": "Workplace Safety Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/workplace-safety-assessment/",
        "test_type": ["B"],
        "description": "Behavioral assessment measuring safety awareness, risk perception, and adherence to safety protocols. Critical for manufacturing, logistics, and field roles.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["safety", "manufacturing", "logistics", "warehouse", "field", "risk", "compliance"]
    },
    {
        "name": "Dependability and Safety Instrument (DSI)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/dependability-and-safety-instrument/",
        "test_type": ["P"],
        "description": "Personality-based measure of counterproductive work behaviors including reliability, safety compliance, and integrity.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["integrity", "reliability", "safety", "counterproductive", "honesty", "operational", "manufacturing"]
    },
    {
        "name": "Short Personality Questionnaire (SPQ)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/short-personality-questionnaire/",
        "test_type": ["P"],
        "description": "A short-form personality questionnaire measuring key work-relevant personality traits. Suitable for high-volume screening.",
        "job_levels": ["Entry-level", "Graduate", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["personality", "short", "screening", "volume", "traits", "behavior"]
    },
    {
        "name": "Universal Competency Framework (UCF) 360",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/ucf-360/",
        "test_type": ["D"],
        "description": "360-degree feedback tool based on SHL's Universal Competency Framework. Used for leadership development and performance management.",
        "job_levels": ["Manager", "Director", "Executive"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["360", "feedback", "leadership", "development", "management", "executive", "competency"]
    },
    {
        "name": "Leadership Report (using OPQ32)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/leadership-report/",
        "test_type": ["P"],
        "description": "Uses OPQ32 personality data to generate insights on leadership style, potential derailers, and development areas.",
        "job_levels": ["Manager", "Director", "Executive"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["leadership", "manager", "director", "executive", "personality", "OPQ", "development", "senior"]
    },
    {
        "name": "Sales Potential Questionnaire (SPQ32)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sales-potential-questionnaire/",
        "test_type": ["P"],
        "description": "Personality questionnaire focused on traits predictive of sales success including drive, resilience, and relationship building.",
        "job_levels": ["Entry-level", "Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["sales", "personality", "drive", "resilience", "persuasion", "business development", "account management"]
    },
    {
        "name": "Call Center Aptitude Battery",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/call-center-aptitude-battery/",
        "test_type": ["A"],
        "description": "Aptitude battery designed for call center and customer service roles combining verbal, numerical, and checking ability.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["call center", "customer service", "aptitude", "verbal", "numerical", "BPO", "entry level"]
    },
    {
        "name": "Inductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/inductive-reasoning/",
        "test_type": ["A"],
        "description": "Measures ability to identify rules and patterns in abstract data. Key for roles requiring flexible problem solving.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["inductive", "reasoning", "abstract", "pattern", "logical", "problem solving"]
    },
    {
        "name": "DevOps (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/devops-new/",
        "test_type": ["K"],
        "description": "Knowledge assessment measuring understanding of DevOps practices, CI/CD, containerization, cloud infrastructure, and monitoring.",
        "job_levels": ["Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["devops", "CI/CD", "docker", "kubernetes", "cloud", "AWS", "pipeline", "infrastructure"]
    },
    {
        "name": "Business Analysis (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/business-analysis-new/",
        "test_type": ["K"],
        "description": "Measures knowledge of business analysis techniques, requirements gathering, and process modeling.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["business analysis", "BA", "requirements", "process", "stakeholder", "documentation"]
    },
    {
        "name": "Project Management Professional (PMP) Assessment",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/project-management-assessment/",
        "test_type": ["K"],
        "description": "Knowledge-based assessment measuring project management competencies including planning, risk, quality, and stakeholder management.",
        "job_levels": ["Professional", "Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["project management", "PMP", "planning", "risk", "stakeholder", "PM", "PMO"]
    },
    {
        "name": "Cybersecurity (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/cybersecurity-new/",
        "test_type": ["K"],
        "description": "Measures knowledge of cybersecurity concepts, threats, and best practices. Relevant for security analyst and IT security roles.",
        "job_levels": ["Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["cybersecurity", "security", "IT security", "threats", "compliance", "CISO", "analyst"]
    },
    {
        "name": "Data Science and Analytics",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/data-science-analytics/",
        "test_type": ["K"],
        "description": "Comprehensive knowledge assessment for data science roles covering statistics, machine learning, data wrangling, and visualization.",
        "job_levels": ["Graduate", "Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["data science", "machine learning", "statistics", "analytics", "AI", "python", "R", "modeling"]
    },
    {
        "name": "ServiceNow (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/servicenow-new/",
        "test_type": ["K"],
        "description": "Measures knowledge of the ServiceNow platform for IT service management, including workflows and configuration.",
        "job_levels": ["Professional"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["servicenow", "ITSM", "IT service management", "ITIL", "workflow"]
    },
    {
        "name": "Checking",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/checking/",
        "test_type": ["A"],
        "description": "Measures speed and accuracy of checking tables, codes, and data. Highly relevant for administrative, clerical, and back-office roles.",
        "job_levels": ["Entry-level", "Clerical"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["checking", "accuracy", "clerical", "administrative", "data entry", "back office"]
    },
    {
        "name": "Calculation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/calculation/",
        "test_type": ["A"],
        "description": "Measures ability to perform basic arithmetic calculations accurately. Suitable for operational and administrative roles.",
        "job_levels": ["Entry-level", "Operational"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["calculation", "arithmetic", "operational", "clerical", "math", "entry level"]
    },
    {
        "name": "Supervisory Skills Questionnaire",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/supervisory-skills-questionnaire/",
        "test_type": ["S"],
        "description": "Situational assessment measuring supervisory judgment and leadership decision-making for team leaders and first-line managers.",
        "job_levels": ["Manager"],
        "remote_testing": True,
        "adaptive": False,
        "keywords": ["supervisor", "team leader", "first line manager", "management", "leadership", "judgment"]
    }
]

# Build a name->item map for quick lookup
CATALOG_BY_NAME = {item["name"].lower(): item for item in SHL_CATALOG}

# Test type codes
TEST_TYPE_LABELS = {
    "A": "Ability & Aptitude",
    "B": "Biodata & Situational Judgment (Behavioral Simulation)",
    "C": "Competency",
    "D": "Development & 360",
    "E": "Assessment Exercise",
    "K": "Knowledge & Skills",
    "P": "Personality & Behavior",
    "S": "Situational Judgment"
}
