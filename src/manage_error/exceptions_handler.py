import traceback
from log.logger import log_event

def handle_exception(func_name: str, error: Exception):
    print("Oops! Something went wrong. Please try again.")
    print("Debug:", error)
    tb = traceback.format_exc()
    log_event("error", f"Error in {func_name}: {error}\n{tb}")
