# Job Application Pipeline: Models

```mermaid
erDiagram
    Job ||--|| JobApplicationSite: has
    DomInteractionApi ||--o{ FormFillVerificationResults: Has
    SiteForm ||--|| DomInteractionApi : has
    JobApplicationSite ||--|{ SiteForm: has
```

