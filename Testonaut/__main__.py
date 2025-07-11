import sys
import pytest


def main():
    print("\n🚀 Testonaut: Launching your tests! 🚀\n")
    # Run pytest programmatically
    exit_code = pytest.main()
    if exit_code == 0:
        print("\n✅ All systems go! No test failures detected.\n")
    else:
        print("\n❌ Testonaut detected some issues. Check the logs above.\n")
    sys.exit(exit_code)


if __name__ == "__main__":
    main() 