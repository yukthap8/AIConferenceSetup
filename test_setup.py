def greet_conference_attendee(name, role="Attendee"):
    """
    A simple greeting function for AI conference attendees
    """
    print(f"Welcome to the AI Conference, {name}!")
    print(f"You are registered as: {role}")
    return True

def test_environment():
    """
    Basic function to test Python environment functionality
    """
    # Test basic operations
    test_number = 42
    test_string = "AI Conference"
    test_list = [1, 2, 3, 4, 5]
    
    # Perform some operations to test IDE features
    try:
        # Test arithmetic
        result = test_number * 2
        
        # Test string manipulation
        upper_string = test_string.upper()
        
        # Test list operations
        list_sum = sum(test_list)
        
        print("Environment Test Results:")
        print("-" * 30)
        print(f"Number operation: {result}")
        print(f"String operation: {upper_string}")
        print(f"List operation: {list_sum}")
        print("\nAll tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"Test failed with error: {str(e)}")
        return False

if __name__ == "__main__":
    # Run some example code
    print("Starting IDE Test Script...")
    print("=" * 30)
    
    # Test the greeting function
    greet_conference_attendee("John Doe", "Speaker")
    print("\n")
    
    # Run environment tests
    test_environment() 