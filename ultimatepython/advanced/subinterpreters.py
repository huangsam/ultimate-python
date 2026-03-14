"""
Multi-interpreter support via concurrent.interpreters in Python 3.14 (PEP 734).

Python subinterpreters allow running Python code in truly isolated
environments within a single process. In Python 3.14, each interpreter
has its own Global Interpreter Lock (GIL), enabling true multi-core
parallelism for Python code.
"""

import concurrent.futures
import concurrent.interpreters as interpreters


def run_worker(data):
    """Function to be run in a subinterpreter."""
    # This code runs in a different interpreter environment
    return f"Processed {data} in a subinterpreter"


def main():
    # 1. Create a subinterpreter
    # The 'interpreters' module provides a high-level API
    interp = interpreters.create()

    assert isinstance(interp, interpreters.Interpreter)
    assert interp.is_running() is False

    # 2. Run code in the subinterpreter
    # We can run simple strings of code
    interp.exec("1 + 1")

    # 3. Using InterpreterPoolExecutor for easier management
    # This is similar to ThreadPoolExecutor or ProcessPoolExecutor
    with concurrent.futures.InterpreterPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the pool
        future1 = executor.submit(run_worker, "Task A")
        future2 = executor.submit(run_worker, "Task B")

        # Get results (this handles passing data back and forth)
        result1 = future1.result()
        result2 = future2.result()

        assert result1 == "Processed Task A in a subinterpreter"
        assert result2 == "Processed Task B in a subinterpreter"

    # 4. Cleaning up
    interp.close()
    assert interp.id not in [i.id for i in interpreters.list_all()]


if __name__ == "__main__":
    main()
