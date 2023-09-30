## security_checker.py
import subprocess
import logging

class SecurityChecker:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def check_code(self) -> None:
        """
        Check the code for security issues using Bandit.
        """
        try:
            result = subprocess.run(["bandit", "-r", "."], capture_output=True, text=True)
            self.logger.info(f"Security check completed.\n{result.stdout}")
        except Exception as e:
            self.logger.error(f"Error occurred while checking code: {e}")
