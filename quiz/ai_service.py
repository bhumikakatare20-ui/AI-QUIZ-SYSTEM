def generate_questions(topic, count=5):
    questions = [
        {
            "question": f"What is the primary use of {topic}?",
            "options": {"a": "Web Development", "b": "Data Science", "c": "Gaming", "d": "Networking"},
            "correct": "a",
            "explanation": f"{topic} is widely used in web development."
        },
        {
            "question": f"Which company is most associated with {topic}?",
            "options": {"a": "Google", "b": "Microsoft", "c": "Apple", "d": "Meta"},
            "correct": "b",
            "explanation": "Microsoft is widely known in this field."
        },
        {
            "question": f"What type of language is {topic}?",
            "options": {"a": "Compiled", "b": "Interpreted", "c": "Assembly", "d": "Markup"},
            "correct": "b",
            "explanation": f"{topic} is an interpreted language."
        },
        {
            "question": f"Which of these is a key feature of {topic}?",
            "options": {"a": "Low level memory access", "b": "Easy syntax", "c": "Only for mobile", "d": "No libraries"},
            "correct": "b",
            "explanation": "Easy syntax is a major advantage."
        },
        {
            "question": f"What file extension is commonly used with {topic}?",
            "options": {"a": ".java", "b": ".cpp", "c": ".py", "d": ".rb"},
            "correct": "c",
            "explanation": ".py is the standard extension."
        },
        {
            "question": f"Which of these is NOT related to {topic}?",
            "options": {"a": "Libraries", "b": "Frameworks", "c": "Assembly code", "d": "Modules"},
            "correct": "c",
            "explanation": "Assembly code is low level and unrelated."
        },
        {
            "question": f"What is a popular framework related to {topic}?",
            "options": {"a": "Laravel", "b": "Django", "c": "Spring", "d": "Rails"},
            "correct": "b",
            "explanation": "Django is a popular Python framework."
        },
        {
            "question": f"How do you run a {topic} file?",
            "options": {"a": "compile then run", "b": "directly execute", "c": "convert to binary", "d": "use a browser"},
            "correct": "b",
            "explanation": "Interpreted languages run directly."
        },
        {
            "question": f"Which of these is used for {topic} web development?",
            "options": {"a": "Flask", "b": "Unity", "c": "Android Studio", "d": "Xcode"},
            "correct": "a",
            "explanation": "Flask is a lightweight web framework."
        },
        {
            "question": f"What is the best way to learn {topic}?",
            "options": {"a": "Reading only", "b": "Practice with projects", "c": "Watching only", "d": "Memorizing syntax"},
            "correct": "b",
            "explanation": "Hands-on practice is the best way to learn."
        },
    ]
    return questions[:count]