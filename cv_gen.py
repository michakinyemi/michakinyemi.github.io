import os, yaml, re

CV_DATA = "_data/cv.yml"
TEMPLATE_DIR = "_latex/"

# --== HELPER FUNCTIONS ==--
# definitely not stealing these from old projects
def find_replace(string, dictionary):
    for item in sorted(dictionary.keys(), key = len, reverse = True):
        string = re.sub(item, dictionary[item], string)
    return string

def createTemplates():
    fileList = []
    for root, dir, files in os.walk(TEMPLATE_DIR):
        for file in files:
            fileList.append(os.path.join(root,file))

    templates = {}
    for file in fileList:
        if file.endswith(".tex"):
            text = open(file).read()
            name = os.path.basename(file)
            templates.update({name[:-4]: text})

    return templates


# Load CV data & LaTeX template



templates = createTemplates()

# for name, template in templates.items():
#     print(template)



dataDir = {
    "@NAME": 1,
}

if "@NAME" in dataDir:
    print("wah")


with open(CV_DATA, 'r') as file:
    data = yaml.safe_load(file)


for section in data:

    if section["title"] == "Education":
        

        for entry in section["contents"]:
            print(entry)




    


# --== Generate CV ==--

# os.system("pdflatex _data/main_cv.tex > /dev/null")
# os.system("rm main_cv.aux main_cv.out main_cv.log")
# os.system("mv main_cv.pdf assets/pdf/Michael_Akinyemi_CV.pdf")





# I do like how the original YAML CV system doesn't require section-specific formatting
# It has the 5 basic templates that everything is created from



