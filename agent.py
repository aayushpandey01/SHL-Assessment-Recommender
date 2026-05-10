"""
SHL Assessment Recommender Agent
Core retrieval and ranking logic using TF-IDF + keyword matching.
Designed for fast, reliable recommendations without external vector DB dependency.
"""

import re
from typing import List, Dict, Optional, Tuple
from catalog import SHL_CATALOG, TEST_TYPE_LABELS

# ─────────────────────────────────────────────
# Lightweight retrieval engine (no vector DB needed)
# ─────────────────────────────────────────────

STOP_WORDS = {"the", "a", "an", "for", "to", "in", "of", "and", "or", "is", "are",
              "with", "who", "we", "i", "they", "need", "want", "looking", "hire",
              "hiring", "role", "position", "candidate", "candidates", "level", "levels"}

# Keyword boosting maps — domain signals → catalog keywords
DOMAIN_SIGNALS = {
    # Tech roles
    "java": ["java", "java 8", "OOP", "backend", "programming"],
    "python": ["python", "programming", "data science", "automation"],
    "javascript": ["javascript", "frontend", "web", "developer"],
    "js": ["javascript", "frontend", "web"],
    "react": ["javascript", "frontend", "web"],
    "node": ["javascript", "backend", "web"],
    ".net": [".NET", "C#", "Microsoft"],
    "c#": [".NET", "C#", "Microsoft"],
    "sql": ["SQL", "database", "data"],
    "data scientist": ["data science", "machine learning", "statistics", "python", "analytics"],
    "data science": ["data science", "machine learning", "statistics"],
    "machine learning": ["data science", "machine learning", "AI", "python"],
    "devops": ["devops", "CI/CD", "docker", "kubernetes", "cloud"],
    "cloud": ["devops", "cloud", "AWS", "infrastructure"],
    "security": ["cybersecurity", "security", "threats"],
    "cybersecurity": ["cybersecurity", "security"],
    "developer": ["programming", "coding", "software"],
    "software engineer": ["programming", "coding", "software", "developer"],
    "frontend": ["javascript", "frontend", "web"],
    "backend": ["programming", "backend", "developer"],
    "fullstack": ["javascript", "programming", "frontend", "backend"],
    "full stack": ["javascript", "programming", "frontend", "backend"],
    
    # Business roles
    "sales": ["sales", "persuasion", "customer", "drive"],
    "customer service": ["customer service", "empathy", "support"],
    "call center": ["call center", "customer service", "BPO"],
    "bpo": ["call center", "customer service", "BPO"],
    "manager": ["management", "leadership", "teamwork"],
    "leader": ["leadership", "management", "senior"],
    "executive": ["leadership", "executive", "director", "senior"],
    "director": ["leadership", "director", "executive", "senior"],
    "finance": ["finance", "accounting", "quantitative", "numerical"],
    "accounting": ["accounting", "finance", "GAAP"],
    "accountant": ["accounting", "finance", "GAAP"],
    "analyst": ["analysis", "data", "numerical", "quantitative"],
    "data analyst": ["SQL", "data", "analytics", "excel", "numerical"],
    "project manager": ["project management", "PM", "stakeholder", "planning"],
    "business analyst": ["business analysis", "BA", "requirements", "stakeholder"],
    "hr": ["personality", "behavior", "culture"],
    "recruiter": ["personality", "behavior"],
    "marketing": ["personality", "communication", "creative"],
    
    # Assessment type hints
    "personality": ["personality", "behavior", "traits"],
    "cognitive": ["cognitive", "aptitude", "reasoning"],
    "aptitude": ["aptitude", "cognitive", "reasoning"],
    "coding test": ["coding", "programming", "practical"],
    "technical test": ["programming", "knowledge", "technical"],
    "situational": ["situational judgement", "SJT", "scenario"],
    "remote": ["remote", "WFH", "work from home"],
    "graduate": ["graduate", "campus", "entry level"],
    "entry level": ["entry level", "clerical", "operational"],
    "senior": ["senior", "professional", "advanced"],
    "stakeholder": ["stakeholder", "interpersonal", "communication"],
    "agile": ["agile", "scrum", "methodology"],
    "safety": ["safety", "manufacturing", "compliance"],
    "manufacturing": ["safety", "manufacturing", "mechanical"],
    "warehouse": ["safety", "warehouse", "logistics"],
    "engineering": ["engineering", "mechanical", "technical"],
}

# Level normalization
LEVEL_ALIASES = {
    "entry": "Entry-level",
    "junior": "Entry-level",
    "fresher": "Entry-level",
    "associate": "Entry-level",
    "mid": "Professional",
    "mid-level": "Professional",
    "intermediate": "Professional",
    "senior": "Professional",
    "staff": "Professional",
    "principal": "Professional",
    "lead": "Manager",
    "manager": "Manager",
    "team lead": "Manager",
    "director": "Director",
    "vp": "Director",
    "c-level": "Executive",
    "executive": "Executive",
    "ceo": "Executive",
    "cto": "Executive",
    "graduate": "Graduate",
    "campus": "Graduate",
    "intern": "Graduate",
    "trainee": "Graduate",
}


def normalize_level(text: str) -> Optional[str]:
    text_lower = text.lower()
    for alias, level in LEVEL_ALIASES.items():
        if alias in text_lower:
            return level
    return None


def extract_signals(conversation_text: str) -> Dict:
    """
    Extract job role, level, test type preferences, and keywords from conversation.
    Returns a dict of signals.
    """
    text = conversation_text.lower()
    signals = {
        "keywords": set(),
        "levels": set(),
        "preferred_types": set(),
        "excluded_types": set(),
        "raw_text": text
    }

    # Extract level signals
    level = normalize_level(text)
    if level:
        signals["levels"].add(level)
    
    # Extract years of experience → level
    year_match = re.search(r'(\d+)\s*(?:to\s*\d+\s*)?years?', text)
    if year_match:
        years = int(year_match.group(1))
        if years <= 1:
            signals["levels"].add("Entry-level")
        elif years <= 3:
            signals["levels"].add("Graduate")
            signals["levels"].add("Professional")
        elif years <= 7:
            signals["levels"].add("Professional")
        else:
            signals["levels"].add("Manager")
            signals["levels"].add("Professional")

    # Map domain signals to keywords
    for trigger, kws in DOMAIN_SIGNALS.items():
        if trigger in text:
            signals["keywords"].update(kws)

    # Detect explicit test type preferences
    type_hints = {
        "personality": "P",
        "aptitude": "A",
        "ability": "A",
        "cognitive": "A",
        "reasoning": "A",
        "knowledge": "K",
        "skills test": "K",
        "coding": "S",
        "simulation": "S",
        "behavioral": "B",
        "situational": "S",
        "360": "D",
    }
    for hint, code in type_hints.items():
        if hint in text:
            signals["preferred_types"].add(code)

    # Generic word extraction (fallback)
    words = re.findall(r'\b[a-z][a-z+#.]{2,}\b', text)
    for w in words:
        if w not in STOP_WORDS:
            signals["keywords"].add(w)

    return signals


def score_assessment(assessment: Dict, signals: Dict) -> float:
    """
    Score a catalog item against extracted signals.
    Higher = better match.
    """
    score = 0.0
    keywords = signals["keywords"]
    levels = signals["levels"]
    preferred_types = signals["preferred_types"]

    # Keyword matching against assessment keywords
    assessment_kws = {k.lower() for k in assessment.get("keywords", [])}
    assessment_name = assessment["name"].lower()
    assessment_desc = assessment["description"].lower()

    for kw in keywords:
        kw_lower = kw.lower()
        if kw_lower in assessment_kws:
            score += 3.0
        elif kw_lower in assessment_name:
            score += 2.5
        elif kw_lower in assessment_desc:
            score += 1.0

    # Level matching
    if levels:
        assessment_levels = set(assessment.get("job_levels", []))
        if levels & assessment_levels:
            score += 2.0

    # Preferred test type boost
    assessment_types = set(assessment.get("test_type", []))
    if preferred_types & assessment_types:
        score += 2.0

    return score


def retrieve_assessments(
    signals: Dict,
    top_k: int = 10,
    min_score: float = 0.5
) -> List[Dict]:
    """
    Retrieve and rank assessments from catalog based on signals.
    Returns top_k results above min_score threshold.
    """
    scored = []
    for assessment in SHL_CATALOG:
        s = score_assessment(assessment, signals)
        if s >= min_score:
            scored.append((s, assessment))

    scored.sort(key=lambda x: x[0], reverse=True)
    results = [item for _, item in scored[:top_k]]
    return results


def format_catalog_context(assessments: List[Dict]) -> str:
    """Format a list of assessments as a readable context block for the LLM."""
    lines = []
    for a in assessments:
        types = ", ".join([f"{t} ({TEST_TYPE_LABELS.get(t, t)})" for t in a.get("test_type", [])])
        levels = ", ".join(a.get("job_levels", []))
        lines.append(
            f"• **{a['name']}** [Types: {types}] [Levels: {levels}]\n"
            f"  URL: {a['url']}\n"
            f"  {a['description']}\n"
        )
    return "\n".join(lines)


def get_all_catalog_context() -> str:
    """Get full catalog as context — used for comparison queries."""
    return format_catalog_context(SHL_CATALOG)


def is_comparison_query(messages: List[Dict]) -> Tuple[bool, List[str]]:
    """Detect if user is asking to compare specific assessments."""
    last_user_msg = ""
    for m in reversed(messages):
        if m["role"] == "user":
            last_user_msg = m["content"].lower()
            break

    comparison_patterns = [
        r'difference between (.+) and (.+)',
        r'compare (.+) (?:with|vs|versus|and) (.+)',
        r'(.+) vs\.? (.+)',
        r'which is better[,:]? (.+) or (.+)',
    ]

    for pattern in comparison_patterns:
        match = re.search(pattern, last_user_msg)
        if match:
            names = [match.group(1).strip(), match.group(2).strip()]
            # Find which catalog items these correspond to
            found = []
            for name in names:
                for item in SHL_CATALOG:
                    if name.lower() in item["name"].lower() or item["name"].lower() in name.lower():
                        found.append(item)
                        break
            return True, found

    return False, []


def build_conversation_text(messages: List[Dict]) -> str:
    """Flatten conversation history to a single text for signal extraction."""
    parts = []
    for m in messages:
        if m["role"] == "user":
            parts.append(m["content"])
    return " ".join(parts)


def is_vague_query(messages: List[Dict]) -> bool:
    """
    Determine if we have enough context to recommend, or if we need to clarify.
    Returns True if the query is too vague.
    """
    conversation_text = build_conversation_text(messages)
    signals = extract_signals(conversation_text)

    # Must have at least a role or skill signal
    has_role_signal = bool(signals["keywords"] - STOP_WORDS)
    has_level = bool(signals["levels"])

    # Very short first message with no specifics
    if len(messages) == 1:
        content = messages[0]["content"]
        words = content.lower().split()
        meaningful = [w for w in words if w not in STOP_WORDS and len(w) > 3]
        if len(meaningful) < 2:
            return True

    # If we have role signals but not level, it's still actionable (level is optional)
    return not has_role_signal


def is_off_topic(message: str) -> bool:
    """Detect off-topic or prompt injection attempts."""
    off_topic_patterns = [
        r'ignore (previous|all|above|your)',
        r'forget (your|the|all)',
        r'you are now',
        r'act as',
        r'pretend (you are|to be)',
        r'legal (advice|question)',
        r'lawsuit',
        r'salary negotiation',
        r'how to fire',
        r'interview tips for candidate',
        r'write (my|a) resume',
        r'cover letter',
        r'job (application|apply)',
        r'visa',
        r'immigration',
    ]
    msg_lower = message.lower()
    for pat in off_topic_patterns:
        if re.search(pat, msg_lower):
            return True
    
    # Check if completely unrelated to hiring/assessments
    hiring_signals = ["hire", "hiring", "assess", "test", "role", "position", "candidate",
                      "job", "recruit", "developer", "manager", "engineer", "analyst",
                      "skill", "aptitude", "personality", "cognitive", "shl", "evaluation"]
    has_hiring_context = any(s in msg_lower for s in hiring_signals)
    
    # Only flag as off-topic if clearly not about hiring
    very_off_topic = ["weather", "recipe", "cook", "movie", "song", "write a poem",
                      "tell me a joke", "what is the capital", "who is the president",
                      "stock price", "cryptocurrency", "bitcoin"]
    if any(s in msg_lower for s in very_off_topic):
        return True

    return False
