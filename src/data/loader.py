from pathlib import Path
from typing import Dict
from pypdf import PdfReader
import docx

print("🚀 Script is running!")

class DataLoader:
    """Loads all resume-related data from the data/ directory."""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.resumes_dir = self.data_dir / "resumes"
        self.summaries_dir = self.data_dir / "summaries"
        self.linkedin_path = self.data_dir / "linkedin.pdf"
        
        # Storage for loaded data
        self.resumes: Dict[str, str] = {}
        self.summaries: Dict[str, str] = {}
        self.linkedin_text: str = ""

    def load_all(self) -> Dict[str, any]:
        """Load all data: resumes, summaries, and LinkedIn profile."""
        print("📂 Loading resume data...")
    
        # Load resumes
        self.resumes = self._load_resumes()
        print(f"   ✅ Loaded {len(self.resumes)} resume(s)")
    
        # Load summaries
        self.summaries = self._load_summaries()
        print(f"   ✅ Loaded {len(self.summaries)} summary file(s)")
    
        # Load LinkedIn profile
        self.linkedin_text = self._load_linkedin()
        print(f"   ✅ Loaded LinkedIn profile")

        return {
            "resumes": self.resumes,
            "summaries": self.summaries,
            "linkedin": self.linkedin_text      
        }


    def _load_resumes(self) -> Dict[str, str]:
        """Load all resume files from the resumes directory."""
        resumes = {}
    
        if not self.resumes_dir.exists():
           print(f"   ⚠️  Warning: {self.resumes_dir} not found")
           return resumes
    
        # Find all .docx and .pdf files
        for file_path in self.resumes_dir.iterdir():
            if file_path.suffix.lower() in ['.docx', '.pdf']:
               try:
                   content = self._extract_text(file_path)
                   # Use filename (without extension) as key
                   key = file_path.stem
                   resumes[key] = content
               except Exception as e:
                   print(f"   ⚠️  Failed to load {file_path.name}: {e}")
    
        return resumes


    def _load_summaries(self) -> Dict[str, str]:
       """Load all summary text files."""
       summaries = {}
    
       if not self.summaries_dir.exists():
          print(f"   ⚠️  Warning: {self.summaries_dir} not found")
          return summaries
    
      # Find all .txt files
       for file_path in self.summaries_dir.iterdir():
          if file_path.suffix.lower() == '.txt':
             try:
                 with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                 key = file_path.stem
                 summaries[key] = content
             except Exception as e:
                print(f"   ⚠️  Failed to load {file_path.name}: {e}")
    
       return summaries


    def _load_linkedin(self) -> str:
       """Load LinkedIn profile PDF."""
       if not self.linkedin_path.exists():
         print(f"   ⚠️  Warning: {self.linkedin_path} not found")
         return ""
    
       try:
           return self._extract_text(self.linkedin_path)
       except Exception as e:
        print(f"   ⚠️  Failed to load LinkedIn profile: {e}")
        return ""
   

    def _extract_text(self, file_path: Path) -> str:
       """Extract text from .docx or .pdf files."""
       if file_path.suffix.lower() == '.pdf':
         return self._extract_pdf_text(file_path)
       elif file_path.suffix.lower() == '.docx':
         return self._extract_docx_text(file_path)
       else:
         raise ValueError(f"Unsupported file type: {file_path.suffix}")

    def _extract_pdf_text(self, pdf_path: Path) -> str:
       """Extract text from PDF file."""
       reader = PdfReader(pdf_path)
       text = ""
       for page in reader.pages:
           page_text = page.extract_text()
           if page_text:
              text += page_text + "\n"
           return text.strip()
    

    def _extract_docx_text(self, docx_path: Path) -> str:
        """Extract text from DOCX file."""
        doc = docx.Document(docx_path)
        paragraphs = [para.text for para in doc.paragraphs]
        return "\n".join(paragraphs).strip()


if __name__ == "__main__":
    # Test the loader
    print("Testing Data Loader...")
    print("=" * 60)
    
    loader = DataLoader()
    data = loader.load_all()
    
    print("\n📋 Data Summary:")
    print(f"   Resumes found: {list(data['resumes'].keys())}")
    print(f"   Summaries found: {list(data['summaries'].keys())}")
    print(f"   LinkedIn profile: {'✅' if data['linkedin'] else '❌'}")