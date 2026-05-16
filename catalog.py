"""
SHL Product Catalog – Individual Test Solutions Only
Source: https://www.shl.com/solutions/products/product-catalog/

Test Type Codes:
  A = Ability & Aptitude
  B = Biodata & Situational Judgement
  C = Competencies
  E = Assessment Exercises
  K = Knowledge & Skills
  P = Personality & Behavior
  S = Simulations
"""

SHL_CATALOG = [

    # ── ABILITY & APTITUDE ────────────────────────────────────────────────
    {
        "name": "Verify Interactive - Numerical Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-numerical-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 18,
        "description": "Adaptive interactive test measuring ability to analyse and interpret numerical data, graphs, and tables. Widely used for finance, analyst, and graduate roles.",
        "job_levels": ["Graduate", "Professional", "Mid-Professional"],
        "keywords": ["numerical", "numbers", "data", "finance", "analyst", "statistics", "quantitative", "maths"]
    },
    {
        "name": "Verify Interactive - Deductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-deductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 20,
        "description": "Adaptive test evaluating ability to draw logical conclusions and evaluate arguments from written information.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "keywords": ["logic", "reasoning", "critical thinking", "management", "graduate", "deductive"]
    },
    {
        "name": "Verify Interactive - Inductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-interactive-inductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 18,
        "description": "Adaptive test of pattern recognition and abstract thinking using sequences of shapes and figures.",
        "job_levels": ["Graduate", "Professional", "Mid-Professional"],
        "keywords": ["patterns", "abstract", "problem solving", "analytical", "inductive", "graduate"]
    },
    {
        "name": "Verify G+ (General Ability)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-g-plus/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 36,
        "description": "Comprehensive general ability battery combining numerical, inductive and deductive reasoning. Ideal for broad cognitive screening across all levels.",
        "job_levels": ["Graduate", "Professional", "Mid-Professional", "Manager"],
        "keywords": ["general ability", "cognitive", "all-round", "screening", "aptitude", "graduate", "reasoning"]
    },
    {
        "name": "Verify - Numerical Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-numerical-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Multiple-choice numerical reasoning measuring ability to work with graphs, tables and statistical information.",
        "job_levels": ["Graduate", "Professional"],
        "keywords": ["numerical", "numbers", "data", "finance", "analyst", "quantitative"]
    },
    {
        "name": "Verify - Verbal Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-verbal-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 19,
        "description": "Tests reading comprehension, understanding and drawing logical conclusions from written passages.",
        "job_levels": ["Graduate", "Professional", "Manager"],
        "keywords": ["language", "writing", "communication", "verbal", "reading", "legal", "hr", "management"]
    },
    {
        "name": "Verify - Deductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-deductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Multiple-choice deductive reasoning assessing logical thinking and ability to identify conclusions.",
        "job_levels": ["Graduate", "Professional"],
        "keywords": ["logic", "reasoning", "deductive", "analytical"]
    },
    {
        "name": "Verify - Inductive Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-inductive-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 24,
        "description": "Multiple-choice inductive reasoning for pattern recognition and abstract thinking.",
        "job_levels": ["Graduate", "Professional"],
        "keywords": ["patterns", "abstract", "analytical", "inductive"]
    },
    {
        "name": "Verify - Mechanical Comprehension",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/verify-mechanical-comprehension/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Understanding of mechanical concepts, tools, and physical principles for engineering and technical roles.",
        "job_levels": ["Entry Level", "Graduate", "Professional"],
        "keywords": ["mechanical", "engineering", "technical", "manufacturing", "operator", "maintenance", "production"]
    },
    {
        "name": "Numerical Ability",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/numerical-ability/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 18,
        "description": "Basic numerical calculation skills without a calculator. Used for clerical and administrative roles.",
        "job_levels": ["Entry Level", "Clerical"],
        "keywords": ["clerical", "admin", "basic maths", "data entry", "accounting", "entry level"]
    },
    {
        "name": "Calculation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/calculation/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 10,
        "description": "Speed and accuracy of arithmetic calculations for operational and entry-level roles.",
        "job_levels": ["Entry Level"],
        "keywords": ["calculation", "arithmetic", "clerk", "cashier", "entry level", "speed accuracy"]
    },
    {
        "name": "Reading Comprehension",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/reading-comprehension/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Ability to understand and draw conclusions from written passages. Suitable for customer service and admin.",
        "job_levels": ["Entry Level", "Clerical"],
        "keywords": ["reading", "comprehension", "customer service", "admin", "written"]
    },
    {
        "name": "Checking",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/checking/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 12,
        "description": "Speed and accuracy test for checking data, names and numbers. Used for clerical and data entry roles.",
        "job_levels": ["Entry Level", "Clerical"],
        "keywords": ["data entry", "clerical", "accuracy", "admin", "back office", "attention to detail"]
    },
    {
        "name": "Graduate/ Manager Short Numerical Reasoning",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/graduate-manager-short-numerical-reasoning/",
        "test_type": "A",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 8,
        "description": "Quick numerical reasoning screener normed for graduate and managerial-level candidates.",
        "job_levels": ["Graduate", "Manager"],
        "keywords": ["quick screening", "graduate", "manager", "numerical", "short test"]
    },

    # ── PERSONALITY & BEHAVIOR ────────────────────────────────────────────
    {
        "name": "OPQ32r",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32r/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Industry-leading personality questionnaire measuring 32 work-relevant personality characteristics. Provides deep insight into behavioral style, leadership potential, and working preferences.",
        "job_levels": ["Graduate", "Professional", "Manager", "Director", "Executive"],
        "keywords": ["personality", "behavior", "leadership", "culture fit", "management", "senior", "OPQ", "traits"]
    },
    {
        "name": "OPQ32",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/opq32/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 30,
        "description": "Full OPQ measuring 32 work-relevant personality dimensions. Used for selection, development and leadership assessment.",
        "job_levels": ["Professional", "Manager", "Director", "Executive"],
        "keywords": ["personality", "behavior", "leadership", "management", "OPQ", "team working", "senior hire"]
    },
    {
        "name": "Occupational Personality Questionnaire 32 (OPQ32)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/occupational-personality-questionnaire-32-opq32/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Measures 32 personality characteristics across relationships with people, thinking style, and feelings/emotions.",
        "job_levels": ["Professional", "Manager", "Director", "Executive"],
        "keywords": ["personality", "OPQ32", "leadership", "management", "senior hire", "executive", "emotions"]
    },
    {
        "name": "Motivational Questionnaire (MQ)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/motivational-questionnaire-mq/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Assesses what motivates an individual at work: achievement, flexibility, reward, security. Used in development and retention contexts.",
        "job_levels": ["Professional", "Manager", "Director"],
        "keywords": ["motivation", "engagement", "values", "retention", "culture", "development", "MQ"]
    },
    {
        "name": "RemoteWorkQ",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/remoteworkq/",
        "test_type": "P",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 10,
        "description": "Measures behavioral traits most relevant to remote work success: self-discipline, collaboration, digital communication.",
        "job_levels": ["Professional", "Mid-Professional", "Manager"],
        "keywords": ["remote", "work from home", "virtual", "hybrid", "distributed team", "wfh"]
    },

    # ── SITUATIONAL JUDGEMENT ─────────────────────────────────────────────
    {
        "name": "Customer Contact Scenarios",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/customer-contact-scenarios/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "SJT for customer-facing roles presenting realistic scenarios and measuring appropriateness of responses.",
        "job_levels": ["Entry Level", "Clerical", "Professional"],
        "keywords": ["customer service", "call centre", "support", "retail", "front-line", "contact centre"]
    },
    {
        "name": "Graduate/ Professional SJT",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/graduate-professional-sjt/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Situational judgement for graduate and professional roles measuring workplace judgment and decision making.",
        "job_levels": ["Graduate", "Professional"],
        "keywords": ["graduate", "professional", "judgement", "decision making", "early career", "SJT"]
    },
    {
        "name": "Dependability & Safety Instrument (DSI)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/dependability-safety-instrument-dsi/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Biodata-based assessment measuring dependability, safety orientation and counter-productive work behavior risk.",
        "job_levels": ["Entry Level", "Operational"],
        "keywords": ["safety", "dependability", "warehouse", "manufacturing", "driver", "blue collar", "operational", "HSE"]
    },
    {
        "name": "Sales Representative Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sales-representative-solution/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "SJT for sales roles assessing customer engagement, persuasion and handling objections.",
        "job_levels": ["Entry Level", "Professional"],
        "keywords": ["sales", "sales rep", "business development", "account executive", "retail sales", "persuasion"]
    },
    {
        "name": "Call Center Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/call-center-solution/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Assessment for call centre agents measuring communication, service orientation and problem resolution.",
        "job_levels": ["Entry Level"],
        "keywords": ["call centre", "call center", "customer support", "helpdesk", "bpo", "inbound", "outbound"]
    },
    {
        "name": "Workplace Safety Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/workplace-safety-solution/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Measures attitudes and behaviors related to workplace safety, risk awareness and rule adherence.",
        "job_levels": ["Entry Level", "Operational"],
        "keywords": ["safety", "health and safety", "hse", "warehouse", "manufacturing", "construction", "compliance"]
    },
    {
        "name": "Entry Level Sales Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/entry-level-sales-solution/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Pre-employment battery for entry-level sales roles measuring sales aptitude and service orientation.",
        "job_levels": ["Entry Level"],
        "keywords": ["entry level sales", "sales associate", "retail", "sales trainee", "junior sales"]
    },
    {
        "name": "Supervisory Solution",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/supervisory-solution/",
        "test_type": "B",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "SJT for supervisory and team leader roles measuring leadership judgment, delegation and team management.",
        "job_levels": ["Manager", "Team Leader"],
        "keywords": ["supervisor", "team leader", "first-line manager", "foreman", "lead", "delegation"]
    },

    # ── KNOWLEDGE & SKILLS ────────────────────────────────────────────────
    {
        "name": "Java 8 (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/java-8-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests Java 8 knowledge: OOP, collections, streams, lambdas, concurrency, and core APIs.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["java", "developer", "backend", "software engineer", "programming", "j2ee", "java 8"]
    },
    {
        "name": "Core Java (Advanced Level)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/core-java-advanced-level-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Advanced Java: multithreading, design patterns, JVM internals, enterprise patterns for senior developers.",
        "job_levels": ["Professional", "Senior Professional"],
        "keywords": ["java", "advanced", "senior developer", "architect", "backend", "design patterns", "jvm"]
    },
    {
        "name": "Python (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/python-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests Python: syntax, data structures, OOP, standard libraries, file handling.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["python", "developer", "data science", "machine learning", "scripting", "backend", "automation", "django", "flask"]
    },
    {
        "name": "JavaScript (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/javascript-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Assesses JavaScript: ES6+, DOM, async/await, closures, prototypes.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["javascript", "js", "frontend", "web developer", "react", "node", "fullstack", "es6"]
    },
    {
        "name": "SQL (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/sql-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests SQL: SELECT, JOINs, aggregations, subqueries, database design and optimization.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["sql", "database", "data analyst", "backend", "data engineer", "reporting", "mysql", "postgres"]
    },
    {
        "name": "C# (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/c-sharp-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Assesses C# and .NET knowledge for backend development roles.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["c#", ".net", "dotnet", "microsoft", "backend developer", "windows development", "csharp"]
    },
    {
        "name": ".NET Framework 4.5",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/net-framework-4-5/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 30,
        "description": "Comprehensive adaptive assessment of .NET Framework 4.5 development skills.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": [".net", "dotnet", "c#", "microsoft", "backend", "framework"]
    },
    {
        "name": "C Programming (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/c-programming-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 10,
        "description": "Tests C: pointers, memory management, procedural programming and embedded concepts.",
        "job_levels": ["Professional"],
        "keywords": ["c programming", "embedded", "systems", "firmware", "low-level", "hardware"]
    },
    {
        "name": "C++ (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/c-plus-plus-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests C++: OOP, templates, STL, memory management and modern C++ features.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["c++", "cpp", "systems developer", "game developer", "embedded", "high performance"]
    },
    {
        "name": "PHP (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/php-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests PHP programming knowledge for web development roles.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["php", "web developer", "backend", "laravel", "wordpress", "server-side"]
    },
    {
        "name": "HTML/CSS (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/html-css-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests HTML and CSS knowledge for frontend web development and design.",
        "job_levels": ["Professional", "Entry Level"],
        "keywords": ["html", "css", "frontend", "web designer", "ui developer", "markup"]
    },
    {
        "name": "React (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/react-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Assesses React.js: components, hooks, state management, lifecycle and JSX.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["react", "reactjs", "frontend developer", "ui developer", "javascript", "hooks", "redux"]
    },
    {
        "name": "Data Science (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/data-science-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Tests conceptual knowledge of machine learning, data analysis, statistics and data-driven decision making.",
        "job_levels": ["Mid-Professional", "Professional"],
        "keywords": ["data science", "machine learning", "ai", "ml", "statistics", "data analyst", "sklearn"]
    },
    {
        "name": "Android (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/android-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests Android development: Activities, Fragments, APIs, mobile architecture patterns.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["android", "mobile developer", "app developer", "kotlin", "java mobile", "android studio"]
    },
    {
        "name": "iOS/Swift (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/ios-swift-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests iOS app development using Swift and Apple frameworks.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["ios", "swift", "apple", "mobile developer", "iphone", "app developer", "xcode"]
    },
    {
        "name": "Cybersecurity (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/cybersecurity-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Measures knowledge of cybersecurity principles, network security, encryption and threat analysis.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["cybersecurity", "security", "infosec", "network security", "penetration testing", "soc analyst", "ethical hacking"]
    },
    {
        "name": "Cloud Computing (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/cloud-computing-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests cloud computing concepts: IaaS, PaaS, SaaS, and major providers (AWS, Azure, GCP).",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["cloud", "aws", "azure", "gcp", "devops", "infrastructure", "cloud engineer", "serverless"]
    },
    {
        "name": "DevOps (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/devops-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests DevOps concepts: CI/CD pipelines, containerization, infrastructure as code and monitoring.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["devops", "ci/cd", "docker", "kubernetes", "jenkins", "infrastructure", "sre", "terraform"]
    },
    {
        "name": "Agile Software Development",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/agile-software-development/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests knowledge of Agile methodologies: Scrum, Kanban, sprints and agile delivery practices.",
        "job_levels": ["Professional", "Manager"],
        "keywords": ["agile", "scrum", "kanban", "project manager", "scrum master", "product owner", "sprint"]
    },
    {
        "name": "Business Analysis (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/business-analysis-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Measures business analysis techniques: requirements gathering, process mapping and stakeholder management.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["business analyst", "ba", "requirements", "stakeholder", "process analysis", "BPMN"]
    },
    {
        "name": "Accounting (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/accounting-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 25,
        "description": "Tests accounting: GAAP, financial statements, journal entries and reconciliation.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["accounting", "finance", "accountant", "bookkeeper", "financial reporting", "cpa", "gaap"]
    },
    {
        "name": "Financial Accounting",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/financial-accounting/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 30,
        "description": "Comprehensive financial accounting for finance professionals: IFRS, GAAP, financial analysis.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["financial accounting", "finance", "accountant", "ifrs", "gaap", "balance sheet", "P&L"]
    },
    {
        "name": "Microsoft Excel (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/microsoft-excel-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests Excel proficiency: formulas, pivot tables, VLOOKUP, data analysis and charts.",
        "job_levels": ["Entry Level", "Professional", "Clerical"],
        "keywords": ["excel", "spreadsheet", "office", "admin", "finance", "analyst", "data entry", "pivot table"]
    },
    {
        "name": "Microsoft Word (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/microsoft-word-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests Word proficiency: document formatting, styles, mail merge and collaboration features.",
        "job_levels": ["Entry Level", "Clerical"],
        "keywords": ["word", "microsoft office", "admin", "secretary", "clerical", "documentation", "report writing"]
    },
    {
        "name": "Project Management (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/project-management-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests project management knowledge: planning, risk management, stakeholder management, PMI/PRINCE2.",
        "job_levels": ["Professional", "Manager"],
        "keywords": ["project manager", "pm", "pmp", "prince2", "project management", "program manager", "waterfall"]
    },
    {
        "name": "R Programming (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/r-programming-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests R programming for statistical analysis and data science applications.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["r programming", "statistics", "data science", "data analyst", "research analyst", "ggplot"]
    },
    {
        "name": "Scala (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/scala-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Measures Scala knowledge for big data and functional programming roles.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["scala", "spark", "data engineer", "big data", "functional programming", "hadoop"]
    },
    {
        "name": "Go (Golang) (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/go-golang-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests Go (Golang): goroutines, channels, interfaces and standard library.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["go", "golang", "backend developer", "microservices", "cloud", "concurrency"]
    },
    {
        "name": "Rust (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/rust-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests Rust: ownership, borrowing, concurrency and safe systems programming.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["rust", "systems programming", "low-level", "webassembly", "backend", "memory safe"]
    },
    {
        "name": "UNIX (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/unix-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 15,
        "description": "Tests Unix/Linux system administration and command-line skills.",
        "job_levels": ["Professional"],
        "keywords": ["unix", "linux", "sysadmin", "devops", "shell scripting", "systems administrator", "bash"]
    },
    {
        "name": "Network Administration (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/network-administration-new/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Tests network administration: TCP/IP, routing, switching, network security.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["network", "networking", "sysadmin", "infrastructure", "cisco", "network engineer", "tcp ip"]
    },
    {
        "name": "Global Skills Assessment (GSA)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/global-skills-assessment/",
        "test_type": "K",
        "remote_testing": True,
        "adaptive_irt": True,
        "duration_min": 30,
        "description": "Adaptive broad workplace skills assessment covering communication, analytical thinking and collaboration.",
        "job_levels": ["Graduate", "Professional", "Mid-Professional"],
        "keywords": ["skills assessment", "broad skills", "general", "communication", "analytical", "graduate", "GSA", "collaboration"]
    },

    # ── SIMULATIONS ───────────────────────────────────────────────────────
    {
        "name": "Automata Data Science (New)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-data-science-new/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 60,
        "description": "Hands-on simulation: analyse and modify data using ML algorithms in a real coding environment.",
        "job_levels": ["Mid-Professional", "Professional"],
        "keywords": ["data science", "machine learning", "ml engineer", "data engineer", "ai simulation", "python", "coding"]
    },
    {
        "name": "Automata - Selenium",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-selenium/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 60,
        "description": "Practical Selenium test automation simulation in a real coding environment.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["selenium", "test automation", "qa engineer", "sdet", "quality assurance", "testing"]
    },
    {
        "name": "Automata - Fix (Java)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-fix-java/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 45,
        "description": "Java debugging simulation: candidates identify and fix bugs in existing Java code.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["java", "debugging", "code fix", "developer", "software engineer", "bug fixing"]
    },
    {
        "name": "Automata - Front End (JavaScript)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-front-end-javascript/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 45,
        "description": "Frontend coding simulation: practical JavaScript, HTML and CSS in a real browser environment.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["frontend", "javascript", "html", "css", "web developer", "ui engineer", "dom"]
    },
    {
        "name": "Automata - Pro (Full Stack)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/automata-pro/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 75,
        "description": "Comprehensive full-stack coding simulation testing both frontend and backend skills.",
        "job_levels": ["Professional", "Senior Professional"],
        "keywords": ["full stack", "fullstack", "senior developer", "software engineer", "backend", "frontend", "api"]
    },
    {
        "name": "SHL Coding Simulation",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/shl-coding-simulation/",
        "test_type": "S",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 60,
        "description": "Live IDE-like coding simulation supporting multiple languages testing algorithmic thinking.",
        "job_levels": ["Professional", "Mid-Professional"],
        "keywords": ["coding", "programming", "software engineer", "developer", "algorithm", "technical test", "leetcode"]
    },

    # ── COMPETENCIES & EXERCISES ──────────────────────────────────────────
    {
        "name": "Universal Competency Framework (UCF)",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/universal-competency-framework/",
        "test_type": "C",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 20,
        "description": "Behavioral questionnaire measuring 20 key workplace competencies based on SHL's UCF model.",
        "job_levels": ["Professional", "Manager", "Director"],
        "keywords": ["competency", "leadership", "behaviors", "development", "talent management", "UCF", "360"]
    },
    {
        "name": "Smart Interview On-Demand",
        "url": "https://www.shl.com/solutions/products/product-catalog/view/smart-interview-on-demand/",
        "test_type": "E",
        "remote_testing": True,
        "adaptive_irt": False,
        "duration_min": 30,
        "description": "AI-powered on-demand video interview platform for structured candidate screening at scale.",
        "job_levels": ["Graduate", "Professional", "Mid-Professional", "Manager"],
        "keywords": ["video interview", "on-demand interview", "ai interview", "screening", "structured interview", "candidate experience"]
    },
]

# Fast lookup
CATALOG_BY_URL = {a["url"]: a for a in SHL_CATALOG}
VALID_URLS = set(CATALOG_BY_URL.keys())
