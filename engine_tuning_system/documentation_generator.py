import subprocess
import logging

class DocumentationGenerator:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def generate_docs(self) -> None:
        """
        Generate the project documentation using Sphinx.
        
        This method assumes that Sphinx is properly configured and the docs are in a directory named "docs".
        """
        try:
            result = subprocess.run(["sphinx-build", "-b", "html", "docs", "docs/_build"], capture_output=True, text=True)
            self.logger.info(f"Documentation generated successfully.\n{result.stdout}")
        except Exception as e:
            self.logger.error(f"Error occurred while generating documentation: {e}")
