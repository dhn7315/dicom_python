import os
import pydicom
import matplotlib.pyplot as plt

def view_dicom(file_path):
    try:
        dicom_data = pydicom.dcmread(file_path)
        # Output all DICOM data
        print(f"\nDICOM File Data for {file_path}:")
        print(dicom_data)
        # Check if the DICOM file contains pixel data
        if hasattr(dicom_data, 'pixel_array'):
            pixel_array = dicom_data.pixel_array
            # Check if the pixel array is 3D
            if pixel_array.ndim == 3:
                # Display the middle slice
                slice_index = pixel_array.shape[0] // 2
                image_to_display = pixel_array[slice_index]
                print(f"Displaying slice {slice_index} of {pixel_array.shape[0]}")
            else:
                # If it's already 2D, use it directly
                image_to_display = pixel_array
            # Display the image
            plt.imshow(image_to_display, cmap=plt.cm.bone)
            plt.title(f'DICOM Image: {os.path.basename(file_path)}')
            plt.axis('off')  # Hide axes
            plt.show()
        else:
            print("No pixel data found in this DICOM file.")
    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        print("Please ensure you have the required libraries installed to handle the DICOM file format.")
        print("You can install the required libraries using the following commands:")
        print("pip install gdcm")
        print("or")
        print("pip install pylibjpeg pylibjpeg-libjpeg")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_dicom_folder(folder_path):
    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.dcm'):  # Check for DICOM files
            file_path = os.path.join(folder_path, filename)
            view_dicom(file_path)

def process_dicom_path(path):
    if os.path.isfile(path):
        # If the path is a file, process it
        if path.lower().endswith('.dcm'):
            view_dicom(path)
        else:
            print("The specified file is not a DICOM file.")
    elif os.path.isdir(path):
        # If the path is a directory, process all DICOM files in it
        process_dicom_folder(path)
    else:
        print("The specified path is neither a file nor a directory.")

if __name__ == "__main__":
    # Specify the path to a DICOM file or a folder containing DICOM files
    dicom_path = r"C:\Users\DHARANI\Downloads\dicom python\Circle of Willis"
    process_dicom_path(dicom_path)