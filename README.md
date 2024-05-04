# Michael's Website

## Launching local test site (via Docker)

`docker compose up --build`

---
## Updating Website Template
Current process for updating the website template from the [upstream repository](https://github.com/alshedivat/al-folio):
1. `git checkout al-folio`
    - For extra safety I'm going to pull template updates on an isolated branch in case I mess anything up
2. `git fetch upstream`
    - D
3. `git pull --rebase`



## Generating CV File
I'm going to have the script generate a `.docx` CV file in the off chance that anybody requires that format. (Its often easier to go from `.docx` -> `.pdf` rather than the other way around). 

### Custom CV System Changes

- Allow links to certificate/degree files on website but remove for LaTex-PDF generation
- aaa









