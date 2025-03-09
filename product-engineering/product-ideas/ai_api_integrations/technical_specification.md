# Project: Scheduled Automated Job Application Pipeline

This document defines the architecture, API design, and other engineering constraints that will have to be addressed.

## **Tech Stack**
- **Framework:** 
- **Mock Data:** JSON API for testing

## **Features & Functionality**

### **1 User Authentication (Protected Routes)**
- **Login / Signup Pages** (with OTP or email/password)
- **Protected Routes:** Only logged-in users can apply to jobs
- **JWT Token Management:** Store tokens in HTTP-only cookies
- **Redux Store Integration:** Store user data globally

### **2 Job Application System**
- **List Jobs currently applied to:** Fetch from mock JSON API (`/api/jobs`)
- **Job application:** Users choose a job, then a request is sent to the mock JSON API (`/api/apply`)
- **Job Status:** Show users whether their application is either ("Pending", "Applied")
- **Ask user to fill unique questions:** If the back-end tries to apply but encounters unique questions by the 
application form, it will show the user in a drop-down with suggested answers.

### **3 Job application Dashboard**
- **Add New Job:** Able to pull jobs from LinkedIn and load them in the dashboard
- **Track Job applications:** View ongoing & completed applications
- **Payment Integration (Mocked for now):** Pay subscription to the platform

### 4. Auto apply feature 
- Set it and forget it. The platform will decide which jobs it thinks you fit well with and applies on your behalf. 
- Show the number of new jobs applied to today. A drop-down is available to see more detail on each application.

### **6 Mobile-First UI (Tailwind CSS Responsive Design)**
- **Sticky Bottom Navbar (For Easy Mobile Access)**
- **Application Cards with application status**
- **Dark Mode Support**
- **Swipe & Tap Friendly Design**

---

## **Folder Structure (Next.js App Router)**
```bash
/src
  ├── app
  │   ├── page.tsx (Home Page - List Applications)
  │   ├── applications
  │   │   ├── [id].tsx (Single application Page)
  │   ├── apply
  │   │   ├── page.tsx (Job Dashboard - Create applications)
  ├── components
  │   ├── ApplicationCard.tsx
  │   ├── Navbar.tsx
  │   ├── Status.tsx
  ├── store
  │   ├── slices
  │   │   ├── auctionSlice.ts (Fetch Auctions, Place Bids)
  │   │   ├── userSlice.ts (User Authentication, Bidding History)
  │   ├── store.ts
  ├── pages
  │   ├── api
  │   │   ├── applications.ts (Mock API for applications)
  │   │   ├── jobs.ts (Mock API for jobs)
  │   │   ├── auth.ts (Mock Authentication API)
  │   │   ├── apply.ts (Mock API to apply)
```
---

## **Mock Data (application.json)**
```json
{
  "job": {
    "name": "Senior Software Engineer",
    "application_url": "https://company.careers/senior-swe-123"
  },
  "resume": {
    "contact_info": {
      "email": "sarah.parker@email.com",
      "phone_number": "+1 (555) 123-4567",
      "address": "123 Tech Street, San Francisco, CA 94105",
      "linkedin": "https://linkedin.com/in/sarahparker",
      "github": "https://github.com/sparker",
      "portfolio_site": "https://sarahparker.dev"
    },
    "work_experiences": [
      {
        "company": "Tech Solutions Inc.",
        "title": "Software Engineer",
        "description": "Led development of cloud-native applications using Python and React. Improved system performance by 40% through optimization of database queries and implementation of caching strategies.",
        "start_date": "2020-03-15",
        "end_date": null
      },
      {
        "company": "DataCorp Systems",
        "title": "Junior Developer",
        "description": "Developed and maintained REST APIs using Django. Collaborated with the frontend team to integrate new features and improve user experience.",
        "start_date": "2018-06-01",
        "end_date": "2020-03-01"
      }
    ],
    "educations": [
      {
        "institution": "University of California, Berkeley",
        "degree": "Bachelor of Science in Computer Science",
        "start_date": "2014-09-01",
        "end_date": "2018-05-15"
      },
      {
        "institution": "Coding Bootcamp X",
        "degree": "Full Stack Web Development Certificate",
        "start_date": "2018-01-15",
        "end_date": "2018-04-15"
      }
    ]
  }
}
```

---

## **Next Steps**
- **Step 1:** Setup Next.js with Redux Toolkit
- **Step 2:** Create API Mock Endpoints for Applications & Users
- **Step 3:** Build Protected Routes for Login & Dashboard
- **Step 4:** Develop Application Components (List, Application, Job, Status)
- **Step 5:** Implement Application Request & Job Selection Logic
- **Step 6:** Ensure Responsive & Secure UI Design

---

## **Final Notes**
- **Keep the UI simple but engaging** (focus on easy navigation & real-time updates)
- **Optimize for mobile users** (since applications should be quick & needs easy access)
- **Plan for scalability** (later integrate payments & real-time application updates)

---

This prompt covers everything required to **build a functional MVP** for the "Apply & Win" platform 🚀.
---

## Architectural Overview
[High-level architecture](./architecture/automated_job_application_pipeline_architecture.drawio)

## Data Model & Database Schema
[Data Model](./architecture/models.md)

## Classes & Services
[Services](./architecture/services.md)

## Dependencies & Third-Party Services
Browser-use library
Deepseek Agent
Langchain
Playwright
