# curl Examples

## 1. List available templates

curl -X GET http://127.0.0.1:5000/templates

## 2. Generate HTML resume

curl -X POST http://127.0.0.1:5000/generate-resume \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_profile": {
      "name": "Meera Shah",
      "title": "Full Stack Engineer",
      "location": "Pune, India",
      "email": "meera.shah@example.com",
      "phone": "+91-98765-00002",
      "summary": "Full stack engineer with 4+ years of experience building SaaS products using React, Node.js, and PostgreSQL.",
      "skills": ["JavaScript", "TypeScript", "React", "Node.js"],
      "experience": [
        {
          "company": "CloudSprint",
          "title": "Software Engineer",
          "location": "Pune, India",
          "start": "2021-03",
          "end": "Present",
          "bullets": [
            "Developed and maintained a React + Node.js subscription billing platform.",
            "Implemented role-based access control APIs."
          ]
        }
      ],
      "education": [
        {
          "degree": "Bachelor of Engineering in Information Technology",
          "institution": "SPPU",
          "location": "Pune, India",
          "date": "2019",
          "details": ["First Class with Distinction."]
        }
      ],
      "extra": ["Spoke at local JS meetup on debugging React apps."]
    },
    "job_description": "Job Title: Full Stack Engineer\nResponsibilities:\n- Build and maintain web applications\nRequirements:\n- Experience with React and Node.js",
    "template_id": 2,
    "top_k": 8,
    "output_format": "html"
  }'

## 3. Generate Markdown resume

curl -X POST http://127.0.0.1:5000/generate-resume \
  -H "Content-Type: application/json" \
  -d '{
    "candidate_profile": {
      "name": "Aarav Kumar",
      "title": "Software Engineer (Entry Level)",
      "location": "Bengaluru, India",
      "email": "aarav.kumar@example.com",
      "phone": "+91-98765-00001",
      "summary": "Computer Science graduate with strong fundamentals in data structures, algorithms, and web development.",
      "skills": ["JavaScript", "React", "Node.js"],
      "experience": [],
      "education": [],
      "extra": []
    },
    "job_description": "Job Title: Frontend Engineer\nResponsibilities:\n- Build responsive UIs using React\nRequirements:\n- Strong JavaScript skills",
    "template_id": 1,
    "top_k": 5,
    "output_format": "markdown"
  }'
