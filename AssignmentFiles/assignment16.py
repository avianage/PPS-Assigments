
# To copy contents of one file to other. While copying 
# a) all full stops are to be replaced with commas 
# b) lower case are to be replaced with upper case 
# c) upper case are to be replaced with lower case.

input_file = input("\nEnter Input File Name: ")
output_file = input("Enter Output File Name: ")

def copy_content(input, output):
    try:
        with open(input, 'r') as file_read:
            content = file_read.read()

        modified = content.replace('.', ',')
        modified = modified.swapcase()

        with open(output, 'w') as file_write:
            file_write.write(modified)

        print("\nFile Copied with Modifications.")

    except FileNotFoundError:
        print("\nInput File Not Found.")
    except Exception as e:
        print(f"An Error Occurred: {str(e)}")

copy_content(input_file, output_file)