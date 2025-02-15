# Job Application Pipeline: Classes & Services

```
classDiagram
    %% Services
    class AiAgent{
        +generate_dom_interaction_api(site_form_dom) ISiteFormInteractor
    }
    class JobApplicationPipeline{
        +addJob(Job) null
        +removeJob() null
    }
    class FormFillVerifier{
        +verify(site_form_dom, resume) bool
    }
    note for ISiteForm "add more methods as they become relevant"
    class ISiteFormInteractor{
        -DContactInfo contact_info
        -Array<DWorkExperience> work_experiences

        +setContactInfo(DContactInfo contact_info) null
        +setWorkExperience(Array<DWorkExperience> work_experiences) null
    }
    %% Models
    class DResume{
        +DContactInfo contact_info
        +Array<DWorkExperience> work_experiences
        +Array<DEducation> educations
    }
    class DContactInfo{
        +String email
        +String phone_number
        +String Address
        +String linkedIn
        +String github
        +String portfolio_site
    }
    class DWorkExperience{
        +String company
        +String title
        +String description
    }
    class DEducation{
        +String institution
        +String degree
    }
    class Job{
        String company
        String application_url
    }
```
    
